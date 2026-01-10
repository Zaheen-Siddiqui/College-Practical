#include<stdio.h>

int top = -1;
int stack[5];

void push(int x)
{
    if(top==4)
        printf("Stack Overflow\n");
    else 
    {
        top++;
        stack[top]=x;
    }
}

void pop()
{
    if(top==-1)
        printf("Stack Underflow\n");
    else
    {
        top--;
    }
}

void display()
{
    if(top==-1)
        printf("Stack Underflow\n");

    for(int i = top; i>=0; i--)
    {
        printf("%d\n",stack[i]);
    }
}

void main()
{
    int a,n=0,boopon;

    while(n!=1)
    {
        printf("Enter 1 for push, 2 for pop, 3 for display, 4 for Exiting ");
        scanf("%d",&a);

        switch(a)
        {
            case 1:
                printf("Enter the value to be pushed ");
                scanf("%d",&boopon);
                push(boopon);
                break;

            case 2:
                pop();
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
