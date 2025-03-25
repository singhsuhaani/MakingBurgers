#Making Burgers - Suhaani Singh
#This program uses keyboard input to modify the number of buns and patties
#and calculates how many burgers made and displays it on the canvas 


def setup():
    """this function changes bg color to black and enlarges canvas size"""
    background(0)                               #bg color to black
    size(500,500)                               #enlarged canvas 

buns = 0                                        #makes the buns 0 for the start
patties = 0                                     #makes the patties 0 for the start 
     
def make_burgers(buns,patties):
    """this function is used for calculating how many burgers made"""
    buns = buns*8                               #every package has 8 buns
    patties = patties*10                        #every package has 10 patties 
    burgers = min(buns, patties)                #burgers made depends on 
                                                #number of buns
    return (burgers)                            
    
def draw():
    """this function displays the text and variable outputs on the canvas"""
    global buns, patties, burgers               #makes variables visible to the 
                                                #function
    background(0)                               #bg colour to black 
    textSize(20)                                #increases textsize 
    text("Package(s) of Buns", 40,100)          #prints text for buns 
    text("Package(s) of Patties", 280,100)      #prints text for patties
    text("Total Burgers Made", 170, 300)        #prints text for total burgers
    text(str(buns), 110, 150)                   #prints output for buns
    text(str(patties), 350, 150)                #prints output for patties
    burgers = make_burgers(buns, patties)       #calculates burgers made 
    text(burgers, 240, 350)                     #prints output for burgers
    
def keyPressed():
    """this function changes the variables for buns and patties according to what
    key is pressed"""
    global buns, patties, burgers               #makes variables visible to the 
                                                #function                         
    if key == "b":                              #if key b is pressed 
        buns = max(0, buns + 1)                 #no. of buns increases by 1 
    elif key == "v":                            #if key v is pressed 
        buns = max(0, buns - 1)                 #no. of buns decreases by 1 
    elif key == "p":                            #if key p is pressed
        patties = max(0, patties + 1)           #no. of patties increases by 1
    elif key == "o":                            #if key o is pressed
        patties = max(0, patties - 1)           #no. of patties decreases by 1 
    else:
        print("Wrong Key Pressed")              #if any other key, prints wrong key
    burgers = min(buns, patties)                #calculates burgers made 
