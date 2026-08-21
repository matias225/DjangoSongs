# DjangoSong, una app de django para guardar una lista de canciones

## 1. Instalar las dependencias

`pip install -r requirements.txt`

## 2. Renombrar archivo .env_template a .env y completar datos

## 3. Crear la base de datos en MySQL

Si no existe la migración, o se hace algún cambio al modelo usar:

`python manage.py makemigrations`

## 4. Hacer las migraciones

`python manage.py migrate`

## 5. Crear un superusuario

`python manage.py createsuperuser`

Se puede acceder al panel de admin desde /admin

## 6. Comprobar que todo funciona

`python manage.py check`

## 7. Correr la aplicacion

`python manage.py runserver`
