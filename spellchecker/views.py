from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import WordSerializer, PrefixSerializer
from spellchecker.trie import trie
import json


class PopulateTrieView(APIView):
    """
    A view to populate the trie from a JSON file.
    """

    def post(self, request):
        # Path to your JSON file
        file_path = "spellchecker/data/en.json"

        try:
            with open(file_path, 'r') as f:
                words = json.load(f)
        except FileNotFoundError:
            return Response({'error': 'JSON file not found.'}, status=status.HTTP_404_NOT_FOUND)
        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON file.'}, status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(words, list):
            return Response({'error': 'JSON file must contain a list of words.'}, status=status.HTTP_400_BAD_REQUEST)

        for word in words:
            trie.insert(word)

        return Response({'message': 'Trie successfully populated with words from JSON file.'},
                        status=status.HTTP_201_CREATED)


class InsertWordView(APIView):
    def post(self, request):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            word = serializer.validated_data['word']
            trie.insert(word)
            return Response({'message': f"Word '{word}' inserted successfully!"},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchWordView(APIView):
    def get(self, request):
        serializer = WordSerializer(data=request.query_params)
        if serializer.is_valid():
            word = serializer.validated_data['word']
            result = trie.search(word)
            return Response({'word': word, 'exists': result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StartsWithView(APIView):
    def get(self, request):
        serializer = PrefixSerializer(data=request.query_params)
        if serializer.is_valid():
            prefix = serializer.validated_data['prefix']
            result = trie.starts_with(prefix)
            return Response({'prefix': prefix, 'all_possibilities': result},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
