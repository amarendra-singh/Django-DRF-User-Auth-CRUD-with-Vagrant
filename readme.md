# Django DRF API CRUD with Vagrant
A REST api written in Django for people with deadlines

This repository contains a Django project with the Django Rest Framework (DRF) that implements user authentication and CRUD (create, read, update, delete) operations. The project is configured to run with Vagrant to simplify the setup process.

Prerequisites
Before you can get started with the project, you'll need to have the following installed on your machine:

Vagrant
VirtualBox
Getting Started
To get started with the project, simply clone or download the repository to your local machine and navigate to the directory where the repository is located. Then, run the following command in your terminal or command prompt:

Copy code
vagrant up

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs

## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
* #### Dependencies
    1. Create and fire up your virtual environment:
        ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate
        ```
    2. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
    3. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/
    ```
