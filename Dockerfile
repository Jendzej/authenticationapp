FROM python:3.10.5-slim
WORKDIR /mainapp
COPY . .
RUN python -m pip install pipenv
RUN pipenv install
RUN pipenv run python mainapp/manage.py migrate
EXPOSE 8000
CMD ["pipenv", "run", "python", "mainapp/manage.py", "runserver"]