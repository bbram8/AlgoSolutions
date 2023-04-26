# reference - https://leetcode.com/problems/top-k-frequent-words/description/
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        cnt = Counter(words)
        bucket = [{} for _ in range(n+1)]
        self.k = k

        def add_word(trie: Mapping, word: str) -> None:
            # initialize the root to the root of the trie
            root = trie

            # iterate through the word
            for c in word:
              # if the letter is not found then add it to the trie
                if c not in root:
                    root[c] = {}
              # new root will be the character
                root = root[c]
              # when the word's end is reached add a '#'
            root['#'] = {}

        def get_words(trie: Mapping, prefix: str) -> List[str]:
            if self.k == 0:
                return []
            res = []

            # if the word's end is reached then top k needs to be decremented
            # and word needs to be added to the result list
            if '#' in trie:
                self.k -= 1
                res.append(prefix)
            for i in range(26):
              # function returns alphabet from a to z
                c = chr(ord('a') + i)

                if c in trie:
                  # recursive call to get the letters further in the trie
                  # pass the children of the character in the trie and prefix + character  as arguments to the recursive call e.g. trie[c] = 'n' and prefix = "an"
                    res += get_words(trie[c], prefix+c)
            return res

        # store the words in the bucket based on the frequency for e.g. 
        # word that occurs once is stored as a trie in bucket with index 1 

        for word, freq in cnt.items():
            add_word(bucket[freq], word)

        res = []

        # start adding the words to result in reverse order i.e. top k
        for i in range(n, 0, -1):
            if self.k == 0:
                return res
                # if a bucket exists with a word in it only then retrieve the words
            if bucket[i]:
                res += get_words(bucket[i], '')
        return res

        # other approaches

        #word_map = collections.defaultdict(int)
        
        #for word in words: word_map[word] += 1
        
        #output = sorted(word_map, key = lambda x: (-word_map[x],x))
        
        #return output [:k]

        #heap = []
        #word_count = collections.Counter(words)

        #for word, freq in word_count.items():
           # heapq.heappush(heap, [-freq, word])
        
        #output = []

       # for i in range(k):
           # count, word = heapq.heappop(heap)

            #output.append(word)
        
        #return output

         
         #bucket sort approach

        
        # variable to hold the max frequency words
       # max_word_count=0

        # dictionary to store the frequency (word : frequency)
        #dict = collections.defaultdict(int)

        # dictionary to store the frequency and list of words with that frequency
        # (frequency : [list of words with that frequency])

        #count=collections.defaultdict(list)
        #for word in words:
           # dict[word] += 1

            # key will be freq and value will be the list of words matching that frequency 
            #count[dict[word]].append(word)
            #max_word_count=max(max_word_count,dict[word])
        #output=[]

        # no dupes hence set
        #visited=set()
        #while k:
          
            #count[max_word_count].sort()
            #for word in count[max_word_count]:
               # if word not in visited:
                 #   output.append(word)
                 #   visited.add(word)
                 #   k-=1
                  #  if not k:
                  #      return output
            # move to the next bucket until k becomes zero
            #max_word_count-=1
        #return output

      
