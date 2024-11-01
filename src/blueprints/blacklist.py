import time

from flask import Blueprint, request, jsonify
from flasgger import swag_from
from src.commands.reset_database import ResetDatabase
from src.commands.create_blacklist import CreateBlacklist
from src.commands.get_blacklist_info import GetBlacklistInfo
from src.errors.errors import EmailAlreadyBlacklisted, InvalidParams, EmailNotFound
from src.decorators.auth import token_required

_blueprint = Blueprint('blacklist', __name__)

@_blueprint.route('/blacklists', methods=['POST'])
@token_required
@swag_from({
    'summary': 'Crear una entrada en la lista negra',
    'description': 'Crea una nueva entrada en la lista negra proporcionando un correo electrónico y otros detalles.',
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'required': True,
            'type': 'string',
            'description': 'Bearer token-super-secreto',
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {'type': 'string', 'example': 'test@example.com'},
                    'app_uuid': {'type': 'string', 'example': '123e4567-e89b-12d3-a456-426614174000'},
                    'blocked_reason': {'type': 'string', 'example': 'Spamming'}
                },
                'required': ['email', 'app_uuid']
            }
        }
    ],
    'responses': {
        '201': {"description": "Blacklist entry successfully registered."},
        '400': {'description': 'Parámetros inválidos.'},
        '409': {'description': 'El correo ya está en la lista negra.'},
        '401': {'description': 'Token no válido o ausente.'}
    }
})
def create_blacklist_entry():
    try:
        data = request.get_json()
        # inyecto un error de variable no definida:
        print(error['error'])
        create_blacklist_command = CreateBlacklist(
            data.get('email'),
            data.get('app_uuid'),
            data.get('blocked_reason'),
            data.get('ip_address')
        ).execute()
        return jsonify(create_blacklist_command), 201
    except (InvalidParams, EmailAlreadyBlacklisted) as e:
        return e.description, e.code
    except Exception as e:
        return str(e), 400


@_blueprint.route('/blacklists/<email>', methods=['GET'])
@token_required
@swag_from({
    'summary': 'Obtener información de una lista negra',
    'description': 'Obtiene detalles de un correo electrónico en la lista negra.',
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'required': True,
            'type': 'string',
            'description': 'Bearer token',
            'example': 'Bearer <token>'
        },
        {
            'name': 'email',
            'in': 'path',
            'required': True,
            'type': 'string',
            'description': 'El correo electrónico a consultar.',
            'example': 'test@example.com'
        }
    ],
    'responses': {
        '200': {
            'description': 'Detalles de la lista negra obtenidos con éxito',
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {'type': 'string'},
                    'app_uuid': {'type': 'string'},
                    'blocked_reason': {'type': 'string'},
                    'ip_address': {'type': 'string'}
                }
            }
        },
        '404': {'description': 'Correo no encontrado.'},
        '500': {'description': 'Error interno del servidor.'},
        '401': {'description': 'Token no válido o ausente.'}
    }
})
def get_blacklist_info(email):
    try:
        # inyecto un error de variable no definida:
        print(error['error'])
        blacklist_info = GetBlacklistInfo(email).execute()
        return jsonify(blacklist_info), 200
    except EmailNotFound:
        return '', 404
    except Exception as e:
        return str(e), 500


@_blueprint.route('/blacklists/ping', methods=['GET'])
@swag_from({
    'summary': 'Comprobar el estado del servicio',
    'description': 'Ping para comprobar que el servicio está funcionando.',
    'responses': {
        '200': {'description': 'El servicio está en funcionamiento.'}
    }
})
def ping():
    # inyecto un error de variable no definida:
    print(error['error'])
    return 'pong', 200


@_blueprint.route('/', methods=['GET'])
def rootpath():
    # inyecto un error de variable no definida:
    print(error['error'])
    return 'ok', 200


@_blueprint.route('/blacklists/rolling', methods=['GET'])
def rolling():
    # inyecto un error de variable no definida:
    print(error['error'])
    return 'ok', 200



@_blueprint.route('/blacklists/rolling-batch', methods=['GET'])
def rollingBatch():
    # inyecto un error de variable no definida:
    print(error['error'])
    return 'ok', 200



@_blueprint.route('/blacklists/inmutable', methods=['GET'])
def inmutable():
    # inyecto un error de variable no definida:
    print(error['error'])    
    return 'ok', 200



@_blueprint.route('/blacklists/all-at-once', methods=['GET'])
def allAtOnce():
    # inyecto un error de variable no definida:
    print(error['error'])
    return 'ok', 200



@_blueprint.route('/blacklists/base', methods=['GET'])
def base():
    # inyecto un error de variable no definida:
    print(error['error'])
    time.sleep(5)
    return 'ok', 200


@_blueprint.route('/blacklists/reset', methods=['POST'])
@token_required
@swag_from({
    'summary': 'Reiniciar la base de datos de listas negras',
    'description': 'Este endpoint restablece la base de datos de listas negras.',
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'required': True,
            'type': 'string',
            'description': 'Bearer <token>'
        }
    ],
    'responses': {
        '200': {"description": "Todos los datos fueron eliminados"},
        '401': {"description": "Token is missing or invalid!"}
    }
})
def reset_database():
    # inyecto un error de variable no definida:
    print(error['error'])
    result = ResetDatabase().execute()
    return jsonify(result), 200
