#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float x = (image[i][j].rgbtBlue + image[i][j].rgbtRed + image[i][j].rgbtGreen) / 3.00;

            int p = round(x);

            image[i][j].rgbtBlue = p;
            image[i][j].rgbtRed = p;
            image[i][j].rgbtGreen = p;

        }
    }


    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {

            //for sepia red
            int sr =  round((image[i][j].rgbtRed * 0.393) + (image[i][j].rgbtGreen * 0.769) + (image[i][j].rgbtBlue * 0.189));


            //for sepia green
            int sg = round((image[i][j].rgbtRed * 0.349) + (image[i][j].rgbtGreen * 0.686) + (image[i][j].rgbtBlue * 0.168));


            //for sepia blue
            int sb = round((image[i][j].rgbtRed * 0.272) + (image[i][j].rgbtGreen * 0.534) + (image[i][j].rgbtBlue * 0.131));


            image[i][j].rgbtBlue = (sb > 255) ? 255 : sb;
            image[i][j].rgbtRed = (sr > 255) ? 255 : sr;
            image[i][j].rgbtGreen = (sg > 255) ? 255 : sg;

        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;


            image[i][j].rgbtBlue =  image[i][width - j - 1].rgbtBlue;
            image[i][j].rgbtRed = image[i][width - j - 1].rgbtRed;
            image[i][j].rgbtGreen = image[i][width - j - 1].rgbtGreen;

            image[i][width - j - 1].rgbtBlue = blue;
            image[i][width - j - 1].rgbtRed = red;
            image[i][width - j - 1].rgbtGreen = green;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    temp[height][width] = image[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sumr = 0;
            int sumg = 0;
            int sumb = 0;
            float counter = 0;

            for (int k = -1; k < 2; k++)
            {
                for (int h = -1; h < 2; h++)
                {
                    if (i + k < 0 || i + k > height - 1 || j + h < 0 || j + h > width - 1)
                    {
                        continue;
                    }

                    sumr += image[i + k][j + h].rgbtRed;
                    sumg += image[i + k][j + h].rgbtGreen;
                    sumb += image[i + k][j + h].rgbtBlue;

                    counter++;
                }
            }

            temp[i][j].rgbtRed = round(sumr / counter);
            temp[i][j].rgbtGreen = round(sumg / counter);
            temp[i][j].rgbtBlue = round(sumb / counter);

        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;

        }

    }

    return;
}
