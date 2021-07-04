#include<stdio.h>
#include<cs50.h>
#include<ctype.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main (int k, char* argv[])
{
   int key, i, n;
   float b;
   b = atof(argv[1]);

   if((k != 2) || (b < 0))
   {
      printf("./caesar key?\n");
      return 1;
   }
   else
   {
      key = round(b);

      if(key != b)
      {
         printf("./caesar key\n");
         return 1;
      }
   }

   string text;

   text = get_string("plaintext:");

    //reducing key to less than or equal to 26
   if(key > 26)
   {
      do
      {
         key = key - 26;
      }
      while(key > 26);
   }

   //printing results

    printf("ciphertext:");
    for(i = 0, n = strlen(text); i < n; i++)
    {
       if(isalpha (text[i]))
       {
           text[i] = text[i] + key;
           printf("%c",text[i]);
       }
       else
       {
          printf("%c",text[i]);
       }
    }
}