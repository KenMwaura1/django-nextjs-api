from ninja import NinjaAPI, Schema
from rich import print

from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router("/waitlists/", "waitlists.api.router")

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str = None


@api.get("/hello")
def user(request):
    print(request)
    return "Hello World"


@api.get("/user", response=UserSchema, auth=JWTAuth())
def user(request):
    return request.user
