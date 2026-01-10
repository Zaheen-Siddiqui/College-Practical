#include <stdio.h>

int f = -1;
int r = -1;
int queue[5];

void enqueue_AT_rear(int x)
{
    if(f==(r+1)%5)
        printf("queue is full\n");
    else if (f == -1 && r == -1)
    {
        f++;
        r++;
        queue[r]=x;
    }
    else 
    {
        r=(r+1)%5;
        queue[r]=x;
    }
}

void enqueue_AT_front(int x)
{
    if(f==(r+1)%5)
        printf("queue is full\n");
    else if (f == -1 && r == -1)
    {
        f++;
        r++;
        queue[f]=x;
    }
    else 
    {
        f=(4+f)%5;
        queue[f]=x;
    }
}

void dequeue_AT_rear()
{
    if(f == -1 && r == -1)
        printf("queue is empty\n");
    else if(f==r)
    {
        f=-1;
        r=-1;
    }
    else
    {
        r=(4+r)%5;
    }
}

void dequeue_AT_front()
{
    if(f == -1 && r == -1)
        printf("queue is empty\n");
    else if(f==r)
    {
        f=-1;
        r=-1;
    }
    else
    {
        f=(f+1)%5;
    }
}

void display()
{
    if(f == -1 && r == -1)
    {
        printf("queue is empty\n");
    }
    else
    {
        for(int i = f; i!=r; i=(i+1)%5)
        {
            printf("%d\n",queue[i]);
        }
        printf("%d\n",queue[r]);
    }
}

void main()
{
    int a,n=0,boopon;

    while(n!=1)
    {
        printf("Enter \n1 for enqueue at rear \n2 for enqueue at front \n3 for dequeue at rear \n4 for dequeue at front \n5 for display \n6 for Exiting ");
        scanf("%d",&a);

        switch(a)
        {
            case 1:
                printf("Enter the value to be entered ");
                scanf("%d",&boopon);
                enqueue_AT_rear(boopon);
                break;

            case 2:
                printf("Enter the value to be entered ");
                scanf("%d",&boopon);
                enqueue_AT_front(boopon);
                break;

            case 3:
                dequeue_AT_rear();
                break;  

            case 4:
                dequeue_AT_front();
                break;

            case 5:
                display();
                break;

            case 6:
                n=1;
                break;

            default:
                printf("Invalid Input\n");
        }
    }
}
