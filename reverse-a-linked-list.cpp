Node *Append(Node *last, Node *x) {
    last->next = x;
    return x;
}

Node* Reverse(Node *head)
{
    std::stack<Node *> s;
    
    while (head) {
        s.push(head);
        head = head->next;
    }
    
    head = NULL;
    Node *x = NULL, *last = NULL;
    
    if (!s.empty()) {
        head = (last = s.top());
        s.pop();
    }
    
    while (!s.empty()) {
        x = s.top(); s.pop();
        x->next = NULL;
        last->next = x;
        last = last->next;
    }
    
    return head;
}
