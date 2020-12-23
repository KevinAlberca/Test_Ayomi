# AYOMI

Test technique realise pour le processus de recrutement AYOMI

Initialisation du projet

```bash
docker-compose build
docker-compose up -d db
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
docker-compose up web
```