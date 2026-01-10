#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100

typedef struct Node 
{
    int vertex;
    struct Node* next;
} Node;

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

void dfs(Graph* graph, int vertex) 
{
    graph->visited[vertex] = 1;
    printf("%d ", vertex);

    Node* temp = graph->adjLists[vertex];

    while (temp != NULL) 
    {
        int connectedVertex = temp->vertex;
        if (graph->visited[connectedVertex] == 0)
            dfs(graph, connectedVertex);

        temp = temp->next;
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

    printf("Enter edges (src dest):\n");

    for (int i = 0; i < edges; i++) 
    {
        int src, dest;
        printf("Edge %d: ", i + 1);
        scanf("%d %d", &src, &dest);
        addEdge(graph, src, dest);
    }

    printf("Depth First Search starting from vertex 0:\n");
    dfs(graph, 0);
}
