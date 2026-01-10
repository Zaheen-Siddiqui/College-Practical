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
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->next = new_node;

    if (head == NULL)
    {
        head = new_node;
    } else{
        struct Node* temp = head;
        while (temp->next != head)
        {
            temp = temp->next;
        }
        temp->next = new_node;
        new_node->next = head;
    }
}

void insert_at_beginning(int data)
{
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;

    if (head == NULL)
    {
        head = new_node;
        new_node->next = new_node;
    } else
    {
        struct Node* temp = head;
        while (temp->next != head)
        {
            temp = temp->next;
        }
        new_node->next = head;
        temp->next = new_node;
        head = new_node;
    }
}

void insert_at_end(int data)
{
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;

    if (head == NULL)
    {
        head = new_node;
        new_node->next = new_node;
    } else{
        struct Node* temp = head;
        while (temp->next != head)
        {
            temp = temp->next;
        }
        temp->next = new_node;
        new_node->next = head;
    }
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

    struct Node* temp = head;
    int i;
    for (i = 0; i < position - 1 && temp->next != head; i++)
    {
        temp = temp->next;
    }

    if (temp->next == head && i < position - 1)
    {
        printf("Position out of bounds.\n");
        free(new_node);
        return;
    }

    new_node->next = temp->next;
    temp->next = new_node;
}

void delete_at_beginning()
{
    if (head == NULL)
    {
        printf("List is empty.\n");
        return;
    }

    struct Node* temp = head;
    if (temp->next == head)
    {
        free(temp);
        head = NULL;
    } else{
        struct Node* last = head;
        while (last->next != head)
        {
            last = last->next;
        }
        last->next = head->next;
        head = head->next;
        free(temp);
    }
}

void delete_at_end()
{
    if (head == NULL)
    {
        printf("List is empty.\n");
        return;
    }

    struct Node* temp = head;
    if (temp->next == head)
    {
        free(temp);
        head = NULL;
        return;
    }

    struct Node* second_last = head;
    while (second_last->next->next != head)
    {
        second_last = second_last->next;
    }
    free(second_last->next);
    second_last->next = head;
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

    struct Node* temp = head;
    int i;
    for (i = 0; i < position - 1 && temp->next != head; i++)
    {
        temp = temp->next;
    }

    if (temp->next == head && i < position - 1)
    {
        printf("Position out of bounds.\n");
        return;
    }

    struct Node* to_delete = temp->next;
    temp->next = to_delete->next;
    free(to_delete);
}

void display()
{
    if (head == NULL)
    {
        printf("List is empty.\n");
        return;
    }

    struct Node* temp = head;
    do
    {
        printf("%d -> ", temp->data);
        temp = temp->next;
    } while (temp != head);
    printf("(back to head: %d)\n", head->data);
}

int search(int key)
{
    struct Node* temp = head;
    int position = 0;

    if (head == NULL) return -1;

    do
    {
        if (temp->data == key)
        {
            return position;
        }
        temp = temp->next;
        position++;
    } while (temp != head);
    return -1;
}

int count()
{
    struct Node* temp = head;
    int count = 0;

    if (head == NULL) return 0;

    do
    {
        count++;
        temp = temp->next;
    } while (temp != head);
    return count;
}

void reverse()
{
    if (head == NULL) return;

    struct Node *prev = NULL, *current = head, *next = NULL;
    struct Node* start = head;

    do
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    } while (current != start);

    head->next = prev;
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
