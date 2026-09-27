release: python manage.py migrate
web: python manage.py migrate && gunicorn cafe_menu.wsgi --log-file -
