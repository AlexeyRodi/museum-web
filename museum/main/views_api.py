from .models import Exhibition

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ExhibitionsSerializer

class ExhibitionsAPI(APIView):
    def get(self, request):
        exhibitions = Exhibition.objects.all()
        serializer = ExhibitionsSerializer(exhibitions, many=True)
        return Response(serializer.data)