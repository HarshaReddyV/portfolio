#include<cs50.h>
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<math.h>

int count_words(string text, int *le, int *wo, int *se);

int main(void)
{
    int l, w, I, s, le, wo, se;
    float L, S;

    string text = get_string("Text:");

    //refering multiple return values

    count_words(text, &le, &wo, &se);

    //float to dispaly decimals

    L = ((float)le / wo) * 100;
    S = ((float)se / wo) * 100;

    //rounding

    I = round(0.0588 * L - 0.296 * S - 15.8);

    //grade displaying
    //i is less than 1
    if (I < 1)
    {
        printf("Before Grade 1\n");
    }

    //i is greater than 16
    else if (I > 16)
    {
        printf("Grade 16+\n");
    }

    //i is ok

    else
    {
        printf("Grade %i\n", I);
    }
}


int count_words(string text, int *le, int *wo, int *se)
{
    int  i, n, l = 0, w = 1, x, s = 0;
    for (i = 0, n = strlen(text); i < n; i++)
    {
        //Counting letters neglecting spaces and symbols(, . !)
        if (isalpha(text[i]))
        {
            l++;

        }

        else if (text[i] == ' ')
        {
            for (x = 0; text[x] == ' '; i++)
            {
                text[x] = text[i];
            }
            {
                w++;
            }
        }
        else if ((text[i] == '.') || (text[i] == '!') || (text[i] == '?'))
        {
            s++;
        }
    }

    *le = l;
    *wo = w;
    *se = s;
    return 0;
} 