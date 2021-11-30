#include <stdio.h>
#include <stdlib.h>
#include<stdint.h>


typedef uint8_t BYTE;
const int block_size = 512;
int main(int argc, char *argv[])
{

   if(argc != 2)
   {
       printf("usage: ./recover image.raw");
       return 1;
   }

    FILE *file = fopen(argv[1],"r");
    if (file == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }



   int counter = 0;
   char filename[8];
   FILE* outputptr = NULL;
   BYTE buffer[block_size];

   if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff )
   {
       if((buffer[3]*0xf0) == 0xe0)
       {

       }
   }






}