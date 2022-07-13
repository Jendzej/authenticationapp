FROM python:3.10.5-slim
WORKDIR /mainapp
COPY . .
RUN python -m pip install -r requirements.txt
RUN python mainapp/manage.py migrate
RUN python mainapp/manage.py createsuperuserwithpassword --username admin --email admin@admin.com --password admin
EXPOSE 8000
CMD ["python", "mainapp/manage.py", "runserver", "0.0.0.0:8000"]
