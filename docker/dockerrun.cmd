rem  django should be run: python manage.py runserver 0.0.0.0:8000
docker run --rm -it --publish 127.0.0.1:8000:8000 --name django-allauth --volume "%cd%":/data django-allauth:1.0  bash