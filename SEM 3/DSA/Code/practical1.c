#include <stdio.h> 

void main ()
{
   int F,n,i=0,f1=0,f2=1;
   printf("enter number to be searched ");
   scanf("%d",&n);
   if(n<0)
     printf("entered number is not present");
   else
   {
       do
       {
           F=f1+f2;
           f2=f1;
           f1=F;
           if(n==F || n==0)
           {
               printf("entered number is present");
               i++;
               break;
           }
       }while(n>F);
   }
   if(i==0)
       printf("entered number is not present");
}
