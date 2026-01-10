#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100

typedef struct Node 
{
    int vertex;
    struct Node* next;
} Node;

typedef struct Queue 
{
    int items[MAX_VERTICES];
    int front;
    int rear;
} Queue;

typedef struct Graph 
{
    Node* adjLists[MAX_VERTICES];
    int visited[MAX_VERTICES];
    int numVertices;
} Graph;

Node* createNode(int v)
{
    Node* newNode = malloc(sizeof(Node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}

Graph* createGraph(int vertices)
{
    Graph* graph = malloc(sizeof(Graph));
    graph->numVertices = vertices;

    for (int i = 0; i < vertices; i++) 
    {
        graph->adjLists[i] = NULL;
        graph->visited[i] = 0;
    }

    return graph;
}

void addEdge(Graph* graph, int src, int dest)
{
    Node* newNode = createNode(dest);
    newNode->next = graph->adjLists[src];
    graph->adjLists[src] = newNode;
}

Queue* createQueue() 
{
    Queue* queue = malloc(sizeof(Queue));
    queue->front = -1;
    queue->rear = -1;
    return queue;
}

int isEmpty(Queue* queue)
{
    return queue->rear == -1;
}

void enqueue(Queue* queue, int value)
{
    if (queue->rear == MAX_VERTICES - 1)
        return;

    if (queue->front == -1)
        queue->front = 0;

    queue->items[++queue->rear] = value;
}

int dequeue(Queue* queue)
{
    if (isEmpty(queue))
        return -1;

    int item = queue->items[queue->front];

    if (queue->front >= queue->rear)
        queue->front = queue->rear = -1;
    else
        queue->front++;

    return item;
}

void bfs(Graph* graph, int startVertex)
{
    Queue* queue = createQueue();

    graph->visited[startVertex] = 1;
    printf("%d ", startVertex);
    enqueue(queue, startVertex);

    while (!isEmpty(queue))
    {
        int currentVertex = dequeue(queue);

        Node* temp = graph->adjLists[currentVertex];

        while (temp != NULL)
        {
            int connectedVertex = temp->vertex;

            if (graph->visited[connectedVertex] == 0)
            {
                graph->visited[connectedVertex] = 1;
                printf("%d ", connectedVertex);
                enqueue(queue, connectedVertex);
            }

            temp = temp->next;
        }
    }
}

void main()
{
    int vertices, edges;

    printf("Enter the number of vertices: ");
    scanf("%d", &vertices);

    Graph* graph = createGraph(vertices);

    printf("Enter the number of edges: ");
    scanf("%d", &edges);

    printf("Enter the edges (src dest):\n");

    for (int i = 0; i < edges; i++)
    {
        int src, dest;
        printf("Edge %d: ", i + 1);
        scanf("%d %d", &src, &dest);
        addEdge(graph, src, dest);
    }

    printf("Breadth First Search starting from vertex 0:\n");
    bfs(graph, 0);
}
