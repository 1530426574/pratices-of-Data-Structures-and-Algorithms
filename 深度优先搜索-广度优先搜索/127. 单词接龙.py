from collections import defaultdict
from pprint import pprint


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:
        """
        关键在哪呢，广度优先遍历的概念->每层轮询访问。
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        l = len(beginWord)  # 单词列表的所有单词长度一致
        d = defaultdict(list)
        # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        for word in wordList:
            for i in range(3):
                key = word[:i] + '*' + word[i + 1:]
                d[key].append(word)

        queue = [(beginWord, 1)]
        visited = {beginWord: True}
        while queue:
            cur, level = queue.pop(0)
            for i in range(l):
                key1 = cur[:i] + '*' + cur[i + 1:]
                for word in d[key1]:  # key不存在的话，value默认为[]
                    if word == endWord:
                        return level + 1
                    if word in visited:
                        continue
                    visited[word] = True
                    queue.append((word, level + 1))  # 相当于把每一层的节点都放入队列当中。
                d[key1] = []
        return 0


class Solution2:
    def __init__(self):
        self.length = 0
        self.d = defaultdict(list)

    def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        self.length = len(beginWord)
        for word in wordList:
            for i in range(self.length):
                self.d[word[:i] + '*' + word[i + 1:]].append(word)
        queue_begin = [(beginWord, 1)]
        queue_end = [(endWord, 1)]
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None
        while queue_begin and queue_end:

            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
        ans = self.visitWordNode(queue_end, visited_end, visited_begin)
        if ans:
            return ans
        return 0

    def visitWordNode(self, queue, visited, others_visited):
        cur, level = queue.pop(0)
        for i in range(self.length):
            key = cur[:i] + '*' + cur[i + 1:]
            for word in self.d[key]:
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None


def test():
    d = defaultdict(list)
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    for word in wordList:
        for i in range(3):
            key = word[:i] + '*' + word[i + 1:]
            d[key].append(word)
    pprint(d)
    return d


test()
