from rest_framework import serializers

class MyTextSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    tree = serializers.CharField(read_only=True)
    limit = serializers.IntegerField(read_only=True)
    