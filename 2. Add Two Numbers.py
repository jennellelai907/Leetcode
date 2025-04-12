""" You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



 """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            val = l1_val + l2_val + carry
            carry = val // 10
            val = val % 10

            cur.next = ListNode(val)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


# ListNode 是 單向鏈結串列 (singly linked list) 的節點類別，通常在 LeetCode 的鏈結串列題目中作為基礎結構使用

# 每個 ListNode 物件包含兩個屬性：
# val (值)：儲存節點的數值
# next (指標)：指向下一個節點，若為 None，表示這是最後一個節點

# cur = dummy 的主要目的是 保留 dummy 作為鏈結串列的頭節點，而 cur 作為指標來操作和延長鏈結串列。如果直接使用 dummy，會影響 dummy 的位置，導致最後無法正確返回結果

# cur.next = val  # ❌ 這是錯誤的，因為 val 是數字，不是 ListNode


        
