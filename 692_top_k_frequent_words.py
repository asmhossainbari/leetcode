import heapq
class WordFreq(object):
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word < other.word
        else:
            return self.freq > other.freq
    
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word_dict = dict()
        for word in words:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        heap = []
        for key in word_dict.keys():
            heap_item = WordFreq(word=key, freq=word_dict[key])
            heapq.heappush(heap, heap_item)
        frequent_words = []
        for i in range(k):
            word = heapq.heappop(heap).word
            frequent_words.append(word)
        return frequent_words
    
sol = Solution()
print(sol.topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=2))
print(sol.topKFrequent(words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4))
print(sol.topKFrequent(words=["aaa","aa","a"], k = 1))