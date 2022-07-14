Django authorization app

- At the beginning, you should build database image:

    `docker compose up database`

- When database will be ready to accept connections, build django_app image:

  `docker compose up django_app`

- When both images will be up, run this command to build database:

  ` docker exec -it authenticationapp-django_app-1 /bin/sh -c "python mainapp/manage.py makemigrations"`
- and:

  `docker exec -it authenticationapp-django_app-1 /bin/sh -c "python mainapp/manage.py migrate"`

If you passed the steps correctly, app should work at this url : `http:127.0.0.1:8000/`\
To sign up new user enter : `http:127.0.0.1:8000/accounts/signup`
