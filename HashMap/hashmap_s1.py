"""
Leetcode top interview 150
https://leetcode.com/studyplan/top-interview-150/

Problem links:
1. https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
2. https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150
3. https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150
4. https://leetcode.com/problems/valid-anagram/description/?envType=study
-plan-v2&envId=top-interview-150

"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool

        this solution on leetcode took:
        14 ms Beats 99.75% of users with Python
        """
        ran_lett = set(ransomNote)
        for letter in ran_lett:
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True

    def get_count_and_all_index(self, string, ch):
        str_count = string.count(ch)
        indx = [idx for idx, ltr in enumerate(string) if ltr == ch]
        return str_count, indx

    def isIsomorphic(self, r, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        # TODO: Solution is having worst time complexity
        """
        str_len = len(t)
        while str_len > 0:
            # for a, b in zip(r, t):
            #     r_count_indx = s.get_count_and_all_index(r, a)
            #     t_count_indx = s.get_count_and_all_index(t, b)
            #     if r_count_indx == t_count_indx:
            #         r = r.replace(a, "")
            #         t = t.replace(b, "")
            #         str_len -= r_count_indx[0]
            #     else:
            #         return False
            for a, b in zip(r, t):
                r_idx = [idx for idx, ltr in enumerate(r) if ltr == a]
                t_idx = [idx for idx, ltr in enumerate(t) if ltr == b]
                if r_idx == t_idx:
                    r = r.replace(a, "")
                    t = t.replace(b, "")
                    str_len -= len(r_idx)
                else:
                    return False
        return True

    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        TODO: Sol failing for test case discuss with Abhi
        test case: "aaa", "aa aa aa aa"
        """
        dt = {}
        for pt, ch in zip(pattern, s.split(" ")):
            if pt not in dt and ch not in dt.values():
                dt[pt] = ch
            elif (pt in dt and dt[pt] != ch) or (
                    ch in dt.values() and pt not in dt):
                return False
        return True

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        # s = [*s]
        # t = [*t]
        # s.sort()
        # t.sort()
        # if s == t:
        #     return True
        # else:
        #     return False
        sd = {}
        td = {}
        for l, c in zip(s, t):
            if l not in sd:
                sd[l] = s.count(l)
            if c not in td:
                td[c] = t.count(c)
        if sd == td:
            return True
        else:
            return False

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        if len(strs) == 1 or len(set(strs)) == 1:
            return [strs]

        for ch in strs:
            sw = ''.join(sorted(ch))
            if sw in groups:
                groups[sw].append(ch)
            else:
                groups[sw] = ([ch])
        return groups.values()


so = Solution()
# print(so.canConstruct('aa',
#                     'aab'))
# print(so.isIsomorphic("foo", "bar"))
# print(so.wordPattern("aaaa", "aa aa aa aa"))
# print(so.isAnagram("a", "ab"))
print(so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
