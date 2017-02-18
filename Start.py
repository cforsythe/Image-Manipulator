#Christopher Forsythe, gist: https://gist.github.com/cforsythe/f45a7d154fe50b931311
import random

pictures = [];redList = [];greenList = [];blueList = []   # variables for my different lists

for counter in range(1,10):
  imagePath = 'C:/Users/Chris/documents/CST205/Project1/IMages/' + str(counter) + '.png' # directing program to path of my images
  pictures.append(makePicture(imagePath))                                                #appending  pictures to a list
  
h = pictures[0].height;w = pictures[0].width;rand = random.random()    # height and width variables
EP = makeEmptyPicture(w, h)                     # creating empty picture
for x in range(0, w):                           # x range nested loop
  for y in range(0, h):                         # y range within x range, so this will do all Y's at an x coord
    for pics in range(0,9):                     # counter for my picture list
      pixel = getPixel(pictures[pics],x,y)      # getting pixels from each picture in the list
      redList.append(getRed(pixel))             # getting red pixel value and appending to list
      greenList.append(getGreen(pixel))         # getting green pixels and appending to list
      blueList.append(getBlue(pixel))           # getting blue pixel values and appending to list
    SortR = sorted(redList);SortG = sorted(greenList);SortB = sorted(blueList) #sorting values for each color
    fr = SortR[4];fg = SortG[4];fb = SortB[4]   # getting median pixel value and applying it to a variable
    newcolor = makeColor(fr,fg,fb)              # making color from pixel values applied to variables
    setColor(getPixel(EP, x, y), newcolor)      # setting color of empty picture to the new color
    redList = [];greenList = [];blueList = []   # resetting the lists so they can store new values
show(EP)                                        # shows the picture when done rendering
writePictureTo(EP, 'C:/Users/Chris/documents/CST205/Project1/IMages/' + str(rand) + '.png')  # saves picture to file path as a random number 