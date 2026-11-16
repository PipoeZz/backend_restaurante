# Declaración de Uso de Inteligencia Artificial

En el desarrollo del backend para nuestro sistema del restaurante, utilizamos Gemini como consultor para resolver errores que nos arrojaba el código. ya que a su vez utilizamos Platzi. A continuación, se detalla el uso específico de esta herramienta:

## Participación estimada por archivo

Archivo  Uso estimado de IA  Descripción 

`models.py`  20%  Ayuda para corregir un bug en `save()` donde no se actualizaba el total del pedido en tiempo real (usando `pedido_fresco`). 
`views.py`  30%  Consultas sobre cómo armar los `ModelViewSet` para el CRUD y solución de errores de importación. 
`serializers.py`  20%  Revisión de sintaxis básica para pasar los modelos a JSON. 
`urls.py`  15%  Dudas puntuales sobre cómo conectar los routers de DRF para las rutas de la API (`/api/productos/`). 
`settings.py`  30%  Pasos para instalar y configurar `django-cors-headers` y dejar listas las variables para conectar React después. 
`admin.py`  30%  Guía para registrar las tablas (`Categoria`, `Producto`, `Pedido`, `DetallePedido`) y poder meter datos desde la web. 

## Preguntas de reflexión

1. ¿En qué aspectos del proyecto utilizaron inteligencia artificial?
Más que nada para resolver errores que salían en la consola y que nos frenaban el avance. Por ejemplo, nos fue útil para arreglar conflictos con Git y GitHub cuando cambiábamos de computador, configurar los permisos de CORS para React y solucionar un problema con la suma automática de los totales en los pedidos.

2. ¿Qué partes del código fueron desarrolladas principalmente por ustedes?
Toda la base del proyecto la armamos nosotros guiándonos por los cursos de Platzi y lo visto en clases: cómo se relacionan las tablas de la base de datos, los campos de cada modelo, el cálculo de los subtotales, la lógica general de las vistas y la creación de los datos de prueba.

3. ¿Qué errores o problemas encontraron en las respuestas generadas por IA?
A veces nos daba comandos asumiendo que estábamos parados en la carpeta correcta o con el entorno virtual prendido, así que nos saltaban errores como `not a git repository` o `No module named 'django'` hasta que nos dábamos cuenta de que había que entrar a la subcarpeta o activar el `venv` primero. También tuvimos que cambiar varios nombres de variables en los ejemplos que nos daba para que calzaran con nuestros modelos.

4. ¿Cómo verificaron que el código sugerido funcionaba correctamente?
Probando todo directo en el navegador. Levantábamos el servidor con `runserver`, entrábamos al `/admin/` para crear productos y categorías reales (como un churrasco y una bebida), y después revisábamos los endpoints en `/api/productos/` para asegurarnos de que devolvieran el JSON sin errores (`HTTP 200 OK`) y que los precios se sumaran bien en la base de datos.

5. ¿Qué conocimientos adquirieron durante el desarrollo?
Aprendimos a levantar una API REST desde cero con Django y Django REST Framework, a entender cómo trabajan juntos los modelos, serializadores y vistas, y a no perderse con los entornos virtuales de Python. También practicamos el manejo de ramas y commits en GitHub trabajando en equipo. Entendimos por qué es necesario configurar CORS antes de conectar el frontend.