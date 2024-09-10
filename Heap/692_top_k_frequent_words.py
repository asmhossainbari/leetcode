# import heapq
# class WordFreq(object):
#     def __init__(self, word, freq):
#         self.word = word
#         self.freq = freq
#
#     def __lt__(self, other):
#         if self.freq == other.freq:
#             return self.word < other.word
#         else:
#             return self.freq > other.freq
#
# class Solution(object):
#     def topKFrequent(self, words, k):
#         """
#         :type words: List[str]
#         :type k: int
#         :rtype: List[str]
#         """
#         word_dict = dict()
#         for word in words:
#             if word not in word_dict:
#                 word_dict[word] = 1
#             else:
#                 word_dict[word] += 1
#         heap = []
#         for key in word_dict.keys():
#             heap_item = WordFreq(word=key, freq=word_dict[key])
#             heapq.heappush(heap, heap_item)
#         frequent_words = []
#         for i in range(k):
#             word = heapq.heappop(heap).word
#             frequent_words.append(word)
#         return frequent_words

import heapq
import collections
import typing

class WordFreq(object):
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word < other.word
        else:
            return self.freq < other.freq


class Solution:
    def topKFrequent(self, words, k):
        hash_map = collections.defaultdict(int)
        min_heap = []
        for word in words:
            hash_map[word] += 1
        for word, freq in hash_map.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, WordFreq(word, freq))
            elif min_heap[0].freq < freq:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, WordFreq(word, freq))

        result = []
        for i in range(k):
            result.append(heapq.heappop(min_heap).word)
        result = result[::-1]
        return result

        # return [heapq.heappop(min_heap).word for _ in range(len(min_heap))][::-1]

sol = Solution()
# print(sol.topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=2))
print(sol.topKFrequent(words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4))
print(sol.topKFrequent(words=["aaa","aa","a"], k = 1))