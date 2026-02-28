from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = User.objects.filter(username=username).first()
    if user and user.check_password(password):
        return Response({"message": "Login successful"})
    return Response({"message": "Invalid credentials"}, status=401)
