from dataclasses import fields
from rest_framework import routers, serializers, viewsets
from .models import Content

class ContentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Content
    fields = ('image', 'uploaded_at')