# Backend Restaurante - La Picada de la doble F

Backend en Django para el sistema de gestión de restaurante

## Instrucciones de instalación y ejecución

*Todos los comandos deben ejecutarse en la terminal de Visual Studio Code o en el CMD*

1. **Descargar el Proyecto:**
Clona este repositorio en tu computador:
git clone https://github.com/PipoeZz/backend_restaurante.git

2. **Entrar en la carpeta:**
cd backend_restaurante

3. **Crear el entorno virtual:**
Crea un espacio aislado para instalar las herramientas:
python -m venv venv

4. **Activar el entorno virtual:**
venv\Scripts\activate

5. **Instalar las dependencias:**
Instala Django y las demás herramientas necesarias:
pip install -r requirements.txt

6. **Preparar la base de datos:**
Ejecuta estos dos comandos para crear las tablas:
python manage.py makemigrations
python manage.py migrate

7. **Ejecutar el servidor:**
Inicia la aplicación:
python manage.py runserver

8. **Ver el proyecto:**
Abre un navegador y visita: http://127.0.0.1:8000/