# python
File Handling in Python
To store data temporarily and permanently, we use files. A file is the collection of data stored on a disk in one unit identified by filename.
1.	Create Files
2.	Read Files
3.	Write to files
Create and Write
with open(‘test.txt’,’w’) as fp:
       fp.write(“new line”)

#read
with open(‘test.txt’,’w’) as fp:
         fp.read()

#Types of File
•	Text File: Text file usually we use to store character data. For example, test.txt
•	Binary File: The binary files are used to store binary data such as images, video files, audio files, etc.

#File Path
A file path defines the location of a file or folder in the computer system. There are two ways to specify a file path.
1.	Absolute path: which always begins with the root folder
2.	Relative path: which is relative to the program's current working directory
The absolute path includes the complete directory list required to locate the file.

#Read File
To read or write a file, Python provides a built-in function open().
Syntax  open(file_path, access_mode) function. It returns the file object. This object is used to read or write the file according to the access mode.
Accesss mode represents R is for reading and W is for writing

# Opening the file with absolute path
fp = open(‘C:\\Users\\deepa\\OneDrive\\Desktop\\ex.txt’, 'r')
# read file
print(fp.read())
# Closing the file after reading
fp.close()


output
hn@gmail.com
+919743303225
+919686807518
hm46@yahoo.in
kffgh

#Writing to a File

To write content into a file, Use the access mode w to open a file in a write mode.
Note:
•	If a file already exists, it truncates the existing content and places the filehandle at the beginning of the file. A new file is created if the mentioned file doesn’t exist.
•	If you want to add content at the end of the file, use the access mode a to open a file in append mode
text = "This is new content"
# writing new content to the file
fp = open("C:\\Users\\deepa\\OneDrive\\Desktop\\ex.txt", 'w')
fp.write(text)
print('Done Writing')
fp.close()

output

Done Writing'

Appending content to file
import re
f=open("C://Users//deepa//OneDrive//Desktop//ex.txt",'+a')
print(f.write("hi"))
f1=open("C://Users//deepa//OneDrive//Desktop//ex.txt",'+r')
print(f1.read())



Move File Pointer
The seek() method is used to change or move the file's handle position to the specified location. The cursor defines where the data has to be read or written in the file.

The position (index) of the first character in files is zero, just like the string index.
•	If you want to add content at the end of the file, use the access mode a to open a file in append mode
text = "This is new content"
# writing new content to the file
fp = open("C:\\Users\\deepa\\OneDrive\\Desktop\\ex.txt", 'w')
fp.write(text)
print('Done Writing')
fp.close()

output

Done Writing'

Appending content to file
import re
f=open("C://Users//deepa//OneDrive//Desktop//ex.txt",'+a')
print(f.write("hi"))
f1=open("C://Users//deepa//OneDrive//Desktop//ex.txt",'+r')
print(f1.read())



Move File Pointer
The seek() method is used to change or move the file's handle position to the specified location. The cursor defines where the data has to be read or written in the file.

The position (index) of the first character in files is zero, just like the string index.

Example

f = open("sample.txt", "r")
# move to 11 character
f.seek(11)
# read from 11th character
print(f.read())

output
   content

readlines()		Read file into a list
# Single Line
import re
f=open("C://Users//deepa//OneDrive//Desktop//ex.txt",'r')
print(f.readline())

# Multiple Lines
import re
f=open("C://Users//deepa//OneDrive//Desktop//ex.txt",'r')
print(f.readlines())


Python File Methods
Method	      Description  
read()			Returns the file content.
readline()		Read single line
readlines()		Read file into a list
Example

f = open("sample.txt", "r")
# move to 11 character
f.seek(11)
# read from 11th character
print(f.read())

output
   content

readlines()		Read file into a list
# Single Line
import re
f=open("C://Users//deepa//OneDrive//Desktop//ex.txt",'r')
print(f.readline())

# Multiple Lines
import re
f=open("C://Users//deepa//OneDrive//Desktop//ex.txt",'r')
print(f.readlines())


#Python File Methods
Method	      Description  
read()			Returns the file content.
readline()		Read single line
readlines()		Read file into a list
truncate(size)	Resizes the file to a specified size.
write()			Writes the specified string to the file.
writelines()		Writes a list of strings to the file.
close()			Closes the opened file.
seek()			Set file pointer position in a file
tell()			Returns the current file location.
fileno()			Returns a number that represents the stream, from the operating system's perspective.
flush()			Flushes the internal buffer.



#Python List Files in a Directory

To list all files in a directory using Python, you can use the built-in os module.
Also, there are multiple ways to list files in a directory. In this article, We will use the following four methods.
•	os.listdir('dir_path'): Return the list of files and directories in a specified directory path.
•	os.walk('dir_path'): Recursively get the list of all files in a directory and subdirectories.
•	os.scandir('path'): Returns directory entries along with file attribute information.
•	glob.glob('pattern'): glob module to list files and folders whose names follow a specific pattern.
Downloading files from web using Python
Python provides different modules like urllib, requests etc to download files from the web 
raise_for_status() Ensures that program halt if bad download occurs without  crashing. Always call raise_for_status() after calling requests.get()

The iter_content() method returns “chunks” of the content on each iteration through the loop. Each chunk is of the bytes data type, and you get to specify how many bytes each chunk will contain. One hundred thousand bytes is generally a good size, so pass 100000 as the argument to iter_content()

To review, here’s the complete process for downloading and saving a file:
1.	Call requests.get() to download the file.
2.	Call open() with 'wb' to create a new file in write binary mode.
3.	Loop over the Response object’s iter_content() method.
4.	Call write() on each iteration to write the content to the file.
5.	Call close() to close the file.

1. Import module
import requests
The requests module lets you easily download files from the web without having to worry about complicated issues such as network errors, connection problems, and data compression

2. Get the link or url
url = 'https://www.facebook.com/favicon.ico'
r = requests.get(url, allow_redirects=True)
3. Save the content with name.
open('facebook.ico', 'wb').write(r.content)
save the file as facebook.ico.


#BeautifulSoup
BeautifulSoup is a Python library that is used to pull data of HTML and XML files. It is mainly designed for web scrapping. It works with the parser to provide a natural way of navigating, searching, and modifying the parse tree

#Working with Excel Spreadsheets in Python
First, let’s go over some basic definitions: an Excel spreadsheet document is called a workbook. A single workbook is saved in a file with the .xlsx extension. Each workbook can contain multiple sheets (also called worksheets). The sheet the user is currently viewing (or last viewed before closing Excel) is called the active sheet. Each sheet has columns (addressed by letters starting at A) and rows (addressed by numbers starting at 1). A box at a particular column and row is called a cell. Each cell can contain a number or text value. The grid of cells with data makes up a sheet.
Openpyxl is a Python library that provides various methods to interact with Excel Files using Python. It allows operations like reading, writing, arithmetic operations, plotting graphs, etc.
Getting Sheets from the Workbook Each sheet is represented by a Worksheet object, which you can obtain by using the square brackets with the sheet name string like a dictionary key. Finally, you can use the active attribute of a Workbook object to get the workbook’s active sheet. The active sheet is the sheet that’s on top when the workbook is opened in Excel. Once you have the Worksheet object, you can get its name from the title attribute.
Example.xlsx
#Reading from Spreadsheets
To read an Excel file you have to open the spreadsheet using the load_workbook() method. 
active to select the first sheet available 
the cell attribute to select the cell by passing the row and column parameter. The value attribute prints the value of the particular cell. 
Note: The first row or column integer is 1, not 0.
import openpyxl
path = "demo.xlsx"
wb_obj = openpyxl.load_workbook(path)
#sheet_obj = wb_obj.active
cell_obj = sheet_obj.cell(row = 1, column = 2)
print(cell_obj.value)
output
             Name

#Reading from Multiple Cells
There can be two ways of reading from multiple cells. 
Method 1: We can get the count of the total rows and columns using the max_row and max_column respectively. We can use these values inside the for loop to get the value of the desired row or column or any cell depending upon the situation. Let’s see how to get the value of the first column and first row.

import openpyxl
path = "demo.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active
row = sheet_obj.max_row
column = sheet_obj.max_column
print("Total Rows:", row)
print("Total Columns:", column)

print("\nValue of first column")
for i in range(1, row + 1):
	cell_obj = sheet_obj.cell(row = i, column = 1)
print(cell_obj.value)
print("\nValue of first row")
for i in range(1, column + 1):
	cell_obj = sheet_obj.cell(row = 2, column = i)
	print(cell_obj.value, end = " "))

output
Total Rows: 8
Total Columns: 3

Value of first column
USN
1
2
3
4
5
6
7

Value of first row
1 Ravi  23 

Method 2: We can also read from multiple cells using the cell name. This can be seen as the list slicing of Python.

import openpyxl
path = "demo.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active
cell_obj = sheet_obj['A1': 'c4']
for cell1, cell2,cell3, cell4 in cell_obj:
	print(cell1.value, cell2.value, cell3.value, cell4.value)

Output
USN    Name      Age
1       Ravi     23
2       Adithya  22
3       Akshay   12


#Writing to Spreadsheets
First, let’s create a new spreadsheet, and then we will write some data to the newly created file. An empty spreadsheet can be created using the Workbook() method
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
sheet['A1']=200
sheet['A2']=100
sheet['A3']=300
sheet['A4']=400
sheet['A5']=500
sheet['A6']='=sum(A1:A5)'
wb.save("ex.xlsx")

#Insert data or to write to an Excel sheet
Call the openpyxl.Workbook() function to create a new, blank Workbook object. The workbook will start off with a single sheet named Sheet. You can change the name of the sheet by storing a new string in its title attribute. Any time you modify the Workbook object or its sheets and cells, the spreadsheet file will not be saved until you call the save() workbook method.
import openpyxl
my_wb = openpyxl.Workbook()
my_sheet = my_wb.active
c1 = my_sheet.cell(row = 1, column = 1)
c1.value = "Aadrika"
c2 = my_sheet.cell(row= 1 , column = 2)
c2.value = "Adwaita"
c3 = my_sheet['A2']
c3.value = "Satyajit"
# B2 = column = 2 & row = 2.
c4 = my_sheet['B2']
c4.value = "Bivas"
my_wb.save("C:\\Users\\deepa\\OneDrive\\Desktop\\e.xlsx")


output
 
#To add Sheets in the Workbook 
import openpyxl
my_wb = openpyxl.Workbook()
my_sheet = my_wb.active
my_wb.create_sheet(index = 1 , title = "new sheet")
my_wb.save("C:\Users\TP\Desktop\Book1.xlsx")

#Display Total number of rows.
import openpyxl
my_path = "C:\Users\TP\Desktop\Book1.xlsx"
my_wb_obj = openpyxl.load_workbook(my_path)
my_sheet_obj = my_wb_obj.active
print(my_sheet_obj.max_row)

#Display total number of columns
import openpyxl
# Give the location of the file
My_path = "C:\Users\TP\Desktop\Book1.xlsx"
My_wb_obj = openpyxl.load_workbook(path)
my_sheet_obj = my_wb_obj.active
print(sheet_obj.max_column)

#Display all columns name
import openpyxl
# Give the location of the file
my_path = "C:\Users\TP\Desktop\Book1.xlsx"
# workbook object is created
my_wb_obj = openpyxl.load_workbook(my_path)
my_sheet_obj = my_wb_obj.active
my_max_col = my_sheet_obj.max_column
for i in range(1, my_max_col + 1):
   my_cell_obj = my_sheet_obj.cell(row = 1, column = i)
   print(my_cell_obj.value)
#Workbooks, Sheets, Cells
As a quick review, here’s a rundown of all the functions, methods, and data types involved in reading a cell out of a spreadsheet file:
1.	Import the openpyxl module.
2.	Call the openpyxl.load_workbook() function.
3.	Get a Workbook object.
4.	Use the active or sheetnames attributes.
5.	Get a Worksheet object.
6.	Use indexing or the cell() sheet method with row and column keyword arguments.
7.	Get a Cell object.
8.	Read the Cell object’s value attribute.

