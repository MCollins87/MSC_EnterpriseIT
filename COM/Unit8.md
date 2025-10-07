[Back to Module](./README.md)

# Unit 8 Formative Activity

## Brief
Design and implement a Disaster Recovery (DR) plan for a cloud-based infrastructure on OpenStack. Simulate a failure scenario and perform a recovery operation using open-source backup tools such as Bacula or Duplicity.

**Deliverable**: A discussion post detailing the DR process, tools used, and a reflection on the effectiveness of the recovery strategy.

## 1: Definitions 

### Objectives
**RPO (Recovery Point Objective)**: Maximum acceptable data loss - Defines how often back-ups should be taken. 
**RTO (Recovery Time Objective)**: Maximum downtime. - Defines whether hot spare, cold spare, IaaC time to spin up new VM etc. 

### Scope
Critical OpenStack components [@heuchert2025]:
- **Controller Services**: Keystone (Identity), Glance (Images), Nova (Compute), Neutron (network API).
- **Compute Nodes**: VM workloads
- **Cinder**: Block Storage
- **Swift**: Object Storage
- **Database & Message queues**: MariaDB/Galera, RabbitMQ.

### Architecture
- **Primary Site**: Main OpenStack Cluster
- **Secondary (DR) Site**: Smaller OpenStack deployment or offsite storage
- **Backup tools**: Bacula or Duplicity to back up VM volumes, database snapshots, and configs to object storage (Swift, Ceph, or external S3).

## 2: Implementation
### Back-up Strategy
1. **Databases (Keystone, Nova, Cinder, Neutron, etc.):**
	- Use `mysqldump` or percona XtraBackup -> Store in Bacula/Duplicity
	- e.g. Duplicity:
	```bash
	duplicity /var/lib/mysql swift://container/mysql-backups
	```
2. **Configuration Files:***
	- `/etc/keystone`, `/etc/nova`, `/etc/cinder`, `/etc/neutron`
	- Back-up with Bacula File Daemon or Duplicity
3. **VM Volumes (Cinder):**
	- Snapshot Cinder Volumes --> export to Swift or Ceph RBD --> backup with Bacula/Duplicity.
	- E.g:
	``` Bash
	cinder snapshot-create --display-name "daily-backup" <volume-id>
	```
4. **Glance Images:**
	- Sync Glance image repository to backup storage.

## 3. Simulating Failure Scenario

Simulate a **Controller node failure**:
- Shut down Keystone, Glance, Nova-API, or MariaDB services to make OpenStack API inaccessible. 
```bash
systemctl stop mariadb
ststemctl stop keystone
```

## 4. Recovery Procedure
1. Restore Databases
```bash
duplicity restore swift://container/mysql-backups /var/lib/mysql-restore
systemctl start mariadb
```

2. Restore Configs
```bash
duplicity restore swift://container/config-backups /etc
```
- Restart services
```bash 
systemctl restart keystone glance-api nova-api neutron-server
```

3. Restore VM Volumes
	- Recreate Volumes from Cinder snapshots stored in backup
	- Attache them back to VM instances
4. Verify
	- Run OpenStack CLI to confirm restored services
```bash
openstack server list
openstack volume list
```

## 5. Testing and Documentation
- Perform planned DR drills quarterly
- Document:
	- Backup frequency
	- Roles/responsibilities
	- Step-by-step recovery guide
	- Verification checklist


## Example script
Example bash scrip for back-up and restore OpenStack configs and databases using Duplicity

### Assumptions
- Swift object storage in OpenStack
- Database is MariaDB/Galeria (default for OpenStack)
- Running script on Controller node

Save file as `openstack-dr.sh` and run with `backup` or `restore`

```bash
#!/bin/bash
# Disaster Recovery Script for OpenStack (Duplicity-based)
# Usage ./openstack-dr.sh <backup|restore>
# ---------------------------------------
# Config Section
# ---------------------------------------
# Swift container for backups
BACKUP_TARGET="swift://backups-container"

# Directories to backup
CONFIG_DIRS="/etc/keystone /etc/nova /etc/neutron /etc/cinder /etc/glance"

# Database backup location (temp)
DB_DUMP="/var/backups/openstack-db.sql"

# OpenStack DB credentials (Change to meet environment)
DB_USER="root"
DB_PASS="<Password>"

# --------------------------------------
# Functions
# --------------------------------------

backup() {
	echo "[INFO] Starting OpenStack Backup..."
	
	# 1. Dump MariaDB
	echo "[INFO] Dumping OpenStack DB..."
	mysqldump -u$DB_USER -p$DB_PASS --all-databases > $DB_DUMP
	
	# 2. Backup configs and DB dump to Switft
	echo "[INFO] Running duplicity backup..."
	duplicity $CONFIG_DIRS file://$BACKUP_TARGET/configs
	duplicity $DB_DUMP file://$BACKUP_TARGET/databases
	
	echo "[INFO] Backup Completed!"
}

restore() {
  echo "[INFO] Starting OpenStack Restore..."

  # 1. Restore configs
  echo "[INFO] Restoring configs..."
  duplicity restore file://$BACKUP_TARGET/configs /etc

  # 2. Restore DB
  echo "[INFO] Restoring databases..."
  duplicity restore file://$BACKUP_TARGET/databases /tmp/dbrestore.sql
  mysql -u$DB_USER -p$DB_PASS < /tmp/dbrestore.sql

  # 3. Restart OpenStack services
  echo "[INFO] Restarting OpenStack services..."
  systemctl restart mariadb
  systemctl restart keystone
  systemctl restart glance-api
  systemctl restart nova-api
  systemctl restart neutron-server
  systemctl restart cinder-scheduler

  echo "[INFO] Restore Completed!"
}

# ------------------------------
# Main
# ------------------------------
case "$1" in
  backup)
    backup
    ;;
  restore)
    restore
    ;;
  *)
    echo "Usage: $0 {backup|restore}"
    exit 1
esac

```