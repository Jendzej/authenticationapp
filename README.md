Django authorization app

WITHOUT DOCKER:
Follow this steps to run app:
- In the beggining, you should install modules and create virtual environment with pipenv (if you don't have pipenv, run: pip install pipenv):

    'pipenv install'

- Secondly, run pipenv shell:

    'pipenv shell'

- Then, change directory to /mainapp and create table in sqlite3 database:

    'py manage.py migrate' or 'python manage.py migrate'

- Now, you can run server:

    'py manage.py runserver' or 'python manage.py runserver'


WITH DOCKER:
- run this command in mainapp directory to build docker image:

  'docker build . -t django_app'

- Then, run this command to start container:

  'docker-compose up'


If you passed the steps correctly, app should work at this url : 'http:127.0.0.1:8000/'\
To sign up new user enter : 'http:127.0.0.1:8000/accounts/signup'
