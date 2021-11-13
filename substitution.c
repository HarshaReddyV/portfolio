#include<cs50.h>
#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<ctype.h>

int validate(string a);
int main (int k, string argv[ ])
{


    //validate the nummber of arguments given
    if (k != 2)
    {
        printf("Usage:./caesar 26 letter key\n");
        printf("%s", argv);

    }

    string h = argv[1];

    validate(h);

     if(validate(h))
     {
        printf("repeated char");
     }
     else
     {
        printf("all good");
     }


}

int validate(string h)
{
    int k, p;

    for(int i=0,n=strlen(h);i<n;i++)
    {
        if(isalpha(h[i]))
        {
          for(k=0,p=0;p<n;p++)
          {
              if( int(strncmp(h[k],h[k+p])==0))
              {
                 return 1;
              }
              else
              {
                  return 0;
              }

          }

        }
        else
        {
            return 1;
        }
    }

}