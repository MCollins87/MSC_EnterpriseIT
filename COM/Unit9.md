[Back to Module](./README.md)

# Unit 9 Formative Activity

## Brief
Migrate a database from a local machine to OpenStack using MySQL and Percona XtraBackup.

## Deliverable
A step by step guide on how to migrate an SQL database on a local Machine to an OpenStack Environment. 

### 1. Prerequisites
This activity took advantage of the *Hot Back-up* feature of Percona XtraBackup (Percona LLC, 2025). The advantage of Hot Back-ups is that incremental back-ups can be performed while the database is live and the MySQL services are running. This allows for users to continue using the original database while the new location is prepared.

Within a production environment, I would most likely follow the following steps:


1. Perform full back-up with: 
	- `sudo xtrabackup --backup --target-dir=/tmp/base_backup --datadir=/var/lib/mysql`
	- `sudo xtrabackup --prepare --target-dir=/tmp/base_backup`
2. Prepare the remote / new environment (Unit 4).
3. Transfer full back-up to new location.
	- ``sudo tar -czf base_backup.tar.gz base_backup`
	- `sudo chown $(whoami):$(whoami) base_backup.tar.gz`
	- `scp -i <SSH_KEY> /tmp/base_backup.tar.gz <NAME>@<LOCATION>:/tmp/`
4. Restore full back-up in new location.
	- `cd /tmp`
	- `tar -xzf base_backup.tar.gz`
	- `sudo xtrabackup --copy-back --target-dir=/tmp/base_backup --datadir=/var/lib/mysql`
	- `sudo chown -R mysql:mysql /var/lib/mysql`
	- `sudo systemctl start mysql`
5. Test migration
	- `sudo mysql -u root -p -e "SHOW DATABASES;"`
	- `sudo mysql -u root -p -e "SELECT * FROM <DATABASE_NAME>;"`
6. Place original database into Lock state.
	- `mysql -u root -p`
	- `FLUSH TABLES WITH READ LOCK;`
	- `SHOW MASTER STATUS;`
	- Do not exit this session yet - keep tables locked!
7. Perform incremental back-up.
	- `sudo xtrabackup --backup --target-dir=/tmp/inc_backup --incremental-basedir=/tmp/base_backup --datadir=/var/lib/mysql`
	- `sudo xtrabackup --prepare --apply-log-only --target-dir=/tmp/base_backup`
	- `sudo xtrabackup --prepare --target-dir=/tmp/base_backup --incremental-dir=/tmp/inc_backup
8. Transfer to new location.
	- `cd /tmp`
	- `sudo tar -czf inc_backup.tar.gz base_backup`
	- `sudo chown $(whoami):$(whoami) inc_backup.tar.gz`
	- `scp -i <SSH_KEY> inc_backup.tar.gz <USER>@<LOCATION>:/tmp/
9. Restore incremental back-up, adding the changes since full back-up. 
	- `sudo systemctl stop mysql`
	- `cd /tmp`
	- `tar -xzf inc_backup.tar.gz`
	- `sudo xtrabackup --copy-back --target-dir=/tmp/base_backup --datadir=/var/lib/mysql
	- `sudo chown -R mysql:mysql /var/lib/mysql`
	- `sudo systemctl start mysql`
10. Point any services relying on database to new location and restart MySQL services. 

The advantage to running a migration this way is that it results in minimal downtime. By performing the Full back-up while the Database is still running, allows for no downtime while the longest task takes place. In theory, within a production environment, this database could be many GB or even TB resulting in allot of time to perform back-up, transfer and restore in new location.

Once the new location is fully prepared and tested, the existing production database can be stopped to prevent any data loss, an incremental back-up can be performed to capture any changes and then this much smaller dataset can be transferred and restored before pointing any services that use the database to the new location.

Additionally, if the preparation of the new environment, including the transfer and restore takes a long time, and the database has many transactions, additional hot incremental backups can be performed and restored during operational with the final back-up and restore and configuration occurring out of hours, further mitigating risk of data loss or service downtime.
Unit 10](./Unit10.md)