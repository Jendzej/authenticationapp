FROM python:3.10.5
COPY . .
WORKDIR /mainapp
RUN python -m pip install pipenv
RUN pipenv install
CMD pipenv shell
CMD pipenv run python manage.py migrate
CMD pipenv run python manage.py runserver 0.0.0.0:8000
EXPOSE 8000