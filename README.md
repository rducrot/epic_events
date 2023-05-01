# Epic Events
[![Python](https://badgen.net/badge/Python/3.10/blue)](https://www.python.org/)
[![Django](https://badgen.net/badge/Django/4.1/blue)](https://www.djangoproject.com/)
[![Django Rest Framework](https://badgen.net/badge/DRF/3.14/blue)](https://www.django-rest-framework.org/)

## Présentation

L'API d'Epic Events est un CRM permettant de gérer les clients d'une entreprise de conseils et de gestion dans l'événementiel.

## Documentation API

La documentation des points de terminaison de l'API est disponible sur [Postman](https://documenter.getpostman.com/view/15224502/2s93eR5wNT).

## Installation

1. Installer les paquets suivants.

```bash
sudo apt-get install postgresql libpq-dev
```

2. Cloner le répertoire depuis Github, puis se placer dans le répertoire principal.

```shell
git clone https://github.com/rducrot/epic_events
cd its-api
```

3. Mettre en place l'environnement virtuel.

```shell
python3 -m venv venv
source venv/bin/activate
```

4. Installer les dépendances depuis l'environnement virtuel.

```shell
pip3 install -r requirements.txt
```

## Base de données

Lancer PostgreSQL avec l'utilisateur `postgres`.
```bash
sudo -u postgres psql
```

Créer la base de données `epic_events`.

```sql
CREATE DATABASE epic_events;
```

Créer l'utilisateur renseigné dans `epic_events/settings.py`, puis lui attribuer les droits sur la db `epic_events`.

```sql
CREATE USER epicadmin WITH ENCRYPTED PASSWORD 'D!j4c39H';
GRANT ALL PRIVILEGES ON DATABASE epic_events TO epicadmin;
```

Une base de données est disponible afin de tester l'application. La commande suivante permet d'importer les données dans la base :

```bash
sudo -u postgres psql epic_events < database.db
```

Les identifiants des utilisateurs sont disponibles dans la partie `authentication` de la documentation sur [Postman](https://documenter.getpostman.com/view/15224502/2s93eR5wNT).

Si vous souhaitez créer vous-même le super utilisateur avec la commande `python3 manage.py createsuperuser`, renseigner le champ `Team: Management`afin d'accéder à la console d'administration.
## Exécution

Lancer la commande depuis le répertoire de l'application :
```shell
python3 manage.py runserver
```
