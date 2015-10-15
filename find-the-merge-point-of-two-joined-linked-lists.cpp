#include <stack>

/*
   Find merge point of two linked lists
   Node is defined as
   struct Node
   {
       int data;
       Node* next;
   }
*/
int FindMergeNode(Node *headA, Node *headB)
{
    stack<Node *> A, B;
    Node *pA = headA, *pB = headB;
    
    while (pA) {
        A.push(pA);
        pA = pA->next;
    }
    
    while (pB) {
        B.push(pB);
        pB = pB->next;
    }
    
    int last = 0;
    while (!A.empty() && !B.empty()) {
        if (A.top()->data == B.top()->data) {
            last = A.top()->data;
            A.pop();
            B.pop();
        } else {
            return last;
        }
    }
    
    return 0;
}
