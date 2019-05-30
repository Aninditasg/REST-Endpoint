# REST-Endpoint
A Rest Endpoint to calculate the total of a large range of numbers.

This webapp gets  a large range of numbers from backend service and displays it on at endpoint http://127.0.0.1:8000/total.

  
     
The Django REST MVT framework has been used to ensure scalability and reliability of the function.
The range of number to add is the model and the view calculates the total and displays it.
The output is 
{"total": 50000015000001}

The test coverage is 94% and there a cache to store the server output to increase performance.
Following is the folder structure for the python files
total
|
|
---total
|     |
|     wsgi.py
|      settings.py
|      urls.py
|____total_calculator
     models.py
     views.py
     test.py
     apps.py
     admin.py
     
     If this app needs to run as an https:// end point the following lines nees to be added to the settings.py file
         SESSION_COOKIE_SECURE = True
         CSRF_COOKIE_SECURE = True
