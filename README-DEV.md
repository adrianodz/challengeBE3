<b>First Commit</b>
Files:
- docker-compose.yml
- Dockerfile
- requirements.txt
- .dockerignore
- /ngix (Dockerfile, nginx.conf and /certs)

Comands:
- docker-compose build
- (only in the first time) docker-compose run --rm app django-admin startproject core
- docker-compose up
- docker exec -it django_container bash

Code formater:
- black => commands: "black . --diff --color" and "black ."