/* 
The structure of the node is

typedef struct node
{
    int freq;
    char data;
    node * left;
    node * right;
    
}node;

*/
void decode_huff(node * root, string s)
{
    char *str = strcpy((char *)calloc(1 << 20, sizeof(char)), s.c_str());
    node *r = root;
    for (int i=0; i<=strlen(str); i++) {
        if (r->data > 0) {
            cout << r->data;
            r = root;
        }
        
        if (str[i] == '0')
            r = r->left;
        else
            r = r->right;
    }
}

