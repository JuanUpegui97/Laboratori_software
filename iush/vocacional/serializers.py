from rest_framework import serializers
from .models import Pregunta

class PreguntaSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    pregunta = serializers.CharField()
    respuestas = serializers.DictField()

    def create(self, validated_data):
        return Pregunta(**validated_data).save()

    def update(self, instance, validated_data):
        instance.pregunta = validated_data.get('pregunta', instance.pregunta)
        instance.respuestas = validated_data.get('respuestas', instance.respuestas)
        instance.save()
        return instance