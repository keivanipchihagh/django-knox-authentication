# django-knox-authentication
Knox provides easy to use authentication for [Django REST Framework](http://www.django-rest-framework.org/) The aim is to allow for common patterns in applications that are REST based, with little extra effort; and to ensure that connections remain secure. Read more [here](https://james1345.github.io/django-rest-knox/).

# Installation
1. Setup a virtual environment and install the required packages (on Ubuntu):
  ```bash
  $ python3 -m venv venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt
  ```
2. Create the initial database and start the server:
  ```bash
  $ cd ./django_knox_auth
  $ python3 manage.py migrate
  $ python3 manage.py runserver
  ```
3. Import [django-knox-authentication.postman_collection.json](https://github.com/keivanipchihagh/django-knox-authentication/blob/main/django-knox-authentication.postman_collection.json) to postman and run the requests.


Enjoy!
