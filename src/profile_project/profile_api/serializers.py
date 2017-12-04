from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serialzies a name field for testing out APIViews"""
    name = serializers.CharField(max_length=10)
