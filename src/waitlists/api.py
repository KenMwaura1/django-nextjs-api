from typing import List

from ninja import Router

from .models import WaitlistEntry
from .schemas import WaitlistEntryListSchema

router = Router()


@router.get("/waitlist", response=List[WaitlistEntryListSchema])
def list_waitlist_entries(request):
    qs = WaitlistEntry.objects.all()
    return qs
