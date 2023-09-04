from PIL import Image, ImageFilter
import os

directorio_entrada = 'resources/up'
directorio_salida = 'resources/out'

#scale image variable
tamaño_objetivo = (970, 1372)  

extensiones_permitidas = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

# Create os directory
if not os.path.exists(directorio_salida):
    os.makedirs(directorio_salida)

# Iterator
for archivo in os.listdir(directorio_entrada):
    if archivo.lower().endswith(extensiones_permitidas):
        ruta_entrada = os.path.join(directorio_entrada, archivo)
        ruta_salida = os.path.join(directorio_salida, archivo)
        
        imagen = Image.open(ruta_entrada)
        
        # Risize
        imagen_escalada = imagen.resize(tamaño_objetivo)
        
        # Appy the filter to up image sharpness
        imagen_nitida = imagen_escalada.filter(ImageFilter.DETAIL)
        
        # Save result
        imagen_nitida.save(ruta_salida, dpi=(300,300))

print('Save image! Done!')
