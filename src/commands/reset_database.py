from src.commands.base_command import BaseCommand
from src.database import session_scope  # Importa session_scope
from src.models.model import Blacklist
import logging

logger = logging.getLogger(__name__)

class ResetDatabase(BaseCommand):
    def execute(self):
        with session_scope() as session:
            session.query(Blacklist).delete()
            logger.info("Todos los datos fueron eliminados de la tabla Blacklist")
        return {"msg": "Todos los datos fueron eliminados"}