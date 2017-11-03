# DjangoTDD

Proyecto que utiliza la metodología TDD para desarrollar una aplicación con 
Django

## Instrucciones:

**1. Crear y activar un entorno virtual:**
```
virtualenv --python=/usr/bin/python3.5 venv
source venv/bin/activate
```

**2. Instalar las dependencias:**
```
pip3 install "django<1.12" "selenium<4"
pip install lettuce
```

## Correr proyecto:
```
python manage.py runserver 0.0.0.0:8000
``` 

## Ejecutar pruebas unitarias:
```
python manage.py test
```

## Ejecutar pruebas funcionales:
```
# Ejecución normal:
lettuce bdd/tests/

# Con stagin server_
STAGING_SERVER=superlists-staging.ottg.eu lettuce bdd/tests/
```
