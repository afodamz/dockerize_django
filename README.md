
This is a dockerized django project using docker-compose
## Procedure to run code
1. install docker
2. install docker compose
3. Using this working directory,
    - docker-compose run django_proj django-admin startproject core .
4. To work with the django container, we bash into it using
    - docker exec -it django_test bash
    where django_test is container name
5. In this bash terminal, you can run any django command
6. To also work with the postgres container, we bash into it using password and username defined in docker-compose.yaml
    - docker exec -it pgdb_djangoTest psql -U postgres
    where pgdb_djangoTest is container name, 
    postgres is username