#include <stdio.h> 

void main ()
{
   int n[10],temp,i;
   printf("enter 10 numbers");
   for(int i=0; i<10; i++)
      scanf("%d",&n[i]);
   for(int i=0; i<10; i++)
   {
       for(int j=i+1; j<10; j++)
       {
          if(n[i]>n[j])
          {
             temp=n[i];
             n[i]=n[j];
             n[j]=temp;
          }
       }
   }
    printf("the greatest of 10 numbers is %d",n[9]);
}  
