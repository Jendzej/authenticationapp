FROM python:3.10.5
COPY . .
EXPOSE 8000
WORKDIR /mainapp
RUN python -m pip install pipenv
RUN pipenv install
RUN pipenv run python manage.py migrate
RUN pipenv run python manage.py runserver