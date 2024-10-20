from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

Base = declarative_base()

class Blacklist(Base):
    __tablename__ = 'blacklist'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    email = Column(String(120), nullable=False, unique=True)
    app_uuid = Column(String(36), nullable=False)
    blocked_reason = Column(String(255), nullable=True)
    ip_address = Column(String(45), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, email, app_uuid, ip_address, blocked_reason=None):
        self.email = email
        self.app_uuid = app_uuid
        self.ip_address = ip_address
        self.blocked_reason = blocked_reason