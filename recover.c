#include <stdio.h>
#include <stdlib.h>
#include<stdint.h>
#include<stdbool.h>
#include<cs50.h>

#define Block_size 512

int main(int argc, char *argv[])
{

   if(argc != 2)
   {
       printf("usage: ./recover image.raw");
       return 1;
   }

    typedef uint8_t BYTE;
    BYTE buffer[Block_size];
    size_t bytes_read;
    bool is_first_jpg = false;
    FILE *current_file = NULL;
    char filename[8];
    int current_file_number = 0;
    bool found_jpg = false;

    FILE* infile = fopen(argv[1],"r");
    if (infile == NULL)
    {
        fclose(infile);
        printf("Could not open file.\n");
        return 1;
    }

    //checking jpg type
    while(true)
    {
        bytes_read = fread(buffer,sizeof(BYTE),512,infile);

        if(bytes_read == 0)
        {
            break;
        }

         if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3]*0xf0) == 0xe0 )
         {
             found_jpg = true;
             if(!is_first_jpg)
             {
                 is_first_jpg = true;
             }
             else
             {
                 fclose(current_file);
             }

             sprintf(filename ,"%03i.jpg",current_file_number);
             current_file = fopen(filename,"w");

             fwrite(buffer,sizeof(BYTE),Block_size,current_file);
             current_file_number++;

         }

         else
         {
            if(found_jpg)
            {
                fwrite(buffer,sizeof(BYTE),bytes_read,current_file);
            }
         }


    }




fclose(infile);
fclose(current_file);
return 0;


}

