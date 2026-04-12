class Trie:

    def __init__(self):
        self.child = [None] * 26
        self.isEnd = False     

    def insert(self, word: str) -> None:
        cur = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if cur.child[ch] is None:
                cur.child[ch] = Trie()
            cur = cur.child[ch]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if cur.child[ch] is None:
                return False
            cur = cur.child[ch]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for ch in prefix:
            ch = ord(ch) - ord('a')
            if cur.child[ch] is None:
                return False
            cur = cur.child[ch]
        return True