from ninja import Schema
from datetime import datetime
from pydantic import EmailStr
class WaitlistEntryCreateSchema(Schema):
    #Create -> Data
    # WaitlistEntryIn
    email: EmailStr
    name: str

class WaitlistEntryDetailSchema(Schema):
    # Get  -> Data
    # WaitlistEntryOut
    email: EmailStr
    name: str
    timestamp: datetime