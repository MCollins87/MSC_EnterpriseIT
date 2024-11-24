# Implementation Notes

## Instalation
Application [iTop](https://www.combodo.com/itop-193) was used. Installed on Ububtu 24.04LST. 

- Install (extraction) location:
    - `/var/www/html/itop`
- MariaDB used. 
    - `CREATE USER 'mark'@localhost IDENTIFIED BY 'Password123'`
- Set permissins to iTop folder:
    - `sudo chmod -R 0777 /var/www/html/itop/`
- Run instalation wizard:
    - Point browser to:
        - `localhost/itop`
    - Connect to DB Server using 
        - `mark`
        - `Password123`
    - Create database 
        `cmdb`
    - 