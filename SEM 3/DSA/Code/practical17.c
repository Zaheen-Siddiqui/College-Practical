#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Stack 
{
    int top;
    unsigned capacity;
    int* array;
};

struct Stack* createStack(unsigned capacity) 
{
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    if (!stack) return NULL;

    stack->top = -1;
    stack->capacity = capacity;
    stack->array = (int*)malloc(stack->capacity * sizeof(int));

    if (!stack->array) return NULL;
    return stack;
}

int Empty(struct Stack* stack) 
{
    return stack->top == -1;
}

int pop(struct Stack* stack) 
{
    if (!Empty(stack))
        return stack->array[stack->top--];
    return '$';
}

void push(struct Stack* stack, int op) 
{
    stack->array[++stack->top] = op;
}

int evaluatePostfix(char* exp) 
{
    struct Stack* stack = createStack(strlen(exp));
    if (!stack) return -1;

    for (int i = 0; exp[i]; ++i) 
    {
        if (exp[i] == ' ') continue;

        else if (isdigit(exp[i])) 
        {
            int num = 0;

            while (isdigit(exp[i])) 
            {
                num = num * 10 + (exp[i] - '0');
                i++;
            }

            i--;
            push(stack, num);
        } 
        else 
        {
            int val1 = pop(stack);
            int val2 = pop(stack);

            switch (exp[i]) 
            {
                case '+': push(stack, val2 + val1); break;
                case '-': push(stack, val2 - val1); break;
                case '*': push(stack, val2 * val1); break;
                case '/': push(stack, val2 / val1); break;
            }
        }
    }

    return pop(stack);
}

void main() 
{
    char exp[100];

    printf("Enter a postfix expression: ");
    fgets(exp, sizeof(exp), stdin);

    size_t len = strlen(exp);
    if (len > 0 && exp[len - 1] == '\n')
        exp[len - 1] = '\0';

    int result = evaluatePostfix(exp);
    printf("Result: %d\n", result);
}
