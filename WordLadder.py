"""
The approach here is to first maintain a hashmap of all the possible types of intermediate words with their
keys as * at every char for the words in wordDict array, now we have a possible intermediate words, now
we replace * at every postion in the begin word, and check if there is such a key present in the hashmap,
if so we add the the possible intermediate words in the queue and then keep poping one element by one, so
the same * replacement step for all of the those, while adding the words to the queue we check if the words
are already visited, if so we we don't add them to queue, like this we explore all possible paths from the
begin word, once we find the end word we return the level value, which has been kept updating for every new
word from the begin word.

Leetcode - running
Time complexity - O(N*W) where N = len of wordDict and W is len of word.
Space complexity - O(N*W)
"""
def ladderLength(self, beginWord, endWord, wordList):
    if endWord not in set(wordList):
        return 0
    L = len(wordList[0])
    dic = collections.defaultdict(list)
    queue = collections.deque([(beginWord, 1)])
    for word in wordList: # O(N x Word.length)
        for i in range(L):
            possible = word[0:i] + '.' + word[i+1:]
            dic[possible].append(word)
    wordList = set(wordList)
    while queue: #  O(Word.length x N)
        cur, length = queue.popleft()
        for i in range(L): 
            possible = cur[0:i] + '.' + cur[i+1:]
            for next_word in dic[possible]:
                if next_word == endWord:
                    return length + 1
                elif next_word in wordList:
                    queue.append((next_word, length+1))
                    wordList.remove(next_word)
    return 0
