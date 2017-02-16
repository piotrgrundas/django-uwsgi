# Django uWSGI

Simple Django management command useful for deploying an uWSGI instance of your Django app.

1. Install

    ```shell
    $ pip install git+https://github.com/pkucmus/django-uwsgi.git
    ```
2. Modify your `settings`  
    ```python

    INSTALLED_APPS = [
        ...
        'django_uwsgi',
    ]

    UWSGI = {
        'module': '{your_project}.wsgi:application',
        'socket': '0.0.0.0:8081',
        'http': '0.0.0.0:8080',
        'env': 'DJANGO_SETTINGS_MODULE=test_project.settings',
        'max_requests': 4096,
    }

    ```
3. Use

    ```shell
    $ python manage.py uwsgi
    ```
