from marshmallow import ValidationError
from src.commands.base_command import BaseCommand
from src.models.model import Blacklist
from src.errors.errors import InvalidParams
from src.database import db_session
from src.models.schemas import GetBlacklistInfoInputSchema, GetBlacklistInfoOutputSchema

class GetBlacklistInfo(BaseCommand):
    def __init__(self, email):
        self.email = email

    def execute(self):
        # Validar el correo electrónico utilizando el schema
        try:
            validated_data = GetBlacklistInfoInputSchema().load({'email': self.email})
            email = validated_data['email']
        except ValidationError as err:
            raise InvalidParams(err.messages)

        # Consultar el modelo Blacklist para el correo validado
        blacklist_entry = db_session.query(Blacklist).filter(Blacklist.email == email).first()

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