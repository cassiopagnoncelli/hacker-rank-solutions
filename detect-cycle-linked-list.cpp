/*
  Detect loop in a linked list 
  List could be empty also
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
int HasCycle(Node* head)
{
    if (!head)
        return 0;
    
    Node *p = head, *q = head->next;
    while (p && q)
        if (p == q)
            return 1;
        else {
            p = p->next;
            q = q->next ? q->next->next : q->next;
        }
    
    return 0;
}

