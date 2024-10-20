from flask import Blueprint, request, jsonify
from src.commands.create_blacklist import CreateBlacklist
from src.commands.get_blacklist_info import GetBlacklistInfo
from src.errors.errors import InvalidParams, EmailNotFound
from src.decorators.auth import token_required 
import uuid

blacklist_blueprint = Blueprint('blacklist', __name__)

@blacklist_blueprint.route('/blacklists', methods=['POST'])
@token_required
def create_blacklist_entry():
    try:
        data = request.get_json()

        # Create a new blacklist entry using the provided email and other details
        create_blacklist_command = CreateBlacklist(
            data.get('email'),
            data.get('app_uuid'),
            data.get('blocked_reason'),
            data.get('ip_address')
        ).execute()
        return jsonify(create_blacklist_command), 201
    except InvalidParams as e:
        return e.description, e.code
    except Exception as e:
        return str(e), 400

@blacklist_blueprint.route('/blacklists/<email>', methods=['GET'])
@token_required
def get_blacklist_info(email):
    try:
        # Retrieve information about the blacklisted email
        blacklist_info = GetBlacklistInfo(email).execute()
        return jsonify(blacklist_info), 200
    except EmailNotFound:
        return '', 404
    except Exception as e:
        return str(e), 500

@blacklist_blueprint.route('/blacklists/ping', methods=['GET'])
def ping():
    return 'pong', 200
