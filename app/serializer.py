from rest_framework import serializers
from .models import visitermodel

class visiterserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = visitermodel
        fields='__all__'