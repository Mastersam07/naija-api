
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import State
from .serializers import StateSerializer, LocalGovernmentAreaSerializer


class StateListView(APIView):
    def get(self, request):
        queryset = State.objects.all()
        serializer = StateSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


class StateDetailView(APIView):
    def get(self, request, slug):
        try:
            query = State.objects.get(slug__iexact=slug)
        except State.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = StateSerializer(query, context={'request': request})
            return Response(serializer.data)


class StateLGAView(APIView):
    def get(self, request, slug):
        try:
            query = State.objects.get(slug__iexact=slug)
        except State.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = LocalGovernmentAreaSerializer(
                query.lgas.all(), many=True, context={'request': request}
            )
            return Response(serializer.data)
