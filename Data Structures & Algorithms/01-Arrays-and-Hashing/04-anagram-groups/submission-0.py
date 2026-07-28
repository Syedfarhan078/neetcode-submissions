class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list) #dictionary to store anagram groups

        for string in strs:
            sorted_keys = "".join(sorted(string)) #create a key by sorting the character of the string

            #add the original string to its anagram group
            anagram_group[sorted_keys].append(string)
        
        #convert dict to list
        return list(anagram_group.values())