# Backend Restaurante - La Picada de la doble F

API REST desarrollada en Django para la gestión del menú, categorías y toma de pedidos del restaurante "La Picada de la doble F". Permite administrar el catálogo de productos y calcular automáticamente los subtotales y el monto total de cada pedido en tiempo real.

## Tecnologías Utilizadas
 Lenguaje: Python 3
 Framework Backend: Django 6.1.2
 API REST: Django REST Framework 3.18.3
 Seguridad / CORS: django-cors-headers 4.9.0
 Base de Datos: SQLite3

## Modelos Implementados
1. `Categoria`: Clasificación de los platos y bebestibles (ej. Sándwiches, Bebidas).
2. `Producto`: Ítems disponibles en la carta, asociados a una categoría (`ForeignKey`) y validados para impedir precios negativos (`MinValueValidator(0)`).
3. `Pedido`: Registro de la orden del cliente con fecha de creación, estado y cálculo automático del `total`.
4. `DetallePedido`: Relación intermedia entre `Pedido` y `Producto` con validación de cantidad mínima (`MinValueValidator(1)`) y cálculo automático de `subtotal` al guardar.



## Documentación de Endpoints

Todas las rutas base cuentan con soporte para operaciones CRUD (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`):

Recurso  ruta base  Métodos HTTP  Descripción 

Categorías `/api/categorias/`  `GET, POST, PUT, DELETE`  Listar, crear, editar o eliminar categorías. 
Productos `/api/productos/`  `GET, POST, PUT, DELETE`  Administrar los platos y precios del menú. 
Pedidos `/api/pedidos/`  `GET, POST, PUT, DELETE`  Crear y consultar órdenes de compra. 
Detalles `/api/detalles/`  `GET, POST, PUT, DELETE`  Agregar productos a un pedido y recalcular totales. 

### Ejemplo de Solicitud (`POST /api/productos/`)
Body (JSON):
```json
{
    "nombre": "Chacarero",
    "precio": 6500,
    "categoria": 1
}


### Instrucciones de instalación y ejecución

*Todos los comandos deben ejecutarse en la terminal de Visual Studio Code o en el CMD*

1. Descargar el Proyecto:
Clona este repositorio en tu computador:
git clone https://github.com/PipoeZz/backend_restaurante.git

2. Entrar en la carpeta:
cd backend_restaurante

3. Crear el entorno virtual:
Crea un espacio aislado para instalar las herramientas:
python -m venv venv

4. Activar el entorno virtual:
venv\Scripts\activate

5. Instalar las dependencias:
Instala Django y las demás herramientas necesarias:
pip install -r requirements.txt

6. Preparar la base de datos:
Ejecuta estos dos comandos para crear las tablas:
python manage.py makemigrations
python manage.py migrate

7. Cargar los datos iniciales del menú
Puebla la base de datos con los productos, precios y categorías
python manage.py loaddata datos_menu.json

8. Ejecutar el servidor:
Inicia la aplicación:
python manage.py runserver

9. Ver el proyecto:
Abre un navegador y visita: http://127.0.0.1:8000/
