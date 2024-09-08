# Gestor Documental

## Sobre el proyecto

Proyecto de código abierto desarrollado en linux con el propósito de crear un sistema de escritorio para gestionar la conservación y consulta del legado documental aplicando las tablas de retención que apliquen.

```mermaid
document_manager/
├── src/
│ ├── main.py
│ ├── config.py
│ ├── gui/
│ │ ├── __init__.py
│ │ ├── gui_main.py
│ └── database/
│ ├── **init**.py
│ ├── conexion.py
│ ├── model/
│ │ ├── __init__.py
│ │ ├── connection.py
├── assets/
│ ├── images/
│ │ └── logo.png
│ └── styles/
│ └── estilos.css
├── .gitignore
├── README.md
└── requirements.txt
```

### 1. Creación de entorno virtual

Ejecuta en la terminal el comando:

```bash
python -m venv ~/proyectos/document_manager/env
```

Activación entorno virtual, recuerda modificar tu ruta `~/proyectos/` según situes el proyecto:

```bash
source ~/proyectos/document_manager/env/bin/activate
```

Desactivar entorno virtual:

```bash
deactivate
```

### 2. Instalar paquete pylint:

Ejecuta en la terminal el comando:

```bash
pip install pylint
```

### 2.1 Instalar paquete autopep8:

Ejecuta en la terminal el comando:

```bash
pip install autopep8
```

### 2.2 Instalar paquete pil:

Ejecuta en la terminal el comando:

```bash
pip install pillow
```

### 2.3 Instalar paquete dotenv y decuple:

Ejecuta en la terminal el comando:

```bash
pip install python-dotenv python-decouple
```

### 2.4 Instalar paquete psycopg2:

Ejecuta en la terminal el comando:

```bash
pip install psycopg2
```
