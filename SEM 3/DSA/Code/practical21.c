#include <stdio.h>

void bubbleSort(int a[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (a[j] > a[j + 1])
            {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }
}

void selectionSort(int a[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        int minIndex = i;

        for (int j = i + 1; j < n; j++)
        {
            if (a[j] < a[minIndex])
                minIndex = j;
        }

        if (minIndex != i)
        {
            int temp = a[i];
            a[i] = a[minIndex];
            a[minIndex] = temp;
        }
    }
}

int main()
{
    int n, choice;

    printf("Enter the number of elements:\n");
    scanf("%d", &n);

    int a[n];

    for (int i = 0; i < n; i++)
    {
        printf("Enter element number %d:\n", i + 1);
        scanf("%d", &a[i]);
    }

    printf("\nChoose Sorting Method:\n");
    printf("1. Bubble Sort\n");
    printf("2. Selection Sort\n");
    printf("Enter choice: ");
    scanf("%d", &choice);

    if (choice == 1)
        bubbleSort(a, n);
    else if (choice == 2)
        selectionSort(a, n);
    else
    {
        printf("Invalid choice!\n");
        return 0;
    }

    printf("\nSorted Elements:\n");
    for (int i = 0; i < n; i++)
        printf("Element number %d = %d\n", i + 1, a[i]);

    return 0;
}
