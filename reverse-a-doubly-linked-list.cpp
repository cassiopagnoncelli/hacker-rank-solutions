#include <stack>

/*
   Reverse a doubly linked list, input list may also be empty
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev;
   }
*/
void swap(Node *x) {
    Node *tmp;
    tmp = x->next;
    x->next = x->prev;
    x->prev = tmp;
}

Node* Reverse(Node* head)
{
    if (!head) return NULL;
    
    stack<Node *> s;
    while (head) {
        s.push(head);
        head = head->next;
    }
    
    Node *ret = s.top();
    while (!s.empty()) {
        swap(s.top());
        s.pop();
    }
    
    return ret;
}

