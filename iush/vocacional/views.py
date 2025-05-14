from asyncio import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Pregunta
from .serializers import PreguntaSerializer
from rest_framework import mixins


class PreguntaViewSet(ListModelMixin, 
                      CreateModelMixin, 
                      mixins.RetrieveModelMixin,   # 👈 permite GET /<id>/
                      mixins.UpdateModelMixin,     # 👈 permite PUT y PATCH
                      mixins.DestroyModelMixin,    # 👈 permite DELETE
                      GenericViewSet):
    serializer_class = PreguntaSerializer

    def get_queryset(self):
        return list(Pregunta.objects.all())  # 👈 ¡Esto soluciona el problema!