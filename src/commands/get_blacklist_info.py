from marshmallow import ValidationError
from src.commands.base_command import BaseCommand
from src.models.model import Blacklist
from src.errors.errors import InvalidParams
from src.database import session_scope  # Importa session_scope
from src.models.schemas import GetBlacklistInfoInputSchema, GetBlacklistInfoOutputSchema
import logging

logger = logging.getLogger(__name__)

class GetBlacklistInfo(BaseCommand):
    def __init__(self, email):
        self.email = email

    def execute(self):
        # Validar el correo electrónico utilizando el schema
        try:
            validated_data = GetBlacklistInfoInputSchema().load({'email': self.email})
            email = validated_data['email']
        except ValidationError as err:
            logger.error(f"Invalid parameters: {err.messages}")
            raise InvalidParams(err.messages)

        # Manejar la sesión de la base de datos con session_scope
        with session_scope() as session:
            # Consultar el modelo Blacklist para el correo validado
            blacklist_entry = session.query(Blacklist).filter(Blacklist.email == email).first()

            # Preparar los datos de respuesta
            if not blacklist_entry:
                data = {
                    'found': False,
                    'reason': "El correo electrónico no se encuentra en la lista negra."
                }
            else:
                data = {
                    'found': True,
                    'reason': blacklist_entry.blocked_reason
                }

        # Serializar y devolver los datos utilizando el schema
        return GetBlacklistInfoOutputSchema().dump(data)