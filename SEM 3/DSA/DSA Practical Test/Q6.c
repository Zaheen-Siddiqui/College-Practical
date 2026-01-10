#include <stdio.h>
#include <stdlib.h>

struct Node 
{
    int data;
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

void push(struct Stack* s, int data) 
{
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->next = s->top;
    s->top = new_node;
    printf("%d pushed to stack\n", data);
}

int pop(struct Stack* s) 
{
    if (is_empty(s)) 
    {
        printf("Stack is empty. Cannot pop\n");
        return -1; 
    }
    struct Node* temp = s->top;
    int popped_data = temp->data;
    s->top = s->top->next;
    free(temp);
    return popped_data;
}

void display(struct Stack* s) 
{
    if (is_empty(s)) 
    {
        printf("Stack is empty.\n");
        return;
    }
    struct Node* current = s->top;
    printf("Stack elements:\n");
    while (current != NULL) 
    {
        printf("%d\n", current->data);
        current = current->next;
    }
}

int search(struct Stack* s, int key) 
{
    struct Node* current = s->top;
    int position = 0;

    while (current != NULL) 
    {
        if (current->data == key) 
        {
            return position;
        }
        current = current->next;
        position++;
    }
    
    return -1; 
}

void main() 
{
    struct Stack s;
    initialize(&s);
    
    int choice, data;

    while (1) 
    {
        printf("\nMenu:\n"
               "1. PUSH\n"
               "2. POP\n"
               "3. DISPLAY\n"
               "4. SEARCH\n"
               "5. EXIT\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) 
        {
            case 1:
                printf("Enter data to push: ");
                scanf("%d", &data);
                push(&s, data);
                break;
            case 2:
                data = pop(&s);
                if (data != -1) 
                {
                    printf("%d popped from stack\n", data);
                }
                break;
            case 3:
                display(&s);
                break;
            case 4:
                printf("Enter data to search: ");
                scanf("%d", &data);
                int position = search(&s, data);
                if (position != -1) 
                {
                    printf("%d found at position: %d\n", data, position);
                } 
                else 
                {
                    printf("%d not found in stack.\n", data);
                }
                break;
            case 5:
                exit(0);
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }
}
