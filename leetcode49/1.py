from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        hashtable = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in hashtable:
                hashtable[sorted_s].append(s)
            else:
                hashtable[sorted_s] = [s]
        for group in hashtable.values():
            answer.append(group)
        
        if answer == []:
            return [[""]]
        else:
            return answer
