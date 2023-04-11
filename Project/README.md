# **Random Service Booking**
### Vide Demo: <https://youtu.be/vC_QBGoopLw>
### Description: This code ideally takes a date as an input as a string initially and Validates it wether it is a date or not by using regex and extracting date, month and year. This further validates for the correct amount of dates in each month by comparing it with the values that are given in an dictionary and check for leap year and is sensitive towards the 29 th of February

## project.py
### Project.py is the main project file import python modules such as re for regualr expressions to validate the user input as specific form and extract the data. Sys for system exit for unspecified or failed errors during the process and warns the user what and why it went wrong such as Invalid Date format.datetime to convert the user input which is usually in a string format to datetime delta which can used to validate date and subtract and add days to it.Tabulate modules to finally take all the data within the project and display to the user in a nicely formatted Tabular form

## Test_project.py
### test_project.py code test the function of get_Date in Project file by incuding datetime.date as a return value if the users inputs valid date or else asserts that the function performs system Exit via sys.exit().

## Requirement.txt
### Lists out all the modules and libraries that were imported and used in the project which can be used as a reference in the future when reimplementing, updating or modifiying the Modules and libraries.

## README.md
### A markdown file which gives a text disceiption of the project and the files inside the project and mentiond the URL for the Youtube video of the proeject demo.Could be used in the future for Reference