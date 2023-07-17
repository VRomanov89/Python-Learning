#14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for string in zip(*strs):
            if len(set(string)) == 1:
                prefix += string[0]
            else:
                return prefix
        return prefix

#Notes
# zip(*strs) - returns tuples from the object


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2
        return dummy.next

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
    
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack)):
            for j in range(i, len(haystack)):
                print(haystack[i:j+1])
                if(haystack[i:j+1]==needle):
                    return(i)
        return -1