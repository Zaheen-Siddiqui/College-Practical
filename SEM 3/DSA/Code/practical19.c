#include <stdio.h>
#include <stdlib.h>

struct Node 
{
    int data;
    struct Node* left;
    struct Node* right;
};

struct Node* createNode(int value) 
{
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

void insert(struct Node** root, int value) 
{
    if (*root == NULL)
        *root = createNode(value);

    else if (value < (*root)->data)
        insert(&((*root)->left), value);

    else
        insert(&((*root)->right), value);
}

struct Node* search(struct Node* root, int value) 
{
    if (root == NULL || root->data == value)
        return root;

    else if (value < root->data)
        return search(root->left, value);

    else
        return search(root->right, value);
}

int countNodes(struct Node* root) 
{
    if (root == NULL)
        return 0;

    return 1 + countNodes(root->left) + countNodes(root->right);
}

int countLeafNodes(struct Node* root) 
{
    if (root == NULL)
        return 0;

    if (root->left == NULL && root->right == NULL)
        return 1;

    return countLeafNodes(root->left) + countLeafNodes(root->right);
}

void freeTree(struct Node* root) 
{
    if (root) 
    {
        freeTree(root->left);
        freeTree(root->right);
        free(root);
    }
}

void main() 
{
    struct Node* root = NULL;
    int choice, value;

    while (1) 
    {
        printf("Menu:\n");
        printf("1. Insert\n");
        printf("2. Search\n");
        printf("3. Count Nodes\n");
        printf("4. Count Leaf Nodes\n");
        printf("5. Exit\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) 
        {
            case 1:
                printf("Enter value to insert: ");
                scanf("%d", &value);
                insert(&root, value);
                break;

            case 2:
                printf("Enter value to search: ");
                scanf("%d", &value);
                struct Node* result = search(root, value);

                if (result)
                    printf("%d found in the tree.\n", value);
                else
                    printf("%d not found in the tree.\n", value);

                break;

            case 3:
                printf("Total nodes in the tree: %d\n", countNodes(root));
                break;

            case 4:
                printf("Total leaf nodes in the tree: %d\n", countLeafNodes(root));
                break;

            case 5:
                freeTree(root);
                exit(0);

            default:
                printf("Invalid choice. Please try again.\n");
        }
    }
}
