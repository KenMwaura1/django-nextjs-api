from ninja import Schema
from datetime import datetime
from pydantic import EmailStr


class WaitlistEntryCreateSchema(Schema):
    #Create -> Data
    # WaitlistEntryIn
    email: EmailStr
    # name: str

class WaitlistEntryListSchema(Schema):
    # List -> Data
    # WaitlistEntryOut
    id: int
    email: EmailStr

class WaitlistEntryDetailSchema(Schema):
    # Get  -> Data
    # WaitlistEntryOut
    id: int
    email: EmailStr
    updated: datetime
    timestamp: datetime
