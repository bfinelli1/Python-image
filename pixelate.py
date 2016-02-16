from cImage import *

def avg(num1, num2):
    average = (num1 + num2) / 2
    return average
begin = 0
#change max for different sized squares
max = 60

start = begin
end = max
rowstart = begin
rowend = max

fileInput = raw_input("File name: ")

oldImage = FileImage(fileInput)

myimagewindow = ImageWin("Image Processing", oldImage.width*2, oldImage.height)

oldImage.draw(myimagewindow)
myRange = oldImage.width/max
myRange2 = oldImage.height/max

newImage = EmptyImage(oldImage.width,oldImage.height)
for j in range (myRange2):
    for i in range (myRange):
        for row in range (rowstart, rowend):
            x = avg(start, end)
            y = avg(rowstart, rowend)
            for col in range (start, end):
                oldPixel = oldImage.getPixel(x, y)
                newPixel = oldPixel
                newImage.setPixel(col,row,newPixel)
        start = end
        end = end + max
    num = oldImage.width%max
    newRange = oldImage.width - num
    newRange = newRange - 1
    if (end-max) < oldImage.width:              #takes care of final column
        for row in range (rowstart, rowend):
            z = avg(newRange, oldImage.width)
            a = avg(rowstart, rowend)
            for col in range (newRange, oldImage.width):
                newPixel = oldImage.getPixel(z, a)
                newImage.setPixel(col,row,newPixel)
    start = begin
    end = max
    rowstart = rowend
    rowend = rowend + max
start = begin
end = max
rowstart = rowend-max
rowend = oldImage.height
if (rowend - max) < oldImage.height:            #takes care of final row
    for k in range (myRange):
        for row in range (rowstart, rowend):
            b = avg(rowend-max, oldImage.height)
            c = avg(start, end)
            for col in range(start, end):
                oldPixel = oldImage.getPixel(c, b)
                newImage.setPixel(col, row, oldPixel)
        start = end
        end = end + max
    if(end-max) < oldImage.width:               #takes care of final square
        for row in range(rowstart, oldImage.height):
            d = avg(rowstart, oldImage.height)
            e = avg(start, oldImage.width)
            for col in range(start-1, oldImage.width):
                oldPixel = oldImage.getPixel(e, d)
                newImage.setPixel(col, row, oldPixel)
    

newImage.setPosition(oldImage.width+1, 0)

newImage.draw(myimagewindow)

myimagewindow.exitOnClick()
