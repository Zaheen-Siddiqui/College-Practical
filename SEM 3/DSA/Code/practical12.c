#include <stdio.h>

int f = -1;
int r = -1;
int queue[5];

void enqueue(int x)
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

void dequeue()
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
        printf("Enter \n1 for enqueue \n2 for dequeue \n3 for display \n4 for Exiting ");
        scanf("%d",&a);

        switch(a)
        {
            case 1:
                printf("Enter the value to be entered ");
                scanf("%d",&boopon);
                enqueue(boopon);
                break;

            case 2:
                dequeue();
                break;

            case 3:
                display();
                break;

            case 4:
                n=1;
                break;

            default:
                printf("Invalid Input\n");
        }
    }
}
