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
    new_node->next = new_node;
    new_node->prev = new_node;
    head = new_node;
}

void insert_at_beginning(int data) 
{
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;

    if (head == NULL) 
    {
        create(data);
        return;
    }

    new_node->next = head;
    new_node->prev = head->prev;
    head->prev->next = new_node;
    head->prev = new_node;
    head = new_node;
}

void insert_at_end(int data) 
{
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;

    if (head == NULL) 
    {
        create(data);
        return;
    }

    new_node->next = head;
    new_node->prev = head->prev;
    head->prev->next = new_node;
    head->prev = new_node;
}

void insert_at_location(int data, int position) 
{
    if (position == 0) 
    {
        insert_at_beginning(data);
        return;
    }

    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;

    struct Node* current = head;
    for (int i = 0; i < position - 1 && current->next != head; i++) 
    {
        current = current->next;
    }

    new_node->next = current->next;
    new_node->prev = current;

    if (current->next != head) 
    {
        current->next->prev = new_node;
    }
    current->next = new_node;

    if (new_node->next == head) 
    {
        head->prev = new_node;
    }
}

void delete_at_beginning() 
{
    if (head == NULL) 
    {
        printf("List is empty.\n");
        return;
    }

    struct Node* temp = head;

    if (head->next == head) 
    {
        head = NULL;
    }
    else 
    {
        head->prev->next = head->next;
        head->next->prev = head->prev;
        head = head->next;
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

    struct Node* last = head->prev;

    if (last == head) 
    {
        free(head);
        head = NULL;
        return;
    }

    last->prev->next = head;
    head->prev = last->prev;
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
    int i;
    for (i = 0; i < position && current->next != head; i++) 
    {
        current = current->next;
    }

    if (current->next == head && i != position) 
    {
        printf("Position out of bounds.\n");
        return;
    }

    if (current->next != head) 
    {
        current->prev->next = current->next;
        current->next->prev = current->prev;
    }
    else 
    {
        head->prev = current->prev;
        current->prev->next = head;
    }

    free(current);
}

void display() 
{
    if (head == NULL) 
    {
        printf("List is empty.\n");
        return;
    }

    struct Node* current = head;
    do 
    {
        printf("%d <-> ", current->data);
        current = current->next;
    } while (current != head);
    printf("NULL\n");
}

int search(int key) 
{
    struct Node* current = head;
    int position = 0;

    if (head == NULL) 
    {
        return -1;
    }

    do 
    {
        if (current->data == key) 
        {
            return position;
        }
        current = current->next;
        position++;
    } while (current != head);
    
    return -1;
}

int count() 
{
    struct Node* current = head;
    int count = 0;

    if (head == NULL) 
    {
        return count;
    }

    do 
    {
        count++;
        current = current->next;
    } while (current != head);
    
    return count;
}

void reverse() 
{
    struct Node* current = head;
    struct Node* temp = NULL;

    if (head == NULL) 
    {
        printf("List is empty.\n");
        return;
    }

    do 
    {
        temp = current->next;
        current->next = current->prev;
        current->prev = temp;
        current = temp;
    } while (current != head);

    head = head->prev;  
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
                }
                else 
                {
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
