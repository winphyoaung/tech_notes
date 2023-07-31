# Tech Notes App
## Environment Variables and value to be replaced with your data
### DJANGO_SECRET_KEY=SECRETKEY
### DJANGO_ALLOWED_HOST="HOST1 HOST2 HOST3"
### DJANGO_DEBUG=TRUE|FLASE
### CSRF_TRUSTED_ORIGINS="[http|https]://DOMAIN-NAME"
### ENGINE=django.db.backends.mysql
### DBNAME=DBNAME
### RPASSWORD=ROOTPASSWORD
### USER=USER
### PASSWORD=DBPASSWORD
### HOST=mydb
### PORT=3306
## Getting Started
```
git clone URL
cd tech_notes
```
## Create .env file
```
    cat <<"EOF" > ../.env
    DJANGO_SECRET_KEY=<SECRETKEY>
    DJANGO_ALLOWED_HOST=<HOST1 HOST2 HOST3>
    DJANGO_DEBUG=<TRUE|FLASE>
    CSRF_TRUSTED_ORIGINS="[http|https]://DOMAIN-NAME"
    ENGINE=django.db.backends.mysql
    DBNAME=<DBNAME>
    RPASSWORD=<ROOTPASSWORD>
    USER=<ROOT>
    PASSWORD=<DBPASSWORD>
    HOST=mydb
    PORT=3306
    EOF
```
## Docker-compose Build
```
docker-compose --env-file=../.env build
```    
## Docker-compose up
```
docker-compose --env-file=../.env up -d
```
## Docker-compose down
```
docker-compose down
```

