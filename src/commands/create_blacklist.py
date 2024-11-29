from src.commands.base_command import BaseCommand
from src.models.model import Blacklist
from src.errors.errors import InvalidParams, EmailAlreadyBlacklisted
from src.database import session_scope
from src.models.schemas import CreateBlacklistInputSchema
from flask import request
import logging

logger = logging.getLogger(__name__)

class CreateBlacklist(BaseCommand):
    def __init__(self, email, app_uuid, blocked_reason, ip_address):
        self.email = email
        self.app_uuid = app_uuid
        self.blocked_reason = blocked_reason
        self.ip_address = request.remote_addr

    def execute(self):
        input_schema = CreateBlacklistInputSchema()

        input_data = {
            "email": self.email,
            "app_uuid": self.app_uuid,
            "blocked_reason": self.blocked_reason,
            "ip_address": self.ip_address
        }

        errors = input_schema.validate(input_data)
        if errors:
            logger.error(f"Invalid parameters: {errors}")
            raise InvalidParams(errors)

        with session_scope() as session:
            existing_blacklist_entry = session.query(Blacklist).filter(
                Blacklist.email == self.email
            ).first()
            if existing_blacklist_entry:
                logger.error(f"Email already blacklisted: {self.email}")
                raise EmailAlreadyBlacklisted()

            new_blacklist_entry = Blacklist(
                email=self.email,
                app_uuid=self.app_uuid,
                blocked_reason=self.blocked_reason,
                ip_address=self.ip_address
            )
            session.add(new_blacklist_entry)

        logger.info(f"Blacklist entry successfully registered for email: {self.email}")
        return {
            "message": "Blacklist entry successfully registered."
        }