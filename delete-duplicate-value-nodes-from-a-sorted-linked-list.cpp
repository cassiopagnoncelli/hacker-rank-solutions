/*
  Remove all duplicate elements from a sorted linked list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* RemoveDuplicates(Node *head)
{
   if (!head)
       return NULL;
   
   if (!head->next)
       return head;
    
    if (head->data == head->next->data) {
        head->next = head->next->next;
        RemoveDuplicates(head);
    } else
        RemoveDuplicates(head->next);
    
    return head;
}
