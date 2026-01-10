#include<stdio.h>

void main()
{
    int n,find; 

    printf("Enter the number of elements\n");
    scanf("%d",&n);

    int a[n];

    for (int i = 0; i<n; i++)
    {
        printf("Enter element number: %d\n",i+1);
        scanf("%d",&a[i]);
    }

    printf("Enter the element to find\n");
    scanf("%d",&find);

    int mid,half;
    int i = 0;

    half = n-1/2;
    mid = a[half];

    int ct = 0;

    while (ct!=1)
    {
        if(mid == find)
        {
            printf("Entered element is present\n");
            ct = 1;
        }
        else
        {   
            if(find>mid)
            {
                i = half;
                half = (i+n)/2;
                mid = a[half];
            }
            else
            {
                n = half;
                half = (i+n)/2;
                mid = a[half];
            }

            if(half == i)
                break;
        }
    }

    if (ct != 1)
    {
        printf("Entered element is not present\n");
    }
}
