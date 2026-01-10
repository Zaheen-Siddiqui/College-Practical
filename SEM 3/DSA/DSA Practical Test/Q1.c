#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node* next;
};

struct Node* head = NULL;

void create(int data)
{
    head = (struct Node*)malloc(sizeof(struct Node));
    head->data = data;
    head->next = NULL;
}

void insert_at_beginning(int data)
{
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->next = head;
    head = new_node;
}

void insert_at_end(int data){


    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->next = NULL;

    if (head == NULL)
    {
        head = new_node;
        return;
    }
    struct Node* last = head;
    while (last->next != NULL)
    {
        last = last->next;
    }
    last->next = new_node;
}

void insert_at_location(int data, int position)
{
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;

    if (position == 0)
    {
        new_node->next = head;
        head = new_node;
        return;
    }

    struct Node* current = head;
    for (int i = 0; i < position - 1 && current != NULL; i++)
    {
        current = current->next;
    }
    if (current == NULL)
    {
        printf("Position out of bounds.\n");
        free(new_node);
        return; 
    }
    new_node->next = current->next;
    current->next = new_node;
}

void delete_at_beginning()
{
    if (head == NULL)
    {
        printf("List is empty.\n");
        return;
    }
    struct Node* temp = head;
    head = head->next;
    free(temp);
}

void delete_at_end()
{
    if (head == NULL)
    {
        printf("List is empty.\n");
        return;
    }
    if (head->next == NULL)
    {
        free(head);
        head = NULL;
        return;
    }
    struct Node* second_last = head;
    while (second_last->next->next != NULL)
    {
        second_last = second_last->next;
    }
    free(second_last->next);
    second_last->next = NULL;
}

void delete_at_location(int position)
{
    if (head == NULL)
    {
        printf("List is empty.\n");
        return;
    }
    if (position == 0)
    {
        delete_at_beginning();
        return;
    }
    struct Node* current = head;
    for (int i = 0; i < position - 1 && current != NULL; i++)
    {
        current = current->next;
    }
    if (current == NULL || current->next == NULL)
    {
        printf("Position out of bounds.\n");
        return;
    }
    struct Node* temp = current->next;
    current->next = temp->next;
    free(temp);
}

void display()
{
    struct Node* current = head;
    if (current == NULL)
    {
        printf("List is empty.\n");
        return;
    }
    while (current != NULL)
    {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int search(int key)
{
    struct Node* current = head;
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

int count()
{
    struct Node* current = head;
    int count = 0;
    while (current != NULL)
    {
        count++;
        current = current->next;
    }
    return count;
}

void reverse()
{
    struct Node *prev = NULL, *current = head, *next = NULL;
    while (current != NULL)
    {
        next = current->next;   
        current->next = prev;
        prev = current;
        current = next;
    }
    head = prev;
}

void main()
{
    int choice, data, position;

    while (1)
    {
        printf("\nMenu:\n"
               "1. CREATE\n"
               "2. INSERT AT BEGINNING\n"
               "3. INSERT AT END\n"
               "4. INSERT AT LOCATION\n"
               "5. DELETE AT BEGINNING\n"
               "6. DELETE AT END\n"
               "7. DELETE AT LOCATION\n"
               "8. DISPLAY\n"
               "9. SEARCH\n"
               "10. COUNT\n"
               "11. REVERSE\n"
               "12. EXIT\n");
        
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        switch (choice)
        {
            case 1:
                printf("Enter data: ");
                scanf("%d", &data);
                create(data);
                break;
            case 2:
                printf("Enter data: ");
                scanf("%d", &data);
                insert_at_beginning(data);
                break;
            case 3:
                printf("Enter data: ");
                scanf("%d", &data);
                insert_at_end(data);
                break;
            case 4:
                printf("Enter data: ");
                scanf("%d", &data);
                printf("Enter position: ");
                scanf("%d", &position);
                insert_at_location(data, position);
                break;
            case 5:
                delete_at_beginning();
                break;
            case 6:
                delete_at_end();
                break;
            case 7:
                printf("Enter position: ");
                scanf("%d", &position);
                delete_at_location(position);
                break;
            case 8:
                display();
                break;
            case 9:
                printf("Enter key to search: ");
                scanf("%d", &data);
                position = search(data);
                if (position != -1){
                    printf("Element found at position: %d\n", position);
                } else{
                    printf("Element not found.\n");
                }
                break;
            case 10:
                printf("Total elements in the list: %d\n", count());
                break;
            case 11:
                reverse();
                printf("List reversed.\n");
                break;
            case 12:
                exit(0);
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }
}
