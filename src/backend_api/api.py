from ninja import NinjaAPI, Schema
from rich import print

api = NinjaAPI()


class UserSchema(Schema):
    username: str
    is_authenticated: bool


@api.get("/hello")
def user(request):
    return request.user
