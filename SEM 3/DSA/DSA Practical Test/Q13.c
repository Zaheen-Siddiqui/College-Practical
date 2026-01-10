#include <stdio.h>
#include <stdlib.h>

#define MAX 10

struct CircularQueue 
{
    int arr[MAX];
    int front;
    int rear;
};

void initialize(struct CircularQueue* q) 
{
    q->front = -1;
    q->rear = -1;
}

int is_full(struct CircularQueue* q) 
{
    return (q->rear + 1) % MAX == q->front;
}

int is_empty(struct CircularQueue* q) 
{
    return q->front == -1;
}

void enqueue(struct CircularQueue* q, int data) 
{
    if (is_full(q)) 
    {
        printf("Queue is full. Cannot enqueue %d\n", data);
        return;
    }

    if (is_empty(q)) 
    {
        q->front = 0;
    }
    q->rear = (q->rear + 1) % MAX;
    q->arr[q->rear] = data;
    printf("%d enqueued to queue\n", data);
}

int dequeue(struct CircularQueue* q) 
{
    if (is_empty(q)) 
    {
        printf("Queue is empty. Cannot dequeue\n");
        return -1; 
    }

    int data = q->arr[q->front];
    if (q->front == q->rear) 
    {
        q->front = -1; 
        q->rear = -1;
    } 
    else 
    {
        q->front = (q->front + 1) % MAX;
    }
    return data;
}

void display(struct CircularQueue* q) 
{
    if (is_empty(q)) 
    {
        printf("Queue is empty.\n");
        return;
    }

    printf("Queue elements:\n");
    int i = q->front;
    while (1) 
    {
        printf("%d ", q->arr[i]);
        if (i == q->rear) 
        {
            break;
        }
        i = (i + 1) % MAX;
    }
    printf("\n");
}

int count(struct CircularQueue* q) 
{
    if (is_empty(q)) 
    {
        return 0;
    }
    if (q->rear >= q->front) 
    {
        return q->rear - q->front + 1;
    }
    return (MAX - q->front + q->rear + 1);
}

void main() 
{
    struct CircularQueue q;
    initialize(&q);
    
    int choice, data;

    while (1) 
    {
        printf("\nMenu:\n"
               "1. ENQUEUE\n"
               "2. DEQUEUE\n"
               "3. DISPLAY\n"
               "4. COUNT\n"
               "5. EXIT\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) 
        {
            case 1:
                printf("Enter data to enqueue: ");
                scanf("%d", &data);
                enqueue(&q, data);
                break;
            case 2:
                data = dequeue(&q);
                if (data != -1) 
                {
                    printf("%d dequeued from queue\n", data);
                }
                break;
            case 3:
                display(&q);
                break;
            case 4:
                printf("Total elements in queue: %d\n", count(&q));
                break;
            case 5:
                exit(0);
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }
}
