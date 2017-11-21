#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "bt3"

'''
Find the mth-to-last element of a linked list.
One option is having two pointers, separated by m. P1 start at the head 
(p1 = self.head) and p2 is m-behind pointer, which is created when p1 is at m.
When p1 reach the end, p2 is the node.
'''

from linked_list_fifo import LinkedListFIFO


class LinkedListFIFO_find_kth(LinkedListFIFO):
    def find_kth_to_last(self, k):
        p1, p2 = self.head, self.head
        i = 0
        while p1:
            if i > k:
                try:
                    p2 = p2.pointer
                except:
                    break
            p1 = p1.pointer
            i += 1
        return p2.value


if __name__ == '__main__':
    ll = LinkedListFIFO_find_kth()
    for i in range(1, 11):
        ll.addNode(i)
    print('The Linked List:')
    print(ll.printList())
    k = 3
    k_from_last = ll.find_kth_to_last(k)
    print("The %dth element to the last of the LL of size %d is %d" % (k, ll.length, k_from_last))
