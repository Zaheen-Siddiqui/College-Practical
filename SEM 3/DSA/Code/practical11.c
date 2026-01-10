#include<stdio.h>

int f = -1;
int r = -1;
int queue[5];

void enqueue(int x)
{
    if(r==4)
        printf("Queue is full\n");
    else if (f == -1 && r == -1)
    {
        f++;
        r++;
        queue[r]=x;
    }
    else 
    {
        r++;
        queue[r]=x;
    }
}

void dequeue()
{
    if(f == -1 && r == -1)
        printf("Queue is empty\n");
    else if(f==r)
    {
        f=-1;
        r=-1;
    }
    else
    {
        f++;
    }
}

void display()
{
    if(f != -1 && r != -1)
    {
        for(int i = f; i<=r; i++)
        {
            printf("%d\n",queue[i]);
        }
    }
    else
    {
        printf("Queue is empty\n");
    }
}

void main()
{
    int a,n=0,boopon;

    while(n!=1)
    {
        printf("Enter 1 for enqueue, 2 for dequeue, 3 for display, 4 for Exiting ");
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
