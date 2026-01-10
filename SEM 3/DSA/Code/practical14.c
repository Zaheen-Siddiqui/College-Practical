#include <stdio.h>
#include <stdlib.h>

struct node 
{
    int info;
    struct node *next;
};

struct node *list = NULL;

struct node* getnode() 
{
    return (struct node *) malloc(sizeof(struct node));
}

void freenode(struct node* p) 
{
    free(p);
}

void insert_at_beg(int x) 
{
    struct node *nn = getnode();  
    nn->info = x;
    nn->next = list;
    list = nn;
    display();
}

void insert_at_end(int x) 
{
    struct node *nn = getnode();  
    nn->info = x;
    nn->next = NULL;

    if (list == NULL) 
    {  
        list = nn;
    } 
    else 
    {
        struct node *temp = list;
        while (temp->next != NULL) 
        {
            temp = temp->next;
        }
        temp->next = nn;
    }
    display();
}

void insert_at_anypoint(int x, int p) 
{
    struct node *nn = getnode();  
    nn->info = x;
    nn->next = NULL;

    if (p == 1) 
    {  
        nn->next = list;
        list = nn;
    } 
    else 
    {
        struct node *temp = list;
        for (int i = 1; i < p - 1 && temp != NULL; i++) 
        {
            temp = temp->next;
        }
        if (temp != NULL)
        {
            nn->next = temp->next;
            temp->next = nn;
        } 
        else 
        {
            printf("Position out of bounds\n");
            freenode(nn);  
        }
    }
    display();
}

void delete_at_beg() 
{
    if (list == NULL) 
    {
        printf("List is empty\n");
        return;
    }
    struct node *dn = list;
    list = dn->next;
    freenode(dn);
    display();
}

void delete_at_end() 
{
    if (list == NULL) 
    {
        printf("List is empty\n");
        return;
    }
    struct node *dn = list;
    struct node *temp = NULL;

    if (dn->next == NULL)
    {  
        free(dn);
        list = NULL;
    } 
    else 
    {
        while (dn->next != NULL) 
        {
            temp = dn;
            dn = dn->next;
        }
        temp->next = NULL;
        freenode(dn);
    }
    display();
}

void delete_at_anypoint(int p) 
{
    if (list == NULL) 
    {
        printf("List is empty\n");
        return;
    }
    if (p == 1) 
    {  
        delete_at_beg();
        return;
    }

    struct node *temp = list;
    for (int i = 1; i < p - 1 && temp != NULL; i++) 
    {
        temp = temp->next;
    }

    if (temp != NULL && temp->next != NULL) 
    {
        struct node *dn = temp->next;
        temp->next = dn->next;
        freenode(dn);
    } 
    else 
    {
        printf("Position out of bounds\n");
    }
    display();
}

void display() 
{
    struct node *print = list;

    if (print == NULL)
    {
        printf("List is empty\n");
        return;
    }

    while (print != NULL) 
    {
        printf("%d ", print->info);
        print = print->next;
    }
    printf("\n");
}

void main() 
{
    int a, n = 0, boopon, pos;

    while (n != 1) 
    {
        printf("Enter \n1 for insert at beginning \n2 for insert at end \n3 for insert at any point \n4 for delete at beginning \n5 for delete at end \n6 for delete at any point \n7 for display \n8 for exiting: ");
        scanf("%d", &a);

        switch (a) 
        {
            case 1:
                printf("Enter the value to be entered: ");
                scanf("%d", &boopon);
                insert_at_beg(boopon);
                break;

            case 2:
                printf("Enter the value to be entered: ");
                scanf("%d", &boopon);
                insert_at_end(boopon);
                break;

            case 3:
                printf("Enter the value to be entered and the position: ");
                scanf("%d%d", &boopon, &pos);
                insert_at_anypoint(boopon, pos);
                break;

            case 4:
                delete_at_beg();
                break;

            case 5:
                delete_at_end();
                break;

            case 6:
                printf("Enter the position to delete: ");
                scanf("%d", &pos);
                delete_at_anypoint(pos);
                break;

            case 7:
                display();
                break;

            case 8:
                n = 1;
                break;

            default:
                printf("Invalid Input\n");
        }
    }
}
