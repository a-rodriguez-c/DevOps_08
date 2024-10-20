from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from enum import Enum as PyEnum
from src.models.base_model import Model

Base = declarative_base()

class UserStatus(PyEnum):
    POR_VERIFICAR = "POR_VERIFICAR"
    NO_VERIFICADO = "NO_VERIFICADO"
    VERIFICADO = "VERIFICADO"

class User(Model, Base):
    __tablename__ = 'users'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phoneNumber = Column(String, nullable=True)
    dni = Column(String, nullable=True)
    fullName = Column(String, nullable=True)
    salt = Column(String, nullable=False)
    token = Column(String, nullable=True)
    status = Column(Enum(UserStatus), nullable=False, default=UserStatus.POR_VERIFICAR)
    expireAt = Column(DateTime, nullable=True)


    def __init__(self, username, password, email, dni=None, fullName=None, phoneNumber=None, salt=None):
        Model.__init__(self)
        self.username = username
        self.password = password
        self.email = email
        self.dni = dni
        self.fullName = fullName
        self.phoneNumber = phoneNumber
        self.salt = salt
        self.status = UserStatus.POR_VERIFICAR


class Blacklist(Model, Base):
    __tablename__ = 'blacklist'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    email = Column(String(120), nullable=False, unique=True)
    app_uuid = Column(String(36), nullable=False)
    blocked_reason = Column(String(255), nullable=True)
    ip_address = Column(String(45), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, email, app_uuid, ip_address, blocked_reason=None):
        Model.__init__(self)
        self.email = email
        self.app_uuid = app_uuid
        self.ip_address = ip_address
        self.blocked_reason = blocked_reason