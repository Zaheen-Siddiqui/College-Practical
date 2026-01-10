#include <stdio.h>
#include <stdlib.h>

struct node 
{
    int info;
    struct node *next;
};

struct node *list = NULL;

struct node* getnode(void) 
{
    return (struct node *)malloc(sizeof(struct node));
}

void freenode(struct node *p)
{
    free(p);
}

void display() 
{
    struct node *print = list;
    int i = 1;

    while (print != NULL) 
    {
        printf("%d: %d\n", i, print->info);
        print = print->next;
        i++;
    }
}

void enqueue(int x) 
{
    struct node *nn = getnode();
    nn->info = x;
    nn->next = list;
    list = nn;
    display();
}

void dequeue() 
{
    if (list == NULL) 
    {
        printf("List is empty\n");
        return;
    }

    struct node *dn = list;
    struct node *prev = NULL;

    while (dn->next != NULL) 
    {
        prev = dn;
        dn = dn->next;
    }

    if (prev == NULL)
    {
        list = NULL;
    } 
    else 
    {
        prev->next = NULL;
    }

    freenode(dn);
    display();
}

void main() 
{
    int a, n, l = 0;    

    while (l != 1)
    {
        printf("Enter \n1 for enqueue \n2 for dequeue \n3 for exiting\n");
        scanf("%d", &a);

        switch (a) 
        {
            case 1:
                printf("Enter number to be enqueued\n");
                scanf("%d", &n);
                enqueue(n);
                break;

            case 2:
                dequeue();
                break;

            case 3:
                l = 1;
                printf("End of program\n");
                break;

            default:
                printf("Incorrect input\n");
                break;
        }
    }
}
