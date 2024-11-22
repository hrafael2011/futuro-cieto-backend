from django.core.exceptions import ValidationError
from PIL import Image
import os

def processImage(image_path, size, dir):
                # Abrir la imagen usando Pillow después de haberla guardado
                img = Image.open(image_path)

                # Establecer el tamaño deseado
                max_size = size
                img.thumbnail(max_size)  # Redimensionar manteniendo la proporción

                # Cambiar el formato de la imagen a webp
                webp_image_path = os.path.splitext(image_path)[0] + '.webp'
                img.save(webp_image_path, format='WEBP')

                # Generar la nueva ruta para la imagen convertida
                new_image_path = os.path.join(dir, os.path.basename(webp_image_path))

                # Retornar la nueva ruta de la imagen en formato webp
                return new_image_path


def validateVideo(file):
        
        #  Tamaño maximo en bytes (20 MB en este ejemplo)

        max_size = 20 * 1024 * 1024
        if file.size > max_size:
                raise ValidationError("El Tamaño del archivo no debe exceder los 20 MB")
        
        # Validar Formato
        valid_formats = ['video/mp4', 'video/webm']
        if file.file.content_type not in valid_formats:
                raise ValidationError("Solo se permiten archivos MP4 y Webm.")

