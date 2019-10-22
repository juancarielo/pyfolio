# In root folder
```sh
$ python -m venv venv
```

# Activate the virtualenv
```sh
$ source venv/bin/activate # Linux or macOS
$ source venv/Scripts/activate # Windows
```

# Migrations
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

# If you're using Linux run this command:
```sh
$ source init.sh
```