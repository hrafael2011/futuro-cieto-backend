#!/bin/bash

# Mover a la carpeta raíz de tu proyecto
cd /home/site/wwwroot

# Aplicar migraciones de la base de datos
echo "Ejecutando migraciones..."
python manage.py migrate --noinput

# Recolectar archivos estáticos para producción
echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

# Iniciar el servidor con Gunicorn
echo "Iniciando Gunicorn..."
gunicorn tu_proyecto.wsgi:application --bind=0.0.0.0 --workers=3 --timeout 600
