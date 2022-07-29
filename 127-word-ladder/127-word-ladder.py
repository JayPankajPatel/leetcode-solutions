class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_list = set(wordList)
        def get_neighbors(word):
            res = []
            for i in range(len(word)):
                cpy = word
                for c in ascii_letters:
                    next_word = cpy[:i] + c + cpy[i+1:]
                    if next_word not in word_list:
                        continue
                    else:
                        res.append(next_word)
            return res
        queue = deque()
        queue.append([beginWord, 0])
        visited = set()
        visited.add(beginWord)
        while queue:
            piece, steps = queue.popleft()
            if piece == endWord:
                return steps+1
            for neig in get_neighbors(piece):
                if neig not in visited:
                    queue.append([neig, steps+1])
                    visited.add(neig)


        return 0