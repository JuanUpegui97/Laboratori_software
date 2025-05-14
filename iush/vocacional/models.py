from django.db import models
from mongoengine import Document, StringField, DictField

class Pregunta(Document):
    pregunta = StringField(required=True)
    respuestas = DictField()  # Para respuestas como respuesta1, respuesta2, etc.

    meta = {
        'collection': 'Question'  # 👈 Aquí le indicas a MongoEngine el nombre real
    }