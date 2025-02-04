# Diario de Gratitud 📝

Una aplicación web desarrollada con Django que permite a los usuarios mantener un diario personal de gratitud, ayudándoles a enfocarse en los aspectos positivos de su vida diaria.

## Características principales 🌟

- **Gestión de entradas**
  - Crear, editar y eliminar entradas.
  - Registro del estado de ánimo.
  - Organización cronológica.

- **Interfaz intuitiva**
  - Diseño responsive con Bootstrap.
  - Navegación sencilla.
  - Experiencia de usuario fluida.

- **Seguridad**
  - Sistema de autenticación de usuarios.
  - Protección de datos personales.
  - Entradas privadas por usuario.

## Tecnologías utilizadas 🛠️

- Django 5.0
- Bootstrap 5
- MySQL
- HTMX 
- Python 3.10+

## Estructura del proyecto 💃

```
gratitude_journal/
├── apps/
│   ├── gratitude_journal/  # Aplicación principal
│   └── users/              # Gestión de usuarios
├── media/                  # Archivos subidos
├── static/                 # Archivos estáticos
├── staticfiles/            # Archivos estáticos recolectados
├── templates/              # Plantillas HTML
├── venv/                   # Entorno virtual
├── .env                    # Variables de entorno
├── .gitignore
├── manage.py
└── requirements.txt
```

## Instalación local 💻

Sigue estos pasos para instalar y ejecutar la aplicación en tu entorno local.

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/diario-gratitud.git

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar base de datos MySQL
# Crear base de datos y configurar settings.py con las credenciales

# Realizar migraciones
python manage.py migrate

# Iniciar servidor
python manage.py runserver
```

## Capturas de pantalla 📸

### Página de Inicio
![Home](screenshots/Home.png)

### Mis Entradas
![Entradas](screenshots/MisEntradas.png)

### Dashboard
![Dashboard](screenshots/Dashboard.png)