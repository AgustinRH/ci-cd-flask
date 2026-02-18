# ci-cd-flask

Proyecto de práctica para una aplicación **Flask** orientada a un flujo de **CI/CD**.

## Objetivo

Este repositorio está pensado para trabajar tres etapas:

- **Integración Continua (CI):** ejecutar tests automáticamente en cada push a `main`.
- **Entrega Continua (CD):** construir y publicar imagen Docker tras pasar los tests.
- **Despliegue Continuo:** desplegar la imagen en un entorno cloud (por ejemplo, AWS).

## Estructura del proyecto

```text
.
├── Dockerfile
├── README.md
├── requirements.txt
├── img/
├── src/
│   └── app.py
└── tests/
	└── test_app.py
```

## Requisitos

- Python 3.10+ (recomendado)
- pip
- Docker (opcional, para ejecución en contenedor)

## Ejecución en local

### 1) Crear y activar entorno virtual

**Windows (PowerShell):**

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3) Ejecutar la app

```bash
python src/app.py
```

La aplicación quedará disponible en:

- http://localhost:8000

### 4) Desactivar entorno virtual

```bash
deactivate
```

## Ejecutar tests

Desde la raíz del proyecto:

```bash
python -m unittest discover tests
```

## Uso con Docker

### Construir imagen

```bash
docker build -t ci-cd-flask .
```

### Ejecutar contenedor

```bash
docker run -p 8000:8000 ci-cd-flask
```

Abrir en navegador:

- http://localhost:8000

## Proceso de desarrollo realizado

### 1. Preparación del proyecto

Fork del repositorio original y clonación en local.

![Paso 1](img/1%20-%20hacer%20fork.png)
![Paso 2](img/2%20-%20clonar%20repositorio.png)

### 2. Implementación de tests unitarios

Se añadieron pruebas para:

- respuesta correcta de la ruta principal,
- contenido esperado,
- manejo de error 404.

![Paso 3](img/3%20-%20creamos%20test%20unitarios.png)

### 3. Configuración del workflow de CI

Ajuste del workflow de GitHub Actions para ejecutar integración continua.

![Paso 4](img/4%20-%20modificamos%20workflows.png)

### 4. Verificación de resultados

Validación de la ejecución correcta de los tests en GitHub Actions.

![Paso 5](img/5%20-%20test%20working.png)

