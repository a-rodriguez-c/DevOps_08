from src.commands.base_command import BaseCommand
from src.models.model import Blacklist
from src.errors.errors import InvalidParams, EmailNotFound
from src.database import db_session

class GetBlacklistInfo(BaseCommand):
    def __init__(self, email):
        self.email = email

    def execute(self):
        # Validate email format (if necessary, you could add custom validation here)
        if not self.email:
            raise InvalidParams({"email": "Email is required."})

        # Query the Blacklist model for the provided email
        blacklist_entry = db_session.query(Blacklist).filter(Blacklist.email == self.email).first()

        # If the entry is not found, return false and no reason
        if not blacklist_entry:
            return {
                "found": False,
                "blocked_reason": None
            }

        # If the entry is found, return true and the blocked reason
        return {
            "found": True,
            "blocked_reason": blacklist_entry.blocked_reason
        }
