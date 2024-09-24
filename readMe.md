# Django Template
1. python -m virtualenv myenv
2. myenv\Scripts\activate 
3. pip install django
4. pip install djangorestframework
5. python -m pip install django-cors-headers
6. pip install djangorestframework-simplejwt
7. Pip freeze >  requirements.txt
8. django-admin startproject myproj .    (the dot is part of the command)
9. django-admin startapp base	(create application)
10. py manage.py runserver  (run the server)
11. Ввести данные суперюзера
12. python manage.py makemigrations
13. python manage.py migrate  
14. python manage.py createsuperuser



## Уже сделано:
1. Register
2. Добавила модель студентов
3. Добавила колоннку с название IMG
4. Добавить через администратора картинку
5. Создали страницу HTML и в альтернативном браузере получилось их показать

## Нужно добавить:
1. Token. есть функция токен, надо только проверить
2. Login
3. Serializer