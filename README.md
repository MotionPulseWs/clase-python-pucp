# clase-python-pucp

# miRedSocial

Proyecto de red social desarrollado con Django y Django REST Framework.

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd miRedSocial
```

### 2. Crear entorno virtual

**En Windows:**
```bash
python -m venv venv
```

**En Linux/Mac:**
```bash
python3 -m venv venv
```

### 3. Activar el entorno virtual

**En Windows:**
```bash
venv\Scripts\activate
```

**En Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Actualizar pip (recomendado)

```bash
python -m pip install --upgrade pip
```

### 5. Instalar dependencias

Si existe `requirements.txt`:
```bash
pip install -r requirements.txt
```

Si no existe, instalar las dependencias manualmente:
```bash
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install pillow
pip install django-cors-headers
pip install channels
pip install channels-redis
```

### 6. Configurar la base de datos

Aplicar las migraciones:
```bash
python manage.py migrate
```

### 7. Crear un superusuario (opcional)

Para acceder al panel de administración:
```bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla para crear tu usuario administrador.

### 8. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://127.0.0.1:8000/`

## Acceso a la Aplicación

- **Aplicación principal:** http://127.0.0.1:8000/
- **Panel de administración:** http://127.0.0.1:8000/admin/

## Estructura del Proyecto

```
miRedSocial/
│
├── accounts/           # App de autenticación y usuarios
├── chat/              # App de mensajería
├── posts/             # App de publicaciones
├── templates/         # Plantillas HTML
├── miRedSocial/       # Configuración principal del proyecto
├── db.sqlite3         # Base de datos SQLite
├── manage.py          # Script de gestión de Django
└── venv/              # Entorno virtual (no se sube a Git)
```

## Comandos Útiles

### Crear migraciones después de cambios en modelos
```bash
python manage.py makemigrations
```

### Aplicar migraciones
```bash
python manage.py migrate
```

### Crear un nuevo superusuario
```bash
python manage.py createsuperuser
```

### Recolectar archivos estáticos (producción)
```bash
python manage.py collectstatic
```

### Generar archivo requirements.txt
```bash
pip freeze > requirements.txt
```

## Desactivar el Entorno Virtual

Cuando termines de trabajar:
```bash
deactivate
```

## Solución de Problemas Comunes

### Error: ModuleNotFoundError

Si aparece un error de módulo no encontrado, instálalo con:
```bash
pip install <nombre_del_modulo>
```

### Error: No such file or directory 'requirements.txt'

Si no existe el archivo, genera uno nuevo:
```bash
pip freeze > requirements.txt
```

### El servidor no inicia

1. Verifica que el entorno virtual esté activado
2. Asegúrate de estar en la carpeta raíz del proyecto
3. Verifica que todas las dependencias estén instaladas

## Tecnologías Utilizadas

- **Django** - Framework web de Python
- **Django REST Framework** - API REST
- **Django REST Framework SimpleJWT** - Autenticación JWT
- **Pillow** - Procesamiento de imágenes
- **Channels** - WebSockets para chat en tiempo real
- **SQLite** - Base de datos (desarrollo)

## Contribuir

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## Licencia

Este proyecto es parte de un curso educativo de PUCP.

## Contacto

Para preguntas o sugerencias sobre el proyecto, contacta al equipo de desarrollo.