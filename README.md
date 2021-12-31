# AUSTRALIA TAX CALCULATOR
#### Video Demo: Watch it on [YOUTUBE](https://youtu.be/fgAecdUWhaI)
#### Description:

As a little background why i have done the project is a few months back it was the end of financial year and i have searched for websites
to calculate my estimated tax returns for the year and so every website i have been to has the tax rate stated as a text but not a single page
where i can enter my income from three different stream and get an estimate on my tax rates. if there are any they insist on signing me up and it annoyed me
so i have decided to do it for myself and hopefully laucnh it after further bettering the website

This website is built to caluculate the users tax rate for the year on various incomes in Australia
There are  basically three input asking for user incomes for the year namely from different sources;
### Personal income:
      income earned as salary and wages which is taxed using tax bracket for different levels of income
### Sole trader:
      income from contract work as a solo operator of the business taxed at a rate used for personal income for this financial year
### Business income:
      income through business activities is taxed at a flat rate for this financial year

Each income has it's own tax rate and brackets and we have to figure  out how much tax they will be paying for the year
input is processed in python and flask and the final tax they have to pay will be the output of the program
i have also created a database in order to store all the searches that's been made on the website and display them on the homepage after the user
has entered his input..

I have created the final project file as per the flask requirements as requirment.txt,templates folder with a basic layout which we can use for other pages
and a report.html to display my final results as output
The website homepage has three input fields for the user to enter his personal,business and sole trader income which will be sent to the application python
file using post function and then processed to calculate the tax rate which is store in a different varialble namely pt,st,bt
These values are then summed up and stored in database i have created using sqlite3 as reports and records as table
These values are then stored in other variable called reports and then sent to the report page using return and render_template function
Using for loop and the index template i have added tables with headers personal income,business and soletrader and printed out all the existing reports
in the database using SELECT * in sqlite and displayed in descending order of id so that the latest tax report will shown on the top of the reports
I have used bootstrap to design the responsive elements in the design  and couldn't design the header as i tried to do it on my pc and failed to use natice command line
as i am still getting used to programming on my pc
I have designed this website as a result of having difficulties finding a websites
that shows the same output without asking to sign up for the website
i am planning and further develope the website and launch it for the public to use for free and no marketing is done to them
