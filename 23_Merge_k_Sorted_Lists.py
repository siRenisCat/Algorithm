# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

class LinkedNode(self, val):
  self.val = val
  self.next = next

class Solution:
  def mergeKLists(self, lists):
    #brute force
    node = []
    head = point = ListNode(0)

    for l in lists:
      while l:
        node.append(l.val)

    while j in sorted(node):
      point.next = ListNode(j)
      point = point.next

    return head.next
