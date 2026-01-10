#include <stdio.h> 

struct student
{
    int roll;
    float per;
    char name[10];
}s[5],temp;

void main ()
{
   int i;
   printf("enter name, roll no. and percentage of 5 students");
   for(int i=0; i<5; i++)
   {
       printf("enter name, roll no. and percentage ");
       scanf("%s",s[i].name);
       scanf("%d %f",&s[i].roll,&s[i].per);
   }
   for(int i=0; i<5; i++)
   {
       for(int j=i+1; j<5; j++)
       {
          if(s[i].per<s[j].per)
          {
             temp=s[i];
             s[i]=s[j];
             s[j]=temp;
          }
       }
   }
    for(int i=0; i<5; i++)
   {
       printf("%s ",s[i].name);
       printf("%d %f \n",s[i].roll,s[i].per);
   }
}  
