#include <queue>

/*
  Merge two sorted lists A and B as one linked list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* MergeLists(Node *headA, Node* headB)
{
    if (!headA) return headB;
    if (!headB) return headA;
    
    /* Alternatingly enqueue smaller elements first up to the end. */
    queue<Node *> q;
    while (headA && headB) {
        if (headA->data < headB->data) {
            q.push(headA);
            headA = headA->next;
        } else {
            q.push(headB);
            headB = headB->next;
        }
    }
    while (headA) {
        q.push(headA);
        headA = headA->next;
    }
    while (headB) {
        q.push(headB);
        headB = headB->next;
    }
    
    /* Construct list from the queue. */
    Node *head = q.front();
    head->next = NULL;
    q.pop();
    
    Node *last = head;
    while (!q.empty()) {
        last->next = q.front();
        last = last->next;
        last->next = NULL;
        q.pop();
    }
    
    return head;
}
