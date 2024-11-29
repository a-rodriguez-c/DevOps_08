from flask import Flask, jsonify
import logging
from src.database import init_db
from src.blueprints.blacklist import _blueprint
from src.errors.errors import ApiError
from flasgger import Swagger

logger = logging.getLogger(__name__)

def setup_app():
    app = Flask(__name__)
    app.register_blueprint(_blueprint)
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "API de Lista Negra",
            "description": "Este microservicio permite a las aplicaciones clientes agregar, consultar y eliminar direcciones de correo electrónico de la lista negra, asegurando que las direcciones bloqueadas no puedan interactuar con el sistema.",
            "version": "0.1.0",
            "license": {
                "name": "MIT",
                "url": "http://opensource.org/licenses/MIT"
            }
        },
        "basePath": "/",  # Base path para todas las rutas
        "schemes": [
            "http",
            "https"
        ],
        "operationId": "getmyData"
    }

    Swagger(app,template=swagger_template)  # Inicializar Flasgger


    @app.errorhandler(ApiError)
    def handle_error(err):
        logger.error(f"API Error: {err}", exc_info=True)
        response = {
            "msg": err.description if err.description else str(err),
        }
        return jsonify(response), err.code

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        logger.error(f"Unexpected error: {error}", exc_info=True)
        response = {
            "msg": "An unexpected error occurred."
        }
        return jsonify(response), 500

    return app

app = setup_app()
logger.info("App setup complete")
init_db()