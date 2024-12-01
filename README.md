# Microservicio de Blacklist

El objetivo del microservicio de Blacklist es proporcionar una API robusta y segura para gestionar una lista negra de direcciones de correo electrónico. Este microservicio permite a las aplicaciones clientes agregar, consultar y eliminar direcciones de correo electrónico de la lista negra, asegurando que las direcciones bloqueadas no puedan interactuar con el sistema. Además, el microservicio valida las solicitudes entrantes y proporciona respuestas claras y detalladas en caso de errores, como campos faltantes o usuarios no encontrados.

## Endpoint de pruebas
https://www.postman.com/material-geoscientist-13340023/devops-08/collection/ex3pdbl/blacklist-service-api?action=share&creator=30444108

## Estructura

La estructura de archivos del microservicio es la siguiente:

```
DEVOPS_08/
├── src/                        # Código fuente del microservicio
│   ├── blueprints/             # Contiene los blueprints de la aplicación Flask
│   │   ├── __init__.py
│   │   └── blacklist.py
│   ├── commands/               # Lógica de negocio organizada por comandos
│   │   ├── __init__.py
│   │   ├── base_command.py     # Clase base para los comandos
│   │   ├── create_blacklist.py
│   │   ├── get_blacklist_info.py
│   │   └── reset_database.py
│   ├── errors/               # Manejo de errores personalizados
│   │   ├── __init__.py
│   │   └── errors.py
│   ├── models/               # Modelos y esquemas de datos de usuario
│   │   ├── __init__.py
│   │   ├── model.py          # Definición de la tabla de blacklist
│   │   └── schemas.py        # Esquemas de serialización
│   ├── database.py           # configuración de la base de datos
│   └── main.py               # Punto de entrada de la aplicación
├── tests/                    # Pruebas unitarias para el microservicio
│   ├── blueprints/           # Pruebas para los blueprints
│   │   └── ...
│   ├── commands/             # Pruebas para los comandos
│   │   └── ...
│   └── conftest.py           # Archivo de configuración para pytest
├── Dockerfile                # Definición de la imagen Docker
├── Pipfile                   # Dependencias del proyecto
├── Pipfile.lock              # Versiones bloqueadas de dependencias
├── docker-compose.yml        # Archivo de despliegue usando Docker Compose
└── README.md                 # Documentación del microservicio

```
## Ejecutar tests

Para ejecutar las pruebas unitarias del microservicio, sigue los pasos a continuación. Estos comandos te permitirán ejecutar las pruebas unitarias y verificar que el microservicio funciona correctamente.

1. Asegurate de tener instalado Python y el entorno activo en tu máquina.
2. Clona el repositorio del proyecto en tu máquina local.
3. Navega al directorio del reposotirio desde la terminal
4. Ejecuta el siguiente comando para instalar las dependencias del proyecto:

```bash
$ pip -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
5. Ejecuta el siguiente comando para ejecutar las pruebas unitarias del microservicio:

```bash
$ pytest --cov=src --cov-report=term-missing --cov-fail-under=70
```

## Ejecución con docker

Para ejecutar el microservicio, sigue los pasos a continuación. Estos comandos te permitirán construir y ejecutar el contenedor Docker del microservicio en tu máquina local.

1. Asegurate de tener instalado Docker y Docker Compose en tu máquina.
2. Clona el repositorio del proyecto en tu máquina local.
3. Navega al directorio del reposotirio desde la terminal
4. Ejecuta el siguiente comando para construir y ejecutar el contenedor Docker del microservicio:

```bash
# Descargar la imagen de PostgreSQL
docker pull postgres
# Construir la imagen del contenedor de PostgreSQL
docker run --name my-postgres-container --network my_network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=2024 -e 
# Ejecutar el contenedor de PostgreSQL
$ POSTGRES_DB=blacklist_db -p 5432:5432 -d postgres
# Construir la imagen del contenedor del microservicio
$ docker build -t my-flask-app . --no-cache
# Ejecutar el contenedor del microservicio
$ docker run --name my-flask-container --network my_network -p 3000:3000 my-flask-app
```

5. Carga el archivo `Blacklist Service API.postman_collection.json` en Postman para probar los endpoints del microservicio.
* o acceder a la siguiente URL Microservicio Inicial Semana 1-4: https://www.postman.com/material-geoscientist-13340023/devops-08/collection/ex3pdbl/blacklist-service-api?action=share&creator=30444108
* o acceder a la siguiente URL Microservicio Actualizacion Semana 5-6: https://blue-station-32150.postman.co/workspace/038a15bb-1801-4e03-a3ef-d92eb8e09b7e/collection/30632007-9b3d1715-a529-41fd-9c5a-cdce87c6e4f7
* o acceder a la siguiente URL Microservicio Actualizacion Semana 7-8: https://speeding-sunset-217733.postman.co/workspace/0b084a12-7986-48bb-8cf3-1976dc6b6a5a

## Integración con AWS Fargate y CI/CD (Entrega 3)
En la **Entrega 3**, se implementó la integración del microservicio con AWS utilizando **Fargate** para el despliegue sin servidores, **ECR** para almacenar la imagen Docker, un **ALB** para balanceo de tráfico, y un pipeline CI/CD automatizado con **GitHub**, **CodeBuild**, **CodePipeline**, y **CodeDeploy** (Blue/Green Deployment), logrando despliegues automáticos y escalables. Además, se actualizó la colección de Postman para reflejar los nuevos endpoints y configuraciones, garantizando pruebas actualizadas y funcionales.  

## Monitoreo con New Relic

En la **Entrega 4**, se implementó **New Relic** como herramienta de monitoreo continuo para el microservicio de Blacklist, con el objetivo de mejorar la visibilidad del rendimiento del sistema en tiempo real. La integración incluyó:
- **Instrumentación del código:** Configuración del agente de New Relic en el entorno Python y actualización del `Dockerfile` para garantizar la recopilación de métricas clave.
- **Pruebas de desempeño:** Validación local y en producción con herramientas como Locust para simular cargas de usuarios y analizar el impacto en los tiempos de respuesta y tasas de error.
- **Configuración de alertas:** Definición de umbrales  para tiempos de respuesta, tasas de error y caídas en el índice Apdex.
Esta integración asegura un monitoreo efectivo del microservicio, garantizando la alta disponibilidad y una respuesta confiable incluso en escenarios de alta demanda o fallos inesperados.

## Enlaces  al Repositorio del Proyecto
- [**README**](https://github.com/lesmesl/DevOps_08/blob/main/README.md)
- [**WIKI**](https://github.com/lesmesl/DevOps_08/wiki)
- [**Diseño de Arquitectura**](https://github.com/lesmesl/DevOps_08/wiki/Entrega-1:-Documento-Arquitectura)
- [**Código General de Aplicación**](https://github.com/lesmesl/DevOps_08/tree/main/src)
- [**Sustentaciones en Video**](https://github.com/lesmesl/DevOps_08/wiki/Sustentaciones-en-Video-%E2%80%90-Entregas)

## Otras Características (opcional)

Este proyecto de microservicio tiene las siguientes características adicionales que pueden ser útiles:

- **Persistencia en PostgreSQL:** El microservicio utiliza una base de datos PostgreSQL para almacenar y gestionar los datos de las publicaciones.
- **Manejo de Errores:** Implementa un manejo de errores robusto para asegurar respuestas claras y útiles a los usuarios finales y a otros servicios.
- **Despliegue en Docker:** El microservicio está configurado para ejecutarse en contenedores Docker, facilitando su despliegue en diferentes entornos.


