class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_the_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.end_of_the_word = True

    def search(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.end_of_the_word

    def starts_with(self, prefix):
        current = self.root
        for ch in prefix:
            if ch not in current.children:
                return []  # Return empty list if prefix doesn't exist
            current = current.children[ch]

        # Gather all words starting from the current TrieNode
        return self._collect_words(current, prefix)

    def _collect_words(self, node, prefix):
        """
        Helper method to collect all words starting from the given node.
        """
        words = []
        if node.end_of_the_word:
            words.append(prefix)

        for char, child_node in node.children.items():
            words.extend(self._collect_words(child_node, prefix + char))

        return words[:10]


trie = Trie()
