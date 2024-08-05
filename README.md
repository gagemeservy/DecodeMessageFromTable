# DecodeMessageFromTable
 This short python script reads an html table from any given link, takes the coordinates and chars from the table and graphs the chars at the given coordinates.

#Table Format
The table needs to have this exact order of columns, x coordinate, character to use, y coordinate. The coordinates do not need to be in any order. The coordinate system is used in a way that 0,0 is the bottom left of the grid.
The table should look like this example image which can be found at this link https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub.
![InputTableExample](https://github.com/user-attachments/assets/500f0fa3-30f3-4ed6-adbb-826582df24e3)

#Running the program
To run it, just open the python solution in Visual Studio or any other ide you want to use.
When you run it, it will ask what url you want to use, put any url with a single table on the page.
It will then graph the characters to the given coordinates.
