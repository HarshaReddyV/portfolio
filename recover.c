#include <stdio.h>
#include <stdlib.h>
#include<stdbool.h>
#include<stdint.h>
#define block_size 512

int main(int argc, char *argv[])
{
  if(argc != 2)
  {
      printf("usage recover ./card.raw\n");
      return 1;
  }

  FILE *infile = fopen(argv[1], "r");
  if(infile == NULL)
  {
      fclose(infile);
      return 1;
  }

  typedef uint8_t BYTE;

  BYTE buffer[block_size];
  bool already_jpg = false;
  bool found_jpg = false;
  FILE *outfile = NULL;
  char filename[8];
  int counter = 0;

  while(fread(buffer,block_size,1,infile))
  {
     if(buffer[0]==0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] * 0xf0 == 0xe0) )
     {
         found_jpg = true;
         if(!already_jpg)
         {
             already_jpg = true;
         }
         else
         {
             fclose(outfile);
         }

         sprintf(filename,"%03i.jpg", counter);
         outfile = fopen(filename,"w");
         fwrite(outfile,sizeof(BYTE),1,infile);
         counter++;


     }
     else
     {
         if(already_jpg)
         {
             fwrite(outfile,sizeof(BYTE),1,infile);
         }
     }

  }

fclose(infile);
fclose(outfile);
return 0;

}