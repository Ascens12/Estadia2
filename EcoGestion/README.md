# EcoGestion con Docker

Este proyecto incluye una configuración lista para levantar el entorno completo con Docker y Docker Compose. Ya no es necesario instalar Python, MySQL ni Redis de forma local: todo se ejecuta en contenedores.

## Requisitos previos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Primer inicio

1. Copia el archivo de variables de entorno si quieres personalizar los valores predeterminados (opcional).
2. Levanta los servicios:

   ```bash
   docker compose up --build
   ```

   El contenedor de la aplicación ejecutará automáticamente las migraciones antes de iniciar el servidor de desarrollo en `http://localhost:8000`.

3. Para detener los servicios usa `Ctrl+C` y luego:

   ```bash
   docker compose down
   ```

## Servicios incluidos

- **web**: Contenedor con la aplicación Django/Channels.
- **db**: Servidor MySQL 8 con almacenamiento persistente en `mysql_data`.
- **redis**: Servidor Redis usado por Channels para manejar websockets.

## Variables de entorno relevantes

Puedes definir un archivo `.env` (en el mismo directorio que `docker-compose.yml`) con valores personalizados. Los principales parámetros disponibles son:

| Variable | Descripción | Valor por defecto |
| --- | --- | --- |
| `DJANGO_ALLOWED_HOSTS` | Lista separada por comas de hosts permitidos | `localhost,127.0.0.1` |
| `MYSQL_DATABASE` | Nombre de la base de datos | `EcoGest` |
| `MYSQL_USER` | Usuario de la base de datos | `root` |
| `MYSQL_PASSWORD` | Contraseña del usuario | `example` |
| `MYSQL_HOST` | Host de MySQL | `db` |
| `MYSQL_PORT` | Puerto de MySQL | `3306` |
| `REDIS_HOST` | Host de Redis | `redis` |
| `REDIS_PORT` | Puerto de Redis | `6379` |

Si necesitas agregar otras credenciales (por ejemplo para correo electrónico), puedes usar el mismo archivo `.env` y leerlas desde `settings.py` como variables de entorno.

## Comandos útiles

- **Crear un superusuario**:

  ```bash
  docker compose run --rm web python manage.py createsuperuser
  ```

- **Ejecutar migraciones manualmente**:

  ```bash
  docker compose run --rm web python manage.py migrate
  ```

- **Aplicar colecta de archivos estáticos** (si lo requieres para producción):

  ```bash
  docker compose run --rm web python manage.py collectstatic --noinput
  ```

## Persistencia de archivos

Los volúmenes `media_data` y `backup_data` preservan los archivos subidos por los usuarios y los respaldos generados por `django-dbbackup`. Esto evita que se pierdan cuando los contenedores se regeneran.

## Desarrollo local

Mientras `docker compose up` está en ejecución puedes editar el código en tu máquina. Los cambios se reflejan automáticamente dentro del contenedor gracias al volumen que monta el proyecto en `/app`.

## Producción

La configuración incluida está pensada para desarrollo. Para desplegar en producción considera usar un servidor ASGI como Daphne o Uvicorn detrás de un proxy inverso (Nginx) y ajustar `DEBUG`, `ALLOWED_HOSTS`, certificados TLS, etc.
