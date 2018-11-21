from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    success_url = 'regisration_create_book'