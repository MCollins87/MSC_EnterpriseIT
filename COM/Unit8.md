[Back to Module](./README.md)

# Unit 8 Formative Activity

# Implementation

Due to a number of issues and repeated attempts, I have been unable to get OpenStack to install on my test set-up (Oracle Cloud, Ubuntu 24.04). Therefore I have changed the brief to implement a DR plan for Oracle Cloud Infrastructure. 

## Definitions and overview

### Objectives
- **RPO (Recovery Point Objective):** Max data loss acceptable. 15 minutes
- **RTO (Recovery Time Objective):** Max downtime acceptable. 1 hour
- Ensure business continuity for critical services on OCI

### Infrastructure Overview
For a proof of concept (PoC) set-up, the following set-up is used:

| Component       | Description                                     |
| --------------- | ----------------------------------------------- |
| Web Server      | Nginx hosting a simple web page                 |
| Database        | MySQL database with sample data                 |
| Back-up storage | OCI Object Storage (local storage used for PoC) |
### Strategy
| Component | Backup Type        | Tool                      | Frequency       | Storage Location           |
| --------- | ------------------ | ------------------------- | --------------- | -------------------------- |
| Web files | Full / Incremental | Duplicity                 | Hourly / Weekly | OCI Object Storage / Local |
| Database  | Logical dump       | mysqldump + Duplicity<br> | Hourly          | OCI Object Storage / Local |
- Backups should be encrypted using GPG
- Critical backups should be replicated to a secondary OCI region (not demonstrated in this PoC).

## Implement Environment

Simulate a cloud VM with simple web app + database.

**Install Nginx**
```bash 
sudo apt update
sudo apt install nginx -y
sudo systemctl enable nginx
sudo systemctl start nginx
echo "<h1>DR PoC Web Page</h1>" | sudo tee /var/www/html/index.html
```

**Install MySQL**
```bash
sudo apt install mysql-server -y
sudo systemctl enable mysql
sudo systemctl start mysql
sudo mysql
```

SQL:
```sql
CREATE DATABASE poc_db;
USE poc_db;
CREATE TABLE test_table (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO test_table (name) VALUES
  ('Backup test 1'),
  ('Backup test 2'),
  ('Backup test 3');
```

**Install Backup Tool (Duplicity)**
```bash
sudo apt install duplicity -y
```

Optional extra for OCI, but using local backup for PoC:
```bash
sudo apt install python3-pip -y
pip3 install --user oci boto3
```
*Additional work is needed for* `pip` *to work due to* `PEP 668` *being used on Ubuntu 24.04*

### Create Backup scripts

**Web Files Backup**
```bash
# backup_web.sh
#!/bin/bash
duplicity full /var/www/html file:///home/ubuntu/backups/web
```

**Database Backup**
```bash
# backup_db.sh
#!/bin/bash
mysqldump -u root -p'YOUR_ROOT_PASSWORD' poc_db > /home/ubuntu/backups/db/poc_db.sql
duplicity full /home/ubuntu/backups/db file:///home/ubuntu/backups/db_backup
```

### Perform initial backups
```bash
./backup_web.sh
./backup_db.sh
```
Simple GPG passphrase: `123`

Verify:
```bash
ls ~/backups/web
ls ~/backups/db_backup
```

### Simulate Failure
**Web Server Failure**
```bash
sudo systemctl stop nginx
sudo rm -rf /var/www/html
```

**Database Failure**
```bash
sudo systemctl stop mysql
sudo rm -rf /var/lib/mysql/poc_db
```

### Restore
**Web service**
```bash
sudo duplicity restore file:///home/ubuntu/backups/web /var/www/html
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html
sudo systemctl start nginx
curl http://localhost  # Should show "DR PoC Web Page"
```

**Database**
1. Start MySQL
```bash
sudo systemctl start mysql
```
2. Restore
```bash
sudo duplicity restore file:///home/ubuntu/backups/db_backup /home/ubuntu/backups/db_restore
sudo mysql -e "DROP DATABASE IF EXISTS poc_db; CREATE DATABASE poc_db;"
sudo mysql poc_db < /home/ubuntu/backups/db_restore/poc_db.sql
```
3. Verify
```bash
ubuntu@TestStack:~$ sudo mysql -e "USE poc_db; SHOW TABLES;"
+------------------+
| Tables_in_poc_db |
+------------------+
| test_table       |
+------------------+
ubuntu@TestStack:~$ sudo mysql -e "SELECT * FROM poc_db.test_table;"
+----+---------------+---------------------+
| id | name          | created_at          |
+----+---------------+---------------------+
|  1 | Backup test 1 | 2025-10-15 18:55:09 |
|  2 | Backup test 2 | 2025-10-15 18:55:09 |
|  3 | Backup test 3 | 2025-10-15 18:55:09 |
+----+---------------+---------------------+
ubuntu@TestStack:~$ 
```
### Automate backup
Add the following lines to `crontab`
```bash
crontab -e
# Run hourly incremental web backup
0 * * * * /home/ubuntu/backup_web.sh >> /home/ubuntu/backups/web/backup.log 2>&1

# Run hourly incremental DB backup
5 * * * * /home/ubuntu/backup_db.sh >> /home/ubuntu/backups/db_backup/backup.log 2>&1

# Run weekly full web backup (Sunday at 2 AM)
0 2 * * 0 duplicity full /var/www/html file:///home/ubuntu/backups/web >> /home/ubuntu/backups/web/backup.log 2>&1

# Run weekly full DB backup (Sunday at 2:15 AM)
15 2 * * 0 mysqldump -u root poc_db > /home/ubuntu/backups/db/poc_db.sql && duplicity full /home/ubuntu/backups/db file:///home/ubuntu/backups/db_backup >> /home/ubuntu/backups/db_backup/backup.log 2>&1
```

# Discussion
We have demonstrated the design and implementation for a Disaster Recovery plan for a cloud-based infrastructure, hosted on Oracle Cloud Infrastructure (OCI). The goal was to ensure data resiliance and service continutiy in the event of a system failure through a combination of open source backup tools, automation, and simulated recovery operations.

### Infrastructure Setup

A virtual machine running Ubuntu 24.04 LTS was deployed on Oracle Cloud. The following services were configured to represent a typical web-based application stack:
- **Nginx** - Serviing static web content.
- **MySQL** - Storing application data in the `poc_db` database.
- **Duplicity** - performing encrypted and incrimental backups of both file and database data.
- **Cron** - automating recuring backups.

This setup mirrors a minimal production environment whil providing a controlled environment to simulate failures and test recovery procedures.

### Disaster Recovery Design

The DR plan focused on three main objectives:
1. **Data Protection** – regularly back up critical data (web content and MySQL database).
2. **Automation** – schedule backups using cron jobs to minimize human intervention.
3. **Rapid Recovery** – test restoration procedures to validate data integrity and minimize downtime.

### Backup Strategy

Two logical backups were created:
- Web content backup – `/var/www/html`
- Database backup – `mysqldump` output of `poc_db`

These were stored locally under `/home/ubuntu/backups/`, with Duplicity maintaining incremental versions to optimize space and performance.

### Tools Used

| Tool | Purpose |
| --- | --- |
| **Oracle Cloud Infrastructure (OCI)** | Host Cloud VM environment |
| **Ubuntu 24.04 LTS | Operating system for the DR Stack |
| **Nginx** | Web server for hosting content |
| **MySQL** | Database engine for application data |
| **Duplicity** | Open-source encrypted, incremental backup tool |
| **Cron** | Scheduler for automated backups |
| **mysqldump** | Logical database backup utility |

### Reflection on the DR Process

The proof-of-concept successfully demonstrated that:
- Automated, incremental backups can protect both web and database data effectively.
- Recovery from total data los was achievable using Duplicity and MySQL restore commands.
- Encrypted local backups provided data security even before integration with offsite storage. 

However, a few key lessons emerged:
- **Backup validation is critical.** Early tests produced empty dumps, emphisizing the need for automated dump verification after each packup.
- **Authentication configuration matters.** Ubuntu's `auth_socket` for MySQL root initially blocked scripted backups until the process was modified to use `sudo`.
- **Offsite storage should be added.** For real-world DR, backups should be replicated to OCI Object Storage or another remote location to survive site failure.

Overall, the strategy was effective, efficient, and fully recoverable for a single-node cloud instance. 

### Future Improvements
- Integrate **OCI Object Storage** as the Duplicity backend (`oci://bucket@namespace`) for offsite redundancy.
- Add **backup verification scripts** that test restore integrity at least weekly.
- Use **systemd timers** or **Ansible playbooks** for more flexible auotomation accross multiple instances.
- Add additional `crontab` entries to remove old back-ups to save space

## Conclusion 
This project demonstrated a complete, functional Disaster Recovery workflow on Oracle Cloud using open-source tools.
The combination of Duplicity, mysqldump, and automated scheduling provided a lightweight yet reliable approach to data protection.
In a production environment, expanding this setup to include offsite replication and continuous integrity testing would provide enterprise-grade resilience at minimal cost.
The above outlines using Duplicity for backing up a web service and a MySQL database on an Oracle Cloud Infrastructure.  By creating backup script, these can be added to the `crontab` to automate back-ups inline with RPO's and RTO's. 
