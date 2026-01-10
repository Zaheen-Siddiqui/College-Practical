#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

void reverse_string(const char* str) 
{
    struct Stack s;
    initialize(&s);
    
    for (int i = 0; str[i] != '\0'; i++) 
    {
        push(&s, str[i]);
    }

    printf("Reversed string: ");
    while (!is_empty(&s)) 
    {
        printf("%c", pop(&s));
    }
    printf("\n");
}

void main() 
{
    char str[100];

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    
    str[strcspn(str, "\n")] = '\0';

    reverse_string(str);
}
