import base64
import os
from src.commands.base_command import BaseCommand
from src.models.model import Blacklist
from src.errors.errors import InvalidParams, EmailAlreadyBlacklisted
from src.database import db_session
from src.models.schemas import CreateBlacklistInputSchema
from flask import request

class CreateBlacklist(BaseCommand):
    def __init__(self, email, app_uuid, blocked_reason, ip_address):
        self.email = email
        self.app_uuid = app_uuid
        self.blocked_reason = blocked_reason
        self.ip_address = request.remote_addr

    def execute(self):
        # Create an instance of the input schema
        input_schema = CreateBlacklistInputSchema()

        # Validate input data
        input_data = {
            "email": self.email,
            "app_uuid": self.app_uuid,
            "blocked_reason": self.blocked_reason,
            "ip_address": self.ip_address
        }

        errors = input_schema.validate(input_data)
        if errors:
            raise InvalidParams(errors)

        # Check if the email is already blacklisted
        existing_blacklist_entry = db_session.query(Blacklist).filter(
            Blacklist.email == self.email
        ).first()
        if existing_blacklist_entry:
            raise EmailAlreadyBlacklisted()

        # Create a new blacklist entry
        new_blacklist_entry = Blacklist(
            email=self.email,
            app_uuid=self.app_uuid,
            blocked_reason=self.blocked_reason,
            ip_address=self.ip_address
        )
        db_session.add(new_blacklist_entry)
        db_session.commit()

        # Return a success message after committing the new entry
        return {
            "message": "Blacklist entry successfully registered."
        }

