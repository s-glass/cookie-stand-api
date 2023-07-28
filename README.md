# Lab - Class 34
## Project: cookie-stand-api

- Author: Sarah Glass for Python 401

- Collaborated with Anthony, Logan, Dan, Slava at a Remo table.

## Overview

- It’s time to show off your skills by bringing “Vanilla” Django and Django Rest Framework together in the same project.

- You’ll build out a Restful API as well as a user facing site.

- Along the way you’ll see how easy Django makes it to move to a remote database.

- The project will be an old favorite with a Python twist - a Cookie Stand management site.

- The CookieStand model must contain:

```python
    location = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(blank=True)
    hourly_sales = models.JSONField(default=list, null=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)

    def __str__(self):
        return self.location
```

**Feature Tasks and Requirements - Django**

- The API Quick Start is a built out skeleton project with lots of the tools we’ve been using in class. Check it out. If you like it, use it. But better yet, use it as an inspiration to build your own that’s a perfect fit.

- Modify your application paying close attention to the instructions in README.md found in root of repository.

- Create/rename .env using .env.sample as starting point.



## Links and Resources

* [This repo](https://github.com/codefellows/python-401-api-quickstart) for starter code / as a template
* Database hosted at [ElephantSQL](elephantsql.com)
* TA and peer help.

## Setup

- Gitignore includes venv.
- sample_env.txt includes env variables

## How to initialize/run your application

- python manage.py runserver
- docker compose up --build
- runs at `http://127.0.0.1:8000/cookie_stands/`

## Libraries / Requirements

asgiref==3.6.0
certifi==2022.12.7
charset-normalizer==3.0.1
Django==4.1.5
django-appconf==1.0.5
django-cors-headers==3.13.0
django-environ==0.9.0
djangorestframework==3.14.0
djangorestframework-simplejwt==5.2.2
fire==0.5.0
gunicorn==20.1.0
idna==3.4
PyJWT==2.6.0
pytz==2022.7.1
rcssmin==1.1.1
requests==2.28.2
rjsmin==1.2.1
six==1.16.0
sqlparse==0.4.3
termcolor==2.2.0
urllib3==1.26.14
whitenoise==6.3.0


## Tests

Built-in Django testing

- python manage.py test
