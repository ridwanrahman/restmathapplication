1. Install virtual environment (virtualenv venv)
2. Turn on virtual environment (source venv/bin/activate)
3. Run command pip install -r requirements.txt to install all the libraries
4. Run command python manage.py migrate 
5. Run command python manage.py createsuperuser
6. Run command python manage.py runserver to turn on server
7. Using postman or insomnia, hit localhost with GET request to get the view from api.views
8. hit url http://127.0.0.1:8000/equation with post request and body an equation to get the output in terminal