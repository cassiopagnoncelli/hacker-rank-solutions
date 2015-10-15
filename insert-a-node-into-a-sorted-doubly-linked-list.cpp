/*
    Insert Node in a doubly sorted linked list 
    After each insertion, the list should be sorted
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev
   }
*/
Node * NewNode(int data)
{
    Node *n = new Node;
    n->data = data;
    return n;
}

void P(Node *h) {
    Node *p = h;
    while (p->prev)
        p = p->prev;
    
    while (p) {
        cout << p->data << " ";
        p = p->next;
    }
    
    cout << endl;
}

Node* SortedInsert(Node *head,int data)
{
    Node 
        *left = NULL,
        *right = NULL,
        *p = head,
        *n = NewNode(data);
    
    while (p) {
        if (data > p->data) {
            left = p;
            right = p->next;
            p = p->next;
        } else {
            left = p->prev;
            right = p;
            break;
        }
    }
    
    // Connect neighbours.
    n->prev = left;
    n->next = right;
    if (left) left->next = n;
    if (right) right->prev = n;
    
    // Head.
    if (!head) head = n;
    if (head->prev) head = head->prev;
    
    //P(head);
    return head;
}
