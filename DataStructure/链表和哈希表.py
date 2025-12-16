#哈希表，直接寻址表，key为k的元素放入h（k）=k%n取余,n为长度，余数为值的位置，如果出现哈希冲突
#使用线性探查法：如果位置i被占用，找i+1.....
#二次探查：i+1，i-1，i-4，i+4，i-9.....
#二度哈希：使用多个哈希函数
#拉链法：发生冲突后，冲突的元素加到该位置链表的后面

#链表
class Node:
    def __init__(self,item):
        self.item=item
        self.next=None
#头插法，尾插法
def createListnode(li):
    head=Node(li[0])
    for element in li[1:]:
        node=Node(element)
        node.next=head
        head=node
    return head#头插法将原列表倒置

def print(lk):
    while lk:
        print(lk.item,end=",")
        lk=lk.next

def creatlistNode2(li):
    head=Node(li[0])
    tail=head
    for element in li[1:]:
        node=Node(element)
        tail.next=node
        tail=node
    return head
#链表的插入和删除
#双链表（一个结点具备两个指针）
# 将p插入两个结点之间：
# p.next=curNode.next
# curNode.next.prior=p
# p.prior=curNode
# curNode.next=p
