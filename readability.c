#include<cs50.h>
#include<stdio.h>
#include<string.h>
#include<ctype.h>

int count_words(string text, int* le, int* wo, int* se);

int main(void)
{
   int l, w, s,L,S,I,le,wo,se;

   string text = get_string("Text:");

   count_words(text, &le,&wo,&se);

   L= (le*100)/wo;
   S= (se*100)/wo;

   I= (0.0588*L)-(0.296*S)-15.8;

   if(I<1)
   {
     printf("BEFORE GRADE 1");
   }
   else if(I>16)
   {
     printf("GRADE 16+");
   }
   else
   {
      printf("GRADE %i\n",I);
   }



}


int count_words(string text, int* le, int* wo, int* se)
{
    int  i, n,l=0, w=1,x, s=1;
    for (i=0,n=strlen(text); i<n; i++)
    {
        //Counting letters neglecting spaces and symbols(, . !)
        if(isalpha(text[i]))
        {
           l++;

        }

        else if( text[i] ==' ')
        {
            for(x=0;text[x]==' ';i++)
            {
                  text[x] = text[i];
            }
            {
               w++;
            }
        }
        else if( (text[i] == ',') ||(text[i]==':')|| ( text[i] == '.') || (text[i] == '!'))
        {
            s++;
        }


    }

    *le=l;
    *wo=w;
    *se=s;
  return 0;


 }