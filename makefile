mig:
	python manage.py makemigrations
	python manage.py migrate


run:
	python manage.py runserver


git:
	git push origin main

super:
	python manage.py createsuperuser