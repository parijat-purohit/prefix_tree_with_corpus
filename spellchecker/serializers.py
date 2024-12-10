from rest_framework import serializers


class WordSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=100)


class PrefixSerializer(serializers.Serializer):
    prefix = serializers.CharField(max_length=100)
