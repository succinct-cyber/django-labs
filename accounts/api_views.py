from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ProfileSerializer

class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = request.user.profile
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


@api_view(["GET"])
def test_api(request):
    return Response({
        "message": "DRF is working",
        "user": str(request.user)
    })

@api_view(["POST"])
def login_api(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response(
            {"error": "Username and password required"},
            status=400
        )

    user = authenticate(username=username, password=password)

    if user is None:
        return Response(
            {"error": "Invalid credentials"},
            status=401
        )

    login(request, user)

    return Response({
        "message": "Login successful",
        "user_id": user.id,
        "username": user.username
    })
