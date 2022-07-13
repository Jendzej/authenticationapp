FROM python:3.10.5-slim

WORKDIR /app

COPY . .

RUN python -m pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "mainapp/manage.py", "runserver", "0.0.0.0:8000"]
