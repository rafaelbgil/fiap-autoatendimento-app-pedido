CATALOGO_API_URL ?= http://127.0.0.1:8090
COBRANCA_API_URL ?= http://127.0.0.1:8091
DJANGO_KEY ?= xxxdsadsadasxx
RABBIT_SERVER ?= 192.168.0.110

export CATALOGO_API_URL COBRANCA_API_URL DJANGO_KEY RABBIT_SERVER
test:
	coverage run --source=./  ./manage.py test 
	coverage html
test-xml:
	coverage run --source=./  ./manage.py test
	coverage xml
run:
	python manage.py runserver 0.0.0.0:8000

run-prod:
	uwsgi --ini uwsgi.ini

update-db:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py makemigrations api
	python manage.py migrate

run-celery:
	celery -A autoatendimento worker -l INFO
