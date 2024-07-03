from ninja import Schema
from datetime import datetime
from pydantic import EmailStr
class WaitlistEntryCreateSchema(Schema):
    #Create -> Data
    # WaitlistEntryIn
    email: str
    name: str

class WaitlistEntryDetailSchema(Schema):
    # Get  -> Data
    # WaitlistEntryOut
    email: str
    name: str
    timestamp: datetime