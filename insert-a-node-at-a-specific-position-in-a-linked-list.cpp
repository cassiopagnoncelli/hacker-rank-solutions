/*
  Insert Node at a given position in a linked list 
  head can be NULL 
  First element in the linked list is at position 0
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node *NewNode(int data, Node *next) {
    Node *n = new Node;
    n->data = data;
    n->next = next;
    return n;
}

Node* InsertNth(Node *head, int data, int position)
{
    if (position == 0)
        return NewNode(data, head);
    
    if (position == 1) {
        head->next = NewNode(data, head->next);
        return head;
    }
    
    InsertNth(head->next, data, position - 1);
    return head;
}
