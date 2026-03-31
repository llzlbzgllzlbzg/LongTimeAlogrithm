from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        hashtable = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            # 这里用排序后的字符串做为哈希表的键，换成统计每个字符出现的次数可以更快一些
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
