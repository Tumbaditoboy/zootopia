# Imagen base 
FROM python:3.11.9

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# archivo de dependencias
COPY requirements.txt .

# Instalar las dependencias de forma aislada
RUN pip install --no-cache-dir -r requirements.txt

#  Copiar el resto del código del proyecto 
COPY . .

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]