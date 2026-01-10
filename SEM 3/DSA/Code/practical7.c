#include<stdio.h>

void main()
{
    int a[5],n[5],t=0;
    printf("Enter the 5 elemnts of first array ");
    for (int i=0; i<5; i++)
    {
        scanf("%d",&a[i]);
    }
    printf("Enter the 5 elemnts of second array ");
    for (int i=0; i<5; i++)
    {
        scanf("%d",&n[i]);
    }
    for (int i=0; i<5; i++)
    {
        if(a[i]==n[i])
        {
            t++;
        }
    }
    if(t==5)
        printf("1");
    else
        printf("0");
}
