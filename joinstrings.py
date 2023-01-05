class Node:                                             #there is no way to solve this quickly in Python without a LinkedList end of story
    def __init__(self, value, next=None):               #initialization statement (value given and default next to nothing)
        self.value = value
        self.next = next

class LinkedList:                                       #overarching linkedlist class to hold the head and tail of the full linkedlist for operations
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        
n = int(input())                                        #read in number of words I will receive
if n == 1: print(input())                               #if it is 1 print the word I get and be done
else:
    groups = []                                         #list of linkedlists for each number code starting with 1 having just word 1, 2 having just word 2 etc
    for i in range(n):
        groups.append(LinkedList(Node(input())))
    for j in range(n-2):                                #for every number combination given but the last
        a, b = input().split()                          #read in the numbers given
        a, b = int(a), int(b)                           #convert them to usable integers
        groups[a-1].tail.next = groups[b-1].head        #add the linked list of the second number to the end of the linked list of the first number to make a large chain
        groups[a-1].tail = groups[b-1].tail             #reset the tail to the new tail of the linked list
        groups[b-1] = LinkedList()                      #make the second number be empty
    a, b = input().split()                              #read in the last number pair
    a, b = int(a), int(b)                               #convert them to integers
    temp = groups[a-1].head                             #set a pointer to traverse through linked list a
    while temp != None:
        print(temp.value, end='')                       #print the values without spaces until you reach the end of the linked list
        temp = temp.next
    temp = groups[b-1].head                             #set a pointer to traverse through linked list b
    while temp != None:
        print(temp.value, end='')                       #print the values without spaces until you reach the end of the linked list
        temp = temp.next
        