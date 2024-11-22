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