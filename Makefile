export CATALOGO_API_URL='http://127.0.0.1:8000'
test:
	coverage run --source=./  ./manage.py test 
	coverage html

run:
	python manage.py runserver 0.0.0.0:8000

update-db:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py makemigrations api
	python manage.py migrate
