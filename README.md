##Introduction

A Simple URL Shortener, written in Python, supported by the Django Framework

##Database used

MySQL

##Dependencies

- Python 2.7 
- Django 1.6.1

##Deploying the App

 1. Install Django(1.6.1) through the command line (or pip)

   `sudo apt-get install python-django`
   
 2. Clone the directory into a working project, say MyProject

   `git clone http://github.com/devanshgoenka97/url-shortener`

 3. Install the MySQL client for python through pip

   `sh pip install mysql-client python-dev`

 4. In the `settings.py` file inside `MyProject/URLShortener/` change the `DATABASES` -> `ENGINE` to

   `django.db.backends.mysql`

 5. Create an appropriate database in MySQL and sync

   `python manage.py syncdb`

 6. Create a superuser

   `python manage.py createsuperuser`

 7. Run the Server
  
   `python manage.py runserver`

 8. Open your browser to `127.0.0.1:8000` to use the app

##For the official documentation for Django, Visit 

[Django documentation](https://docs.djangoproject.com/en/1.8/)

##Created by
----------
[Devansh Goenka](https://github.com/devanshgoenka97) 
