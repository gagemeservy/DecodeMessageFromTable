import urllib.request
from bs4 import BeautifulSoup

url = input("Enter url: ")
response = urllib.request.urlopen(url)
data = response.read()
soup = BeautifulSoup(data, "html.parser")
rows = soup.table
xList = []
yList = []
charList = []
counter = 0
xMax = 0
yMax = 0
for row in rows:
    cells = row.find_all("td")
    x = cells[0].get_text()
    char = cells[1].get_text()
    y = cells[2].get_text()
    if(counter > 0):
        xList.append(int(x))
        charList.append(char)
        yList.append(int(y))
        if(int(x) > xMax):
            xMax = int(x)
        if(int(y) > yMax):
            yMax = int(y)
    counter = counter + 1

coordinates = [[' ' for x in range(xMax+1)] for y in range(yMax+1)]

i = 0
while(i < len(charList)):
    coordinates[yList[i]][xList[i]] = charList[i]
    i = i + 1
    
def ReverseList(list):
   new_list = list[::-1]
   return new_list

print ('\n'.join(''.join(row) for row in ReverseList(coordinates)))

