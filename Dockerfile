# Usa una imagen base de Python
FROM python:3.13.3-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos y el código fuente al contenedor
COPY requirements.txt requirements.txt
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app
# Expone el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para correr la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]