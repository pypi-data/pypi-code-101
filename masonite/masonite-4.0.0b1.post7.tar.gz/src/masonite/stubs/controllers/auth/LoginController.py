from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from masonite.response import Response
from masonite.authentication import Auth


class LoginController(Controller):
    def show(self, view: View):
        return view.render("auth.login")

    def store(self, view: View, request: Request, auth: Auth, response: Response):
        login = auth.attempt(request.input("username"), request.input("password"))

        if login:
            return response.redirect(name="home")

        # Go back to login page
        return response.redirect(name="login")
