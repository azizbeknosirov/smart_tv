release: python manage.py migrate && python manage.py ensure_admin
web: python manage.py migrate && python manage.py ensure_admin && gunicorn cafe_menu.wsgi --log-file -
