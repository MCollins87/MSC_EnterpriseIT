[Back to Module](./README.md)

# Unit 9 Formative Activity

## Brief
Migrate a database from a local machine to OpenStack using MySQL and Percona XtraBackup.

## Deliverable
A step by step guide on how to migrate an SQL database on a local Machine to an OpenStack Environment. 

### 1. Prerequisites
- Local machine:
    - MySQL (Source DB)
    - Percona XtraBackup installed
- OpenStack Environment:
    - A running VM (Ubuntu) with MySQL installes
    - SSH access between local and OpenStack VM
- Ensure both source and target MySQL versions are compatible.

### 2. Backup with Percona XtraBackup 

On Local machine:

1. Install Percona XstraBackup if not already installed:

``` bash
sudo apt-get install percona-xtrabackup-80
```

2. Run backup of database:

``` bash
innobackupex --user=<mysql_user> --password=<mysql_password> /tmp/db_backup
```

3. Prepare the backup (apply redo logs to maintain consistancy)

``` bash
innobackupex --apply-log /tmp/db_backup/<timestamped_dir>
```

### 3. Transfer Backup to OpenStack

1. Compress the backup directory:

``` bash
tar -czvf db_backup.tar.gz -C /tmp/db_backup/<timestamped_dir> .
```

2. Copy to OpenStack

```bash
scp db_backup.tar.gz ubuntu@<openstack_vm_ip>:/tmp/
```

### 4. Restore on OpenStack

On OpenStack VM:

1. Install Percona XtraBackup on the VM (as before)
2. Stop MySQL:
``` bash
sudo systemctl stop mysql
```

3. Extract the backup
```bash
tar -xzvf /tmp/db_backup.tar.gz -C /tmp/dv_restore/
```

4. Move backup files to MySQL data dir
``` bash
sudo rsync -avrP /tmp/db_restore/ /var/lib/mysql/
```

5. Set ownership:
``` bash
sudo chown -R mysql:mysql /var/liv/mysql
```

6. Start MySQL
```bash
sudo systemctl start mysql
```

### 5. Verify Migration

1. log into mySQL on OpenStack VM
``` bash
mysql -u root -p
```

2. Check that all databases, tables and users exist
3. Run integrity checks as necessary

