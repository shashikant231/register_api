from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view



from .serializers import RegistrationSerializer


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "successfully registered a new user"
        else:
            data = serializer.error()
        return Response(data)        

