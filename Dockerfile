#Imagen base con Python 3.11.9
FROM python:3.11.9

#Carpeta de trabajo dentro del contenedor para la aplicación zoo
WORKDIR /app

#Copia archivos desde al proyecto hacia la imagen que estoy construyendo

COPY . .

#Instalar las dependencias
RUN pip install -r requeriments.txt


CMD ["python", "app.py"]