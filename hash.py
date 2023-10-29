import hashlib
import os
from PIL import Image

for foto in os.listdir("/home/ander/Escritorio/irudia"):
    ruta_completa = os.path.join("/home/ander/Escritorio/irudia", foto)
    if foto.endswith('.jpg'):
        try:
            with open(ruta_completa, 'rb') as archivo:
                contenido = archivo.read()

            hash_obj = hashlib.md5()
            hash_obj.update(contenido)
            hash_resultado = hash_obj.hexdigest()
            if hash_resultado == "e5ed313192776744b9b93b1320b5e268":
                print(f'Archivo JPG encontrado: {foto} ')
        except Exception as e:
            print(f'Error al abrir {foto}: {e}')

#"Al Fascismo no se le discute, se le destruye." Buenaventura Durruti
