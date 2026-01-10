#include <stdio.h>
#include <stdlib.h>

struct Node 
{
    char data;
    struct Node* next;
};

struct Stack 
{
    struct Node* top;
};

void initialize(struct Stack* s) 
{
    s->top = NULL;
}

int is_empty(struct Stack* s) 
{
    return s->top == NULL;
}

void push(struct Stack* s, char data) 
{
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->next = s->top;
    s->top = new_node;
}

char pop(struct Stack* s) 
{
    if (is_empty(s)) 
    {
        return '\0'; 
    }
    struct Node* temp = s->top;
    char popped_data = temp->data;
    s->top = s->top->next;
    free(temp);
    return popped_data;
}

int is_palindrome(const char* num) 
{
    struct Stack s;
    initialize(&s);
    
    for (int i = 0; num[i] != '\0'; i++) 
    {
        push(&s, num[i]);
    }

    for (int i = 0; num[i] != '\0'; i++) 
    {
        if (num[i] != pop(&s)) 
        {
            return 0; 
        }
    }
    
    return 1; 
}

void main() 
{
    char num[100];

    printf("Enter a number: ");
    scanf("%s", num);

    if (is_palindrome(num)) 
    {
        printf("%s is a palindrome.\n", num);
    } 
    else 
    {
        printf("%s is not a palindrome.\n", num);
    }
}
