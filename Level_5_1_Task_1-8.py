from Level_5_1 import Node, LinkedList

def Equal_list(s1=LinkedList, s2=LinkedList): # 1.8. Напишите функцию, которая получает на вход два связанных списка, состоящие из целых значений, 
                        # и если их длины равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков. 
    len1 = s1.len()
    len2 = s2.len()
    s3 = LinkedList()
    if len1 == len2:
        s1_node = s1.head
        s2_node = s2.head
        for i in range(len1):
            s3.add_in_tail(Node(s1_node.value + s2_node.value))
            s1_node = s1_node.next
            s2_node = s2_node.next
    return s3

s1_list = LinkedList()
for i in range(1, 12):
    s1_list.add_in_tail(Node(i))

s2_list = LinkedList()
for i in range(1, 11):
    s2_list.add_in_tail(Node(i))

s3 = Equal_list(s1_list, s2_list)
s3.print_all_nodes()