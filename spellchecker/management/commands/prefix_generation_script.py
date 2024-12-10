import json
from django.core.management.base import BaseCommand
from spellchecker.views import trie


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = 'spellchecker/data/en.json'

        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                if not data:
                    print("ERROR: No words found in the JSON file.")
                    return

                for word in data:
                    trie.insert(word)

                print(
                    f"SUCCESS: Successfully populated Trie with {len(data)} words.")

        except FileNotFoundError:
            print(f"ERROR: File not found: {file_path}")
        except json.JSONDecodeError:
            print("ERROR: Invalid JSON file format.")
