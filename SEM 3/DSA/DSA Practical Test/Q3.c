#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node* next;
    struct Node* prev;
};

struct Node* head = NULL;

void create(int data) 
{
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->next = NULL;
    new_node->prev = NULL;
    head = new_node;
}

void insert_at_beginning(int data) 
{
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->next = head;
    new_node->prev = NULL;

    if (head != NULL)
    {
        head->prev = new_node;
    }
    head = new_node;
}

void insert_at_end(int data) 
{
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->next = NULL;

    if (head == NULL)
    {
        new_node->prev = NULL;
        head = new_node;
        return;
    }

    struct Node* last = head;
    while (last->next != NULL)
    {
        last = last->next;
    }
    last->next = new_node;
    new_node->prev = last;
}

void insert_at_location(int data, int position) 
{
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;

    if (position == 0)
    {
        insert_at_beginning(data);
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
    new_node->prev = current;

    if (current->next != NULL)
    {
        current->next->prev = new_node;
    }
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

    if (head != NULL)
    {
        head->prev = NULL;
    }
    free(temp);
}

void delete_at_end() 
{
    if (head == NULL)
    {
        printf("List is empty.\n");
        return;
    }

    struct Node* last = head;
    if (last->next == NULL)
    {
        free(last);
        head = NULL;
        return;
    }

    while (last->next != NULL)
    {
        last = last->next;
    }
    last->prev->next = NULL;
    free(last);
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
    for (int i = 0; i < position && current != NULL; i++)
    {
        current = current->next;
    }

    if (current == NULL)
    {
        printf("Position out of bounds.\n");
        return;
    }

    if (current->prev != NULL)
    {
        current->prev->next = current->next;
    }
    if (current->next != NULL)
    {
        current->next->prev = current->prev;
    }
    free(current);
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
        printf("%d <-> ", current->data);
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
    struct Node* current = head;
    struct Node* temp = NULL;

    while (current != NULL)
    {
        temp = current->prev;
        current->prev = current->next;
        current->next = temp;
        current = temp;
    }

    if (temp != NULL)
    {
        head = temp->prev;
    }
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
                if (position != -1)
                {
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
