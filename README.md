# Trie-Based Spellchecker/Autocomplete with Django REST Framework
A reliable spellchecker and autocomplete system depends not just on the data structure, but on the corpus it relies on. While this project uses a Prefix Tree (Trie), the overall performance and accuracy are driven by the quality of the word corpus. For this implementation, I've used two sources of common English words:

Source 1: https://github.com/SMenigat/thousand-most-common-words/tree/master

Source 2: https://github.com/first20hours/google-10000-english/tree/master

## Key Features
* **No Database:** The project generates the trie tree directly from a JSON file, so there are no database queries involved, ensuring fast search and autocomplete operations.
* **Efficient Search:** With the trie data structure, searching for words or prefixes is done in constant time, making operations much faster compared to searching in a list.

## Endpoints
1. `populate-trie/`: Generates the trie from the provided JSON file.
2. `insert/`: Inserts a word into the trie.
3. `search/`: Searches for an exact word in the trie.
4. `startswith/`: Searches for a prefix and returns the first 10 suggestions (similar to autocomplete).

## Why Use a Trie?
A standard word search in an unsorted list has a time complexity of _O(n*k)_ where _n_ is the number of words and _k_ is the length of the longest word. In contrast, searching in a trie has a time complexity of _O(k)_, where _k_ is the length of the word or prefix.

Additionally, when searching for a single-character prefix, the trie provides
_O(1)_ time complexity, while a list search would still take _O(n)_.

## Initial Setup
1. Initially, a script was used to generate the trie, but it wasn’t storing any data.
2. Once the first endpoint (`populate-trie/`) is hit, the trie will be generated with the provided words.
3. The prefix tree can then be used for subsequent operations.