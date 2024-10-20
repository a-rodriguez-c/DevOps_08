from commands.base_command import BaseCommand
from database import db_session
from models.model import Blacklist

class ResetDatabase(BaseCommand):
    def execute(self):
        db_session.query(Blacklist).delete()
        db_session.commit()
        return {"msg": "Todos los datos fueron eliminados"}