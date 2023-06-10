# progrlang-vote-app

# Project setup

Rename all .env.example to .env and provide your passwords before running the start app command. If you specify ci environment copy the .env files to a server space. MYSQL_ROOT_PASSWORD, MYSQL_DATABASE, MYSQL_USER and MYSQL_PASSWORD are not predefined and can be freely chosen by the user. SECRET_KEY should be genereted by Django.

## Generate Django Secret Key

https://djecrety.ir/

Generate self-signed certificates with mkcert for local environment and Let's Encrypt certificates for production environment.

Set up a local DNS like Dnsmasq (Mac OS) for local environment in order to direct traffic from test domain to localhost.

https://passingcuriosity.com/2013/dnsmasq-dev-osx/

# Build images:

## Build frontend and backend images for local environment:
Go to frontend and backend project folders.

```bash
docker build --target dev-stage -t alonimacaroni/vote-frontend:dev .
docker build --target dev-stage -t alonimacaroni/vote-backend:dev .
```

## Build frontend and backend images for production environment:

```bash
docker build --target prod-stage -t alonimacaroni/vote-frontend:prod .
docker build --target prod-stage -t alonimacaroni/vote-backend:prod .
```

# Use devops.sh script for app management:
Set LOC parameter equal to dev (default), ci or prod.

## Build all images at once:
For dev and prod:

```bash
LOC=dev ./devops.sh setup
```

## Start app correctly:

```bash
LOC=dev ./devops.sh start
```

## Shutdown app correctly:

```bash
LOC=dev ./devops.sh exit
```

## Wait for database connection. For ci:

```bash
LOC=ci ./devops.sh wait
```

## Apply migrations:

```bash
LOC=dev ./devops.sh migrate
```

## Run automated tests:

```bash
LOC=dev ./devops.sh test
```

## Reset and clean Docker environment:
```bash
LOC=dev ./devops.sh clean
```