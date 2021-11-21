#Final Project
#Anas Saqib and Vinay Jayachandiran

#This is a game based after the anime show Naruto, it is a 2 player battle game, with no AI.
#There are nine different characters, each character can move left or right, jump and crouch.
#They have a light punch, hard punch, a combo, and a guard. They also have three special
#attacks. To do special attack, you need chakra, there is a chakra bar indicating a players
#chakra level near the top of the screen. A player can gain chakra by attacking the opponent,
#or by charging (up+down). You need a third of the chakra bar to do
#attack 1, 2 thirds for attack 2 and a full bar for attack3. In the start of the game, there is a controls screen that shows
#the keys to perform attacks for player one and player two. There are also five different
#stages to choose from, each stage has platforms that the player can jump on. All the sprites
#for each character are in a folder with the character's name. Here is the layout:

#start screen -> character selection -> stage selection -> fight page
#controls screen is a link from start screen

#also thanks go Umar Azhar for giving us some sprites and fixing a glitch with the music
#thanks to Mr. McKenzie for his examples and teaching us
#and thanks to everyone who made the sprite sheets

from pygame import*
from random import*
from math import*

init() 
mixer.music.load("intro.mp3") #starting song
mixer.music.play(-1)



screen = display.set_mode((1000,700))
count=0 # a variable used to keep track of how long a players special attack should last

start = Rect(402,5,197,82) #on the starting screen teh button that leads to the next screen
controls = Rect(807, 4, 180, 68) #button that leads to controls screen
back = Rect(667, 2, 157, 77) #leads from the controls screen back to the start
counter=0 #used to reset variables
counter2=0 #used to reset variables for player2
page="startpage" #to start off

running=True


collisionl = [image.load("Explode-05_frame_"+str(x)+".gif") for x in range(0,28)] #for when two special attacks collide

#loading images for the starting of the game, names are self explanitory

ifrontpage = image.load("Front Page copy.jpg")
istart = image.load("start.png")
icontrols = image.load("controls.png")
selectionpage = image.load("selection screen.jpg")
hover = image.load("hover.png")
select = image.load("select.png")
conform = image.load("confirm.png") #I am aware of the spelling error on confirm
conform2 =image.load("confirm2.png")
narutostance = image.load("naruto Stance.png") #stances are shown on charter selection when you select a character
madarastance = image.load("madara Stance.png")
kisamestance = image.load("kisame Stance.png")
jiraiyastance = image.load("jiraiya Stance.png")
itachistance = image.load("itachi Stance.png")
gaarastance = image.load("gaara Stance.png")
hokagestance = image.load("hokage Stance.png")
sasukestance = image.load("sasuke Stance.png")
kakashistance = image.load("kakashi Stance.png")
healthbarpic = image.load("health bar.png")
grayhealthbarpic = image.load("gray healthbar.png")
slowmotion = image.load("slow motion.png")
healthitem = image.load("health item.png")
chakraitem= image.load("chakra item.png")
player1 = image.load("player1.png")
player1victory = image.load("player1 victory.png")
player2 = image.load("player2.png")
player2victory = image.load("player2 victory.png")
selectintructions = image.load("instructions.png")
playagain = image.load("play again.png")
timesFont = font.SysFont("Times New Roman",50) #initilizing font

#defining all the rectangles for character selection
narutorect = Rect(54, 19, 101, 103)
madararect = Rect(201, 19, 101, 100)
kisamerect = Rect(351, 19, 101, 101)
sakurarect = Rect(0,0,0,0)
jiraiyarect= Rect(54, 157, 101, 101)
itachirect = Rect(201, 158, 101, 100)
gaararect  = Rect(351, 157, 101, 101)
hokagerect = Rect(54, 300, 101, 101)
sasukerect = Rect(202, 297, 101, 101)
kakashirect= Rect(351,297,101,101)
#to pick a character
conformrect= Rect(500,450,500,250)

#to restart game after fight
playagainrect= Rect(415,425,167,43)

pics=[[""]*15  for i in range(9)] # ends up a 3-dim list first dimension goes to the pitures of a general character, second dimension goes to the pictures for a move, third dimension goes to each individual picture

#loading all the sprites for a character, only the two picked characters will be loaded, this function is called below
def imageload(firstplayer,secondplayer):
    global pics,dogs,fireitachi
    
    if firstplayer=="naruto" or secondplayer=="naruto":
        #setting up all naruto pics
        pics[0][0]=[image.load("Naruto\\Stance1"+str(x)+".png") for x in range(1,6)]
        pics[0][1]=[image.load("Naruto\\walk1"+str(x)+".png") for x in range(1,7)]
        pics[0][2]=[image.load("Naruto\\crouch.png")]
        pics[0][3]=[image.load("Naruto\\jump"+str(x)+".png") for x in range(0,4)]
        pics[0][4]=[image.load("Naruto\\summon1"+str(x)+".png") for x in range(1,13)]
        pics[0][5]=[image.load("Naruto\\attack2"+str(x)+".png") for x in range(1,49)]
        pics[0][6]=[image.load("Naruto\\attack3"+str(x)+".png") for x in range(0,58)]
        pics[0][7]=[image.load("Naruto\\punch"+str(x)+".png") for x in range(0,4)]
        pics[0][8]=[image.load("Naruto\\hard punch"+str(x)+".png") for x in range(0,4)]
        pics[0][9]=[image.load("Naruto\\combo"+str(x)+".png") for x in range(0,12)]
        pics[0][10] = [image.load("Naruto\\attack30.png")]
        pics[0][11] = [image.load("Naruto\\run" +str(x)+".png")for x in range(1,7)]
        pics[0][12] = "naruto" #so we can keep track of which character we are using
        pics[0][13] = image.load("Naruto\\naruto mugshot.png")
        pics[0][14]=[image.load("Naruto\\Naruto"+str(x)+".png") for x in range(1,10)]
        
    if firstplayer=="kisame" or secondplayer=="kisame":
        #setting up all kisame pics
        pics[1][0]=[image.load("Kisame2\\stance"+str(x)+".png") for x in range(0,5)]
        pics[1][1]=[image.load("Kisame2\\walk"+str(x)+".png") for x in range(1,6)]
        pics[1][2]=[image.load("Kisame2\\crouch0.png")]
        pics[1][3]=[image.load("Kisame2\\jump"+str(x)+".png") for x in range(0,4)]
        pics[1][4]=[image.load("Kisame2\\attack2"+str(x)+".png") for x in range(0,8)]+[image.load("Kisame2\\attack1"+str(x)+".png") for x in range(0,14)] #this picture had no hand sign, so we used attack2s signs
        pics[1][5]=[image.load("Kisame2\\attack2"+str(x)+".png") for x in range(0,22)]
        pics[1][6]=[image.load("Kisame2\\attack3"+str(x)+".png") for x in range(0,26)]
        pics[1][7]=[image.load("Kisame2\\punch"+str(x)+".png") for x in range(0,7)]
        pics[1][8]=[image.load("Kisame2\\hard punch"+str(x)+".png") for x in range(0,7)]
        pics[1][9]=[image.load("Kisame2\\combo"+str(x)+".png") for x in range(0,13)]
        pics[1][10]=[image.load("Kisame2\\guard.png")]
        pics[1][11]=[image.load("Kisame2\\run"+str(x)+".png") for x in range(1,6)]
        pics[1][12]="kisame"
        pics[1][13] = image.load("Kisame2\\Kisame mugshot.png")
        pics[1][14]=[image.load("Kisame2\\damage"+str(x)+".png") for x in range(1,12)]

    if firstplayer=="madara" or secondplayer=="madara":
        #setting up all Madara pics
        pics[2][0]=[image.load("Madara\\stance"+str(x)+".png") for x in range(1,4)]
        pics[2][1]=[image.load("Madara\\walks"+str(x)+".png") for x in range(1,6)]
        pics[2][2]=[image.load("Madara\\crouch.png") ]
        pics[2][3]=[image.load("Madara\\jumps"+str(x)+".png") for x in range(1,6)]
        pics[2][4]=[image.load("Madara\\attack1"+str(x)+".png") for x in range(1,29)]
        pics[2][5]=[image.load("Madara\\attack2"+str(x)+".png") for x in range(1,14)]
        pics[2][6]=[image.load("Madara\\attack3"+str(x)+".png") for x in range(1,10)]
        pics[2][7]=[image.load("Madara\\punch"+str(x)+".png") for x in range(1,6)]
        pics[2][8]=[image.load("Madara\\hardpunch"+str(x)+".png") for x in range(1,12)]
        pics[2][9]=[image.load("Madara\\Madara"+str(x)+".png") for x in range(3,13)]
        pics[2][10]=[image.load("Madara\\attack11.png")]
        pics[2][11]=[image.load("Madara\\run"+str(x)+".png") for x in range(1,7)]
        pics[2][12]="madara"
        pics[2][13]=image.load("Madara\\Madara mugshot.png")
        pics[2][14]=[image.load("Madara\\damage"+str(x)+".png") for x in range(1,12)]


    if firstplayer=="kakashi" or secondplayer=="kakashi":
        #setting up all Kakashi pics
        pics[3][0]=[image.load("Kakashi\\stance"+str(x)+".png") for x in range(0,4)]
        pics[3][1]=[image.load("Kakashi\\walk"+str(x)+".png") for x in range(0,5)]
        pics[3][2]=[image.load("Kakashi\\crouch"+str(x)+".png") for x in range(0,1)]
        pics[3][3]=[image.load("Kakashi\\jump"+str(x)+".png") for x in range(0,4)]
        pics[3][4]=[image.load("Kakashi\\summon"+str(x)+".png") for x in range(0,12)]
        pics[3][5]=[image.load("Kakashi\\fsummon"+str(x)+".png") for x in range(0,10)]
        pics[3][6]=[image.load("Kakashi\\lightningblade"+str(x)+".png") for x in range(0,28)]
        pics[3][7]=[image.load("Kakashi\\punch"+str(x)+".png") for x in range(0,5)]
        pics[3][8]=[image.load("Kakashi\\hardpunch"+str(x)+".png") for x in range(0,4)]
        pics[3][9]=[image.load("Kakashi\\cattack"+str(x)+".png") for x in range(0,13)]
        pics[3][10]=[image.load("Kakashi\\Kakashi7.png")]
        pics[3][11]=[image.load("Kakashi\\Kakashi"+str(x)+".png") for x in range(1,7)]
        pics[3][12]="kakashi"
        pics[3][13]=image.load("Kakashi\\Kakashi mugshot.png")
        pics[3][14]=[image.load("Kakashi\\Kakashi"+str(x)+".png") for x in range(8,18)]
        dogs=[image.load("Kakashi\\dogs"+str(x)+".png") for x in range(0,4)]

    if firstplayer=="gaara" or secondplayer=="gaara":
        #setting up all Gaara pics
        pics[4][0]=[image.load("Gaara\\stance"+str(x)+".png") for x in range(1,5)]
        pics[4][1]=[image.load("Gaara\\walk"+str(x)+".png") for x in range(1,7)]
        pics[4][2]=[image.load("Gaara\\crouch.png")]
        pics[4][3]=[image.load("Gaara\\jump"+str(x)+".png") for x in range(1,5)]
        pics[4][4]=[image.load("Gaara\\attack1"+str(x)+".png") for x in range(43,60)] #slight naming error
        pics[4][5]=[image.load("Gaara\\attack2"+str(x)+".png") for x in range(1,41)]
        pics[4][6]=[image.load("Gaara\\attack3"+str(x)+".png") for x in range(1,19)]
        pics[4][7]=[image.load("Gaara\\punch"+str(x)+".png") for x in range(1,9)]
        pics[4][8]=[image.load("Gaara\\hard punch"+str(x)+".png") for x in range(1,10)]
        pics[4][9]=[image.load("Gaara\\combo"+str(x)+".png") for x in range(1,16)]
        pics[4][10]=[image.load("Gaara\\guard.png")]
        pics[4][11]=[image.load("Gaara\\run"+str(x)+".png") for x in range(1,7)]
        pics[4][12]="gaara"
        pics[4][13]= image.load("Gaara\\gaara mugshot.png")
        pics[4][14]=[image.load("Gaara\\damage"+str(x)+".png") for x in range(1,13)]

    if firstplayer=="jiraiya" or secondplayer=="jiraiya":
        pics[5][0]=[image.load("Jiraiya\\Jiraiya 2"+str(x)+".png") for x in range(1,7)]
        pics[5][1]=[image.load("Jiraiya\\Jiraiya 2"+str(x)+".png") for x in range(16,22)]
        pics[5][2]=[image.load("Jiraiya\\Jiraiya 264.png")]
        pics[5][3]=[image.load("Jiraiya\\Jiraiya 2"+str(x)+".png") for x in range(54,58)]
        pics[5][4]=[]
        for x in range(209,219):
             pics[5][4].append(image.load("Jiraiya\\Jiraiya 2"+str(x)+".png"))
             if x==215:
                 for i in range(6):
                    pics[5][4].append(image.load("Jiraiya\\Jiraiya 2"+str(x)+".png"))
        
        pics[5][5]=[image.load("Jiraiya\\attack2"+str(x)+".png") for x in range(1,6)]+[image.load("Jiraiya\\attack2"+str(x)+".png") for x in range(8,35)]
        pics[5][6]=[image.load("Jiraiya\\attack 3"+str(x)+".png") for x in range(1,8)]
        pics[5][7]=[image.load("Jiraiya\\Jiraiya 2"+str(x)+".png") for x in range(158,163)]
        pics[5][8]=[image.load("Jiraiya\\Jiraiya 2"+str(x)+".png") for x in range(135,140)]
        pics[5][9]=[image.load("Jiraiya\\Jiraiya 2"+str(x)+".png") for x in range(101,117)]
        pics[5][10]=[image.load("Jiraiya\\Jiraiya 285.png")]
        pics[5][11]=[image.load("Jiraiya\\Jiraiya 2"+str(x)+".png") for x in range(25,31)]
        pics[5][12]="jiraiya"
        pics[5][13]=image.load("Jiraiya\\Jiraiya 211.png")
        pics[5][14]=[image.load("Jiraiya\\damage"+str(x)+".png") for x in range(1,13)]

    if firstplayer=="itachi" or secondplayer=="itachi":
        #setting up all itachi pics
        pics[6][0]=[image.load("Itachi\\itachid"+str(x)+".png") for x in range(8,12)]
        pics[6][1]=[image.load("Itachi\\itachid"+str(x)+".png") for x in range(18,24)]
        pics[6][2]=[image.load("Itachi\\itachid34.png") ]
        pics[6][3]=[image.load("Itachi\\itachid"+str(x)+".png") for x in range(35,39)]
        pics[6][4]=[image.load("Itachi\\itachid"+str(x)+".png") for x in range(175,188)] + [image.load("Madara\\attack1"+str(x)+".png") for x in range(2,29)]
        pics[6][5]=[image.load("Itachi\\itachid"+str(x)+".png") for x in range(153,159)]+[image.load("Itachi\\Itachi"+str(x)+".png") for x in range(2,29)]
        pics[6][6]=[image.load("Itachi\\itachid"+str(x)+".png") for x in range(153,159)]
        pics[6][7]=[image.load("Itachi\\itachid"+str(x)+".png") for x in range(79,83)]
        pics[6][8]=[image.load("Itachi\\itachid"+str(x)+".png") for x in range(75,79)]
        pics[6][9]=[image.load("Itachi\\itachid"+str(x)+".png") for x in range(55,68)]
        pics[6][10]=[image.load("Itachi\\itachid46.png")]
        pics[6][11]=[image.load("Itachi\\itachid"+str(x)+".png") for x in range(24,30)]
        pics[6][12]="itachi"
        pics[6][13]= image.load("Itachi\\itachid1.png")
        pics[6][14]=[image.load("Itachi\\itachid"+str(x)+".png") for x in range(1047,1058)]
        fireitachi=[image.load("Itachi\\Sasuke"+str(x)+".png") for x in range(4,10)]
        
    if firstplayer=="sasuke" or secondplayer=="sasuke":
        pics[7][0]=[image.load("Sasuke\\sasukedd"+str(x)+".png") for x in range(5,9)]
        pics[7][1]=[image.load("Sasuke\\sasukedd"+str(x)+".png") for x in range(12,19)]
        pics[7][2]=[image.load("Sasuke\\sasukedd60.png") ]
        pics[7][3]=[image.load("Sasuke\\sasukedd"+str(x)+".png") for x in range(24,29)]
        pics[7][4]=[image.load("Sasuke\\sasukedd"+str(x)+".png") for x in range(136,143)]+[image.load("Sasuke\\sasukedd"+str(x)+".png") for x in range(145,156)] 
        pics[7][5]=[image.load("Sasuke\\sasukea"+str(x)+".png") for x in range(1,18)]
        pics[7][6]=[image.load("Sasuke\\sasukee"+str(x)+".png") for x in range(4,20)]+[image.load("Sasuke\\sasukee"+str(x)+".png") for x in range(23,27)]+[image.load("Sasuke\\sasukee"+str(x)+".png") for x in range(44,62)]
        pics[7][7]=[image.load("Sasuke\\sasukedd"+str(x)+".png") for x in range(94,103)]
        pics[7][8]=[image.load("Sasuke\\sasukedd"+str(x)+".png") for x in range(80,86)]
        pics[7][9]=[image.load("Sasuke\\sasukedd"+str(x)+".png") for x in range(94,103)]+[image.load("Sasuke\\sasukedd"+str(x)+".png") for x in range(118,129)]
        pics[7][10]=[image.load("Sasuke\\sasukedd33.png")]
        pics[7][11]=[image.load("Sasuke\\sasukedd"+str(x)+".png") for x in range(12,19)]
        pics[7][12]="sasuke"
        pics[7][13]=image.load("Sasuke\\sasukedd2.png")
        pics[7][14]=[image.load("Sasuke\\sasukedd"+str(x)+".png") for x in range(46,61)]
    
    if firstplayer=="hokage" or secondplayer=="hokage":
        pics[8][0]=[image.load("hokage\\hokage 1"+str(x)+".png") for x in range(7,11)]
        pics[8][1]=[image.load("hokage\\hokage 1"+str(x)+".png") for x in range(30,36)]
        pics[8][2]=[image.load("hokage\\hokage 156.png")]
        pics[8][3]=[image.load("hokage\\jump"+str(x)+".png") for x in range(1,6)]
        pics[8][4]=[image.load("hokage\\hokage 1"+str(x)+".png") for x in range(138,149)] 
        pics[8][5]=[image.load("hokage\\hokage 1"+str(x)+".png") for x in range(190,205)]
        pics[8][6]=[image.load("hokage\\hokage 2"+str(x)+".png") for x in range(1,18)]
        pics[8][7]=[image.load("hokage\\hokage 1"+str(x)+".png") for x in range(71,75)]
        pics[8][8]=[image.load("hokage\\hokage 1"+str(x)+".png") for x in range(75,80)]
        pics[8][9]=[image.load("hokage\\hokage 1"+str(x)+".png") for x in range(71,80)]
        pics[8][10]=[image.load("hokage\\hokage 1192.png")]
        pics[8][11]=[image.load("hokage\\hokage 1"+str(x)+".png") for x in range(39,45)]
        pics[8][12]="hokage"
        pics[8][13]= image.load("hokage\\hokage mugshot.png")
        pics[8][14]=[image.load("hokage\\hokage 1" + str(x) + ".png") for x in range(51,57)]

#this list contains the different backgrounds, in each row the first element is the image of the background, the second row is the platform areas that player can jump on, the third element
#is the name of the music for that background.
backlist=[(image.load("Ninja Academy.png"),[Rect(234, 527, 277, 14),Rect(270, 415, 203, 16),Rect(305, 307, 142, 14),Rect(740, 306, 143, 13),Rect(706, 417, 206, 13),Rect(670, 526, 277, 15)],"academy.mp3"),
          (image.load("TrainingField.png"),[Rect(375, 542, 20, 9),Rect(490, 546, 25, 8),Rect(607, 544, 16, 11),Rect(16, 400, 132, 12),Rect(149, 391, 37, 19),Rect(190, 381, 22, 12),Rect(793, 380, 24, 12),Rect(830, 396, 61, 14),Rect(907, 398, 75, 20)],"training.mp3"),
          (image.load("valley of the end.png"),[Rect(3, 387, 63, 21),Rect(10, 596, 108, 13),Rect(335, 568, 67, 21),Rect(488, 628, 40, 17),Rect(626, 558, 44, 15),Rect(905, 607, 89, 19),Rect(913, 398, 82, 21),Rect(310, 469, 399, 16)],"valley.mp3"),
          (image.load("UchihaHideout.png"),[Rect(0, 489, 315, 16),Rect(683, 492, 316, 14)],"uchiha.mp3"),
          (image.load("ramen shop.png"),[Rect(0, 283, 138, 11),Rect(2, 452, 178, 9),Rect(435, 305, 200, 14),Rect(569, 333, 36, 15),Rect(405, 462, 287, 10),Rect(876, 284, 123, 12),Rect(855, 450, 144, 12),Rect(1, 120, 255, 6),Rect(361, 121, 363, 5),Rect(825, 121, 174, 6)],"ramen.mp3")]

#starting background
background = backlist[0][0]
platforms = backlist[0][1]
column=0

#the next few funtions are universal to all player1s, they are the basic movement and attacks

# this is a basic funtion, blits every picture in the stances row, there two different option,
#one where the character is facing right, the other is when they are faing left
def stance(x1,y1,direction,row):
    global frame,pics,parea #the "row" refers to which character it is, so first we go into character, than the 0 makes us go to the place with all the stanc pictures
    cpics = pics[row][0]

    if frame>len(cpics)-1: #when we blit every picture, we start over again
        frame=0

    if direction=="right":screen.blit( cpics[frame] ,(x1,y1-cpics[frame].get_size()[1])) #y1-cpics[frame].get_size()[1]), y1 is where the bottom of the feet should be, cpics[frame].get_size()[1]) gives us the picture length, so if we subtract them we get to top y, this is so the feet is always on the bottom

    else: screen.blit(transform.flip( cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1])) #facing left #transform.flip() flips all the pictures

    parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1]) #the player area, where the character is standing, used to see if they are being attacked

#this is the same as before except we have x+=3 and x-=3 so the character moves
def walk(x1,y1,direction,row):
    global frame,pics,x,parea
    cpics = pics[row][1]
    if frame>len(cpics)-1:
        frame=0
    if direction=="right":
        screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))
        x+=3
    else:
        screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
        x-=3
    parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])

#same as walk except character moves faster
def run(x1,y1,direction,row):
    global frame,pics,x,parea
    cpics = pics[row][11]
    if frame>len(cpics)-1:
        frame=0
    if direction=="right":
        screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))
        x+=5
    else:
        screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
        x-=5
    parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])

#blits only one picture, the crouch
def crouch(x1,y1,direction,row):
    global parea
    cpics = pics[row][2]
    if direction=="right":screen.blit(cpics[0],(x1,y1-cpics[0].get_size()[1]))
    else: screen.blit(transform.flip(cpics[0],x1,0),(x1,y1-cpics[0].get_size()[1]))
    parea=Rect(x1,y1-cpics[0].get_size()[1],cpics[0].get_size()[0],cpics[0].get_size()[1])

#same as stance except the end
def jump(x1,y1,direction,row):
    global pics,frame,jumpdone,parea,yvalue
    cpics = pics[row][3]
    if frame>len(cpics)-2:
        frame=len(cpics)-2 
    if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
    parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])  
    if y1>=yvalue: #when the character hits the ground again, the move stops. # yvalue is the value of the platform
        jumpdone=True #jumpdone tell us when the moves is done, so the player doesn't have to hold the key
    
#same as basic funtion with an attackarea
def punch(x1,y1,direction,row):
    global frame,pics,parea,attackarea
    cpics = pics[row][7]
    if frame>len(cpics)-1:
        frame=0
    if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
    parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    attackarea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1]) #to see if the opponent is in this area, if they are they loose health

def hardpunch(x1,y1,direction,row):
    global frame,pics,parea,attackarea,char
    cpics = pics[row][8]
    if frame>len(cpics)-1:
        frame=0
        move="stance"
        
    if char=="madara": #madara has a different punch than others
        if direction=="right":screen.blit(cpics[0],(x1,y1-cpics[0].get_size()[1]))#this is madara himself, the below picture is a dragon that moves forward
        else: screen.blit(transform.flip(cpics[0],x1,0),(x1,y1-cpics[0].get_size()[1]))
        if frame>0:
            if direction=="right":
                screen.blit(cpics[frame],(x1+10+frame*50,y1-cpics[frame].get_size()[1])) #his punch must move forward, so each time we incease the fram, we blit it further
                attackarea=Rect(x1+10+frame*50,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1]) 
            else:
                screen.blit(transform.flip(cpics[frame],x1-50-frame*50,0),(x1-50-frame*50,y1-cpics[frame].get_size()[1]))
                attackarea=Rect(x1-50-frame*50,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
        parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])

    else: #this part is same as punch
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))
        else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
        parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
        attackarea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])

#same as punch
def combo(x1,y1,direction,row):
    global frame,pics,parea,attackarea
    cpics = pics[row][9]
    if frame>len(cpics)-1:
        frame=0
    if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
    parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    attackarea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])

#this is if the player gets hitm, they fall down or move back based on the level of the attack
def takedamage(x1,y1,direction,row,dtype):
    global frame,pics,parea,attackarea,takedamagedonelevel1,takedamagedonelevel2,x,direc2
    cpics = pics[row][14]
    if dtype==1: #weak attack, only move back, don't fall
        if frame>1:
            frame=0

        if frame==0 or frame==1 or frame==2: #if the opponent is on the ground they should not move, in frames 0,1 and 2 the player is never down
            if direc2=="right": #if the opponent is attacking to the right than this player is going to fall to the right
                x+=1
            else:
                x-=1
            
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))
        else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
        parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])

        if frame>=1: #we only want the first few frames where the character moves back
            takedamagedonelevel1=True   #keeps track of wether the move is done
    else:
        if frame>len(cpics)-1:
            frame=0

        if frame==0 or frame==1 or frame==2: #if the opponent is on the ground they should not move, in frames 0,1 and 2 the player is never down
            if direc2=="right": #if the opponent is attacking to the right than this player is going to fall to the right
                x+=1
            else:
                x-=1
       
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))
        else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
        parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
        if frame+1==len(cpics): #if each picture in this is done, the move is over
            takedamagedonelevel2=True #keeps track of wether the move is done

#just blits one picture, the gaurd picture 
def guard(x1,y1,direction,row):
    global parea
    cpics = pics[row][10]
    if direction=="right":screen.blit(cpics[0],(x1,y1-cpics[0].get_size()[1]))
    else: screen.blit(transform.flip(cpics[0],x1,0),(x1,y1-cpics[0].get_size()[1]))
    parea=Rect(x1,y1-cpics[0].get_size()[1],cpics[0].get_size()[0],cpics[0].get_size()[1])
    
# Player 2 -------------------------------------------------------------------

#there is no need to comment player twos functions because they are the same as player one with different variables, most variables have a two after them

def stance2(x1,y1,direction,row):
    global frame2,pics,parea2
    cpics = pics[row2][0]
    if frame2>len(cpics)-1:
        frame2=0
    if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1])) #y1-cpics[frame].get_size()[1]), this allows us to blit all picture so that the bottom is at the y level(400)
    else: screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))
    parea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])

def walk2(x1,y1,direction,row):
    global frame2,pics,x2,parea2
    cpics = pics[row2][1]
    if frame2>len(cpics)-1:
        frame2=0
    if direction=="right":
        screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1]))
        x2+=3
    else:
        screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))
        x2-=3
    parea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])

def run2(x1,y1,direction,row):
    global frame2,pics,x2,parea2
    cpics = pics[row2][11]
    if frame2>len(cpics)-1:
        frame2=0
    if direction=="right":
        screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1]))
        x2+=5
    else:
        screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))
        x2-=5
    parea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    
def crouch2(x1,y1,direction,row):
    global parea2
    cpics = pics[row2][2]
    if direction=="right":screen.blit(cpics[0],(x1,y1-cpics[0].get_size()[1]))
    else: screen.blit(transform.flip(cpics[0],x1,0),(x1,y1-cpics[0].get_size()[1]))
    parea2=Rect(x1,y1-cpics[0].get_size()[1],cpics[0].get_size()[0],cpics[0].get_size()[1])

def guard2(x1,y1,direction,row):
    global parea2
    cpics = pics[row2][10]
    if direction=="right":screen.blit(cpics[0],(x1,y1-cpics[0].get_size()[1]))
    else: screen.blit(transform.flip(cpics[0],x1,0),(x1,y1-cpics[0].get_size()[1]))
    parea2=Rect(x1,y1-cpics[0].get_size()[1],cpics[0].get_size()[0],cpics[0].get_size()[1])

def jump2(x1,y1,direction,row):
    global pics,frame2,jumpdone2,parea2,yvalue2
    cpics = pics[row2][3]
    if frame2>len(cpics)-2:
        frame2=len(cpics)-2
    if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))
    if y1>=yvalue2:
        jumpdone2=True
    parea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
        
def punch2(x1,y1,direction,row):
    global frame2,pics,parea2,attackarea2
    cpics = pics[row2][7]
    if frame2>len(cpics)-1:
        frame2=0
    if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))
    parea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    attackarea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])

def hardpunch2(x1,y1,direction,row):
    global frame2,pics,parea2,attackarea2,char2
    cpics = pics[row2][8]
    if frame2>len(cpics)-1:
        frame2=0
        move2="stance"
        
    if char2=="madara":
        if direction=="right":screen.blit(cpics[0],(x1,y1-cpics[0].get_size()[1]))
        else: screen.blit(transform.flip(cpics[0],x1,0),(x1,y1-cpics[0].get_size()[1]))
        if frame2>0:
            if direction=="right":
                screen.blit(cpics[frame2],(x1+10+frame2*50,y1-cpics[frame2].get_size()[1]))
                attackarea2=Rect(x1+10+frame2*50,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
            else:
                screen.blit(transform.flip(cpics[frame2],x1-50-frame2*50,0),(x1-50-frame2*50,y1-cpics[frame2].get_size()[1]))
                attackarea2=Rect(x1-50-frame2*50,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
        parea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])

    else:
        if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1]))
        else: screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))
        parea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
        attackarea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])

def combo2(x1,y1,direction,row):
    global frame2,pics,parea2,attackarea2
    cpics = pics[row2][9]
    if frame2>len(cpics)-1:
        frame2=0
    if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))
    parea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    attackarea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])

def takedamage2(x1,y1,direction,row,dtype):
    global frame2,pics,parea2,takedamagedonelevel12,takedamagedonelevel22,x2,direc
    cpics = pics[row][14]
    if dtype==1:
        if frame2>1:
            frame2=0
            
        if frame2==0 or frame2==1 or frame2==2: 
            if direc=="right":
                x2+=1
            else:
                x2-=1
        if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1]))
        else: screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))
        parea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
        if frame2>=1:
            takedamagedonelevel12=True  
    else:
        if frame2>len(cpics)-1:
            frame2=0

        if frame2==0 or frame2==1 or frame2==2: 
            if direc=="right":
                x2+=1
            else:
                x2-=1
                
        if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1]))
        else: screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))
        parea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
        if frame2+1==len(cpics):
            takedamagedonelevel22=True

#-----------------------------------------------------

#collision is when two special attacks collide, then those two moves stop and there is an explosion
def collision(x1,y1):
    global collision,screencopy
    for i in collisionl: #this way the characters can't move while this is happening
        screen.blit(screencopy,(0,0))
        screen.blit(i,(x1,y1-i.get_size()[1]))
        display.flip()
        time.wait(50)

#special moves: most special moves are different so each one requires it own code
#each character has three special moves, but they need six function, 3 for player one and three for player two
#the attack done variables keep track of the attack, so if the character presses the attack key once it continues till it is over

#this is same as the basic functions, except he moves in some frames so we change the x
def narutoattack1(x1,y1,direction):
    global frame,pics,count,attack1done,x,attackarea
    cpics = pics[0][4]
    if frame>len(cpics)-2:
        frame=len(cpics)-2
    if frame>=7:
        if direc=="right": x+=10
        else: x-=10
    if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
    if frame>=7:
         attackarea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    count+=1
    if count==150: #after a while the move will stop, count keeps track of the time of this move in action
        attack1done=True
        count=0

#till the 43 frame, the character does a few movements, than after that the ball moves towards the opponent in a linear fashion
#that is, the ball moves only on the ground does not go up and down
def narutoattack2(x1,y1,direction):
    global frame,pics,first,rincrease,lincrease,count,attack2done,attackarea,x,x2
    cpics = pics[0][5]
    if first: #when the player first clicks the key to launch the move first becomes true, so we can reset a few variables
        frame=0
        rincrease=0 #to see where the ball shoud go
        lincrease=0
    if frame<=43: #the first 43 frames
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
    else:
        if direction=="right":
            screen.blit(cpics[42],(x1,y1-cpics[42].get_size()[1]))
            screen.blit(cpics[44+frame%4],(x1+rincrease,y1-cpics[44+frame%4].get_size()[1])) # we use 44+frame%4 because we want to keep repeating the 44,45,46 and 47 frame to give the ball a spinning effect
            attackarea=Rect(x1+rincrease,y1-cpics[44+frame%4].get_size()[1],cpics[44+frame%4].get_size()[0],cpics[44+frame%4].get_size()[1])
            rincrease+=(x2-(x1+rincrease))/15.0 #x2 is the opponents x xoordinate, x1 is the players, this makes the ball move closer and closer to the player, ideally in 15 frames
        else:
            screen.blit(transform.flip(cpics[42],x1,0),(x1,y1-cpics[42].get_size()[1]))
            screen.blit(cpics[44+frame%4],(x1+lincrease,y1-cpics[44+frame%4].get_size()[1]))
            attackarea=Rect(x1+lincrease,y1-cpics[44+frame%4].get_size()[1],cpics[44+frame%4].get_size()[0],cpics[44+frame%4].get_size()[1])
            lincrease+=(x2-(x1+lincrease))/15.0
    if frame>70:
        attack2done=True
        rincrease,lincrease=0,0

#once again till the 43 frame the character does movements then he spins a appears in front of the character and hit the character with a ball
#
def narutoattack3(x1,y1,direction):
    global frame,pics,first,attack3done,attackarea,x2,y2,x
    cpics = pics[0][6]
    if frame==35: 
       x=x2-100
       x1=x #the oppinents postitions where we want to hit
    if first:
        frame=0
    if frame==44: #want to skip a few frames
        frame=48
    if frame<=43:
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
    elif frame!=36 and frame!=37 and frame!=35:
        if direction=="right":
            screen.blit(cpics[46],(x1,y1-cpics[46].get_size()[1])) #image of the character 
            screen.blit(cpics[frame],(x1+50,y1-cpics[frame].get_size()[1])) #image of the ball infront of opponent
            attackarea=Rect(x1+50,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
        else:
            screen.blit(transform.flip(cpics[46],x1,0),(x1,y1-cpics[46].get_size()[1]))
            screen.blit(cpics[frame],(x1-100,y1-cpics[frame].get_size()[1]))
            attackarea=Rect(x1-100,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    if frame+1==len(cpics):
        attack3done=True

#once again i won't comment player 2's because they are same as player one with different variables

def narutoattack12(x1,y1,direction):
    global frame2,pics,count,attack1done2,x2,attackarea2
    cpics = pics[0][4]
    if frame2>len(cpics)-2:
        frame2=len(cpics)-2
    if frame2>=7:
        if direction=="right": x2+=10
        else:  x2-=10
    if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))
    if frame2>=7:
         attackarea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    if x2<0 or x2>1000:
        attack1done2=True
        
def narutoattack22(x1,y1,direction):
    global frame2,pics,first2,rincrease2,lincrease2,attack2done2,attackarea2,x
    cpics = pics[0][5]
    if first2:
        frame2=0
        rincrease2=0
        lincrease2=0
    if frame2<=43:
        if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))
    else:
        if direction=="right":
            screen.blit(cpics[42],(x1,y1-cpics[42].get_size()[1]))
            screen.blit(cpics[44+frame2%4],(x1+rincrease2,y1-cpics[44+frame2%4].get_size()[1]))
            attackarea2=Rect(x1+rincrease2,y1-cpics[44+frame2%4].get_size()[1],cpics[44+frame2%4].get_size()[0],cpics[44+frame2%4].get_size()[1])
            rincrease2+=(x-(x1+rincrease2))/15.0
            
        else:
            screen.blit(transform.flip(cpics[42],x1,0),(x1,y1-cpics[42].get_size()[1]))
            screen.blit(cpics[44+frame2%4],(x1+lincrease2,y1-cpics[44+frame2%4].get_size()[1]))
            attackarea2=Rect(x1+lincrease2,y1-cpics[44+frame2%4].get_size()[1],cpics[44+frame2%4].get_size()[0],cpics[44+frame2%4].get_size()[1])
            lincrease2+=(x-(x1+lincrease2))/15.0
            
    if frame2>70:
        attack2done2=True
        rincrease2,lincrease2=0,0
    

def narutoattack32(x1,y1,direction):
    global frame2,pics,first2,attack3done2,attackarea2,x2,x
    cpics = pics[0][6]
    if frame2==35:
       x2=x-100
       x1=x2
    if first2:
        frame2=0
    if frame2==44:
        frame2=48
    if frame2<=43:
        if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))
    elif frame2!=36 and frame2!=37 and frame2!=35:
        if direction=="right":
            screen.blit(cpics[46],(x1,y1-cpics[46].get_size()[1]))
            screen.blit(cpics[frame2],(x1+50,y1-cpics[frame2].get_size()[1]))
            attackarea2=Rect(x1+50,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
        else:
            screen.blit(transform.flip(cpics[46],x1,0),(x1,y1-cpics[46].get_size()[1]))
            screen.blit(cpics[frame2],(x1-100,y1-cpics[frame2].get_size()[1]))
            attackarea2=Rect(x1-100,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    if frame2+1==len(cpics):
        attack3done2=True

#this is same as narutoattack2, exept we wait till frame 18
def kisameattack1(x1,y1,direction):
    global frame,pics,attack1done,rincrease,lincrease,count,attackarea
    cpics=pics[1][4]
    if first:
        frame=0
        rincrease=50
        lincrease=100
    if frame<=18:
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
    else:
        if direction=="right":
            screen.blit(cpics[7],(x1,y1-cpics[7].get_size()[1]))
            screen.blit(cpics[18+frame%4],(x1+rincrease,y1-cpics[18+frame%4].get_size()[1]))
            attackarea=Rect(x1+rincrease,y1-cpics[18+frame%4].get_size()[1],cpics[18+frame%4].get_size()[0],cpics[18+frame%4].get_size()[1])
            rincrease+=6
        else:
            screen.blit(transform.flip(cpics[7],x1,0),(x1,y1-cpics[7].get_size()[1]))
            screen.blit(transform.flip(cpics[18+frame%4],x1,0),(x1-lincrease,y1-cpics[18+frame%4].get_size()[1]))
            attackarea=Rect(x1-lincrease,y1-cpics[18+frame%4].get_size()[1],cpics[18+frame%4].get_size()[0],cpics[18+frame%4].get_size()[1])
            lincrease+=6
    count+=1
    if count>200:
        attack1done=True
        count=0
        rincrease=0
        lincrease=0

#basic function, blit ever picture in the set
def kisameattack2(x1,y1,direction):
    global frame,pics,attack2done,attackarea
    cpics = pics[1][5]
    if frame>len(cpics)-1:
        frame=0
    if direction=="right":screen.blit(cpics[frame],(x1-((cpics[frame].get_size()[0])/2.0),y1-cpics[frame].get_size()[1])) #(x1-((cpics[frame].get_size()[0])/2.0), since the sharks come around him, he has to stay in the middle, this is what it does
    else: screen.blit(transform.flip(cpics[frame],x1,0),((x1-((cpics[frame].get_size()[0])/2.0),y1-cpics[frame].get_size()[1])))
    attackarea=Rect((x1-((cpics[frame].get_size()[0])/2.0),y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1]))
    if frame+1==len(cpics):
        attack2done =True
    
#basic function, blit ever picture in the set
def kisameattack3(x1,y1,direction):
    global frame,pics,attack3done,attackarea
    cpics = pics[1][6]
    if frame>len(cpics)-1:
        frame=0
    if direction=="right":screen.blit(cpics[frame],(x1-((cpics[frame].get_size()[0])/2.0),y1-cpics[frame].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame],x1,0),((x1-((cpics[frame].get_size()[0])/2.0),y1-cpics[frame].get_size()[1])))
    attackarea=Rect((x1-((cpics[frame].get_size()[0])/2.0),y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1]))
    if frame+1==len(cpics):
        attack3done =True

def kisameattack12(x1,y1,direction):
    global frame2,pics,attack1done2,rincrease2,lincrease2,count2,attackarea2
    cpics=pics[1][4]
    if first:
        frame=0
        rincrease=50
        lincrease=100
    if frame2<=18:
        if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))
    else:
        if direction=="right":
            screen.blit(cpics[7],(x1,y1-cpics[7].get_size()[1]))
            screen.blit(cpics[18+frame2%4],(x1+rincrease2,y1-cpics[18+frame2%4].get_size()[1]))
            attackarea2=Rect(x1+rincrease2,y1-cpics[18+frame2%4].get_size()[1],cpics[18+frame2%4].get_size()[0],cpics[18+frame2%4].get_size()[1])
            rincrease2+=6
        else:
            screen.blit(transform.flip(cpics[7],x1,0),(x1,y1-cpics[7].get_size()[1]))
            screen.blit(transform.flip(cpics[18+frame2%4],x1,0),(x1-lincrease2,y1-cpics[18+frame2%4].get_size()[1]))
            attackarea2=Rect(x1-lincrease2,y1-cpics[18+frame2%4].get_size()[1],cpics[18+frame2%4].get_size()[0],cpics[18+frame2%4].get_size()[1])
            lincrease2+=6
    count2+=1
    if count2>200:
        attack1done2=True
        count2=0
        rincrease2=0
        lincrease2=0

def kisameattack22(x1,y1,direction):
    global frame2,pics,attack2done2,attackarea2
    cpics = pics[1][5]
    if frame2>len(cpics)-1:
        frame2=0
    if direction=="right":screen.blit(cpics[frame2],(x1-((cpics[frame2].get_size()[0])/2.0),y1-cpics[frame2].get_size()[1])) #(x1-((cpics[frame2].get_size()[0])/2.0), since the sharks come around him, he has to stay in the middle, this is what it does
    else: screen.blit(transform.flip(cpics[frame2],x1,0),((x1-((cpics[frame2].get_size()[0])/2.0),y1-cpics[frame2].get_size()[1])))
    attackarea2=Rect((x1-((cpics[frame2].get_size()[0])/2.0),y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1]))
    if frame2+1==len(cpics):
        attack2done2 =True
    

def kisameattack32(x1,y1,direction):
    global frame2,pics,attack3done2,attackarea2
    cpics = pics[1][6]
    if frame2>len(cpics)-1:
        frame2=0
    if direction=="right":screen.blit(cpics[frame2],(x1-((cpics[frame2].get_size()[0])/2.0),y1-cpics[frame2].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame2],x1,0),((x1-((cpics[frame2].get_size()[0])/2.0),y1-cpics[frame2].get_size()[1])))
    attackarea2=Rect((x1-((cpics[frame2].get_size()[0])/2.0),y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1]))
    if frame2+1==len(cpics):
        attack3done2 =True

#this attack is two picture parts, the character is standing and in front of him a flame appears
def madaraattack1(x1,y1,direction):
    global frame,pics,first,attack1done,attackarea
    cpics = pics[2][4]
    if frame>len(cpics)-1:
        frame=0
    if frame<=0: #the first picture is just character
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
    else:
        if direction=="right":
            screen.blit(cpics[0],(x1,y1-cpics[0].get_size()[1])) #character standing
            screen.blit(cpics[frame],(x1+50,y1-cpics[frame].get_size()[1])) #flame appearing infront of him, so x1+50
            attackarea=Rect(x1+50,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
        else:
            screen.blit(transform.flip(cpics[0],x1,0),(x1,y1-cpics[0].get_size()[1]))
            screen.blit(transform.flip(cpics[frame],x1,0),(x1-150,y1-cpics[frame].get_size()[1])) #has to travel behind picture after transformation, so -150
            attackarea=Rect(x1-100,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
            
    if frame+1==len(cpics): #end of set, leads to end of attack
        attack1done=True

countmadara=0 #for some reason we substituted first with this for this guy
#first part blit character, second, blit fox in front of him, third blit hands comming out at opponents position
def madaraattack2(x1,y1,direction):
    global frame,pics,attack2done,attackarea,x2,countmadara,x5
    cpics = pics[2][5]
    if countmadara==0: #could have gone if first
        x5=x2 #gets positions of opponent
        countmadara=5
    if frame>len(cpics)-1:
        frame=0
        
    if direction=="right": screen.blit(cpics[0],(x1,y1-cpics[0].get_size()[1])) #character
    else: screen.blit(transform.flip(cpics[0],x1,0),(x1,y1-cpics[0].get_size()[1]))
    
    if frame==1:
        if direction=="right": screen.blit(cpics[1],(x1+50,y1-cpics[1].get_size()[1])) #fox part1
        else: screen.blit(transform.flip(cpics[1],x1-100,0),(x1-100,y1-cpics[1].get_size()[1]))

    if frame>1:
        if direction=="right": screen.blit(cpics[2],(x1+50,y1-cpics[2].get_size()[1]))  #fox part2
        else: screen.blit(transform.flip(cpics[2],x1-100,0),(x1-100,y1-cpics[2].get_size()[1]))

    if frame>2:
         if direction=="right":
        
             screen.blit(cpics[frame],(x5,y1-cpics[frame].get_size()[1]+5))  #bltiing hands at position of opponent
             attackarea=Rect(x5,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
         else:
             
             screen.blit(transform.flip(cpics[frame],x5,0),(x5,y1-cpics[frame].get_size()[1]))
             attackarea=Rect(x5,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
         
    if frame+1==len(cpics):
        attack2done =True
        countmadara=0

#like madaraattack1

def madaraattack3(x1,y1,direction):
    global frame,pics,attack3done,attackarea
    cpics = pics[2][6]
    if first:
        frame=0
    if frame<6:
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1])) #character hand signs
        else: screen.blit(transform.flip(cpics[frame],x1,0),((x1,y1-cpics[frame].get_size()[1])))
    else:
        if direction=="right":screen.blit(cpics[5],(x1,y1-cpics[5].get_size()[1])) #bliting character
        else: screen.blit(transform.flip(cpics[5],x1,0),((x1,y1-cpics[5].get_size()[1])))
        
        if direction=="right":
            screen.blit(cpics[6+frame%3],(x1+50,y1-cpics[6+frame%3].get_size()[1])) #bliting a ball in front of him, use mod to repeat frames to animate ball
            attackarea=Rect((x1+50,y1-cpics[6+frame%3].get_size()[1],cpics[6+frame%3].get_size()[0],cpics[6+frame%3].get_size()[1]))
        else:
            screen.blit(transform.flip(cpics[6+frame%3],x1-150,0),((x1-150,y1-cpics[6+frame%3].get_size()[1])))
            attackarea=Rect((x1-150,y1-cpics[6+frame%3].get_size()[1],cpics[6+frame%3].get_size()[0],cpics[6+frame%3].get_size()[1]))

    if frame>20: #longer than it looks
        attack3done =True
        
def madaraattack12(x1,y1,direction):
    global frame2,pics,first,attack1done2,attackarea2
    cpics = pics[2][4]
    if frame2>len(cpics)-1:
        frame2=0
    if frame2<=0:
        if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))
    else:
        if direction=="right":
            screen.blit(cpics[0],(x1,y1-cpics[0].get_size()[1]))
            screen.blit(cpics[frame2],(x1+50,y1-cpics[frame2].get_size()[1]))
            attackarea2=Rect(x1+50,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
        else:
            screen.blit(transform.flip(cpics[0],x1,0),(x1,y1-cpics[0].get_size()[1]))
            screen.blit(transform.flip(cpics[frame2],x1,0),(x1-150,y1-cpics[frame2].get_size()[1]))
            attackarea2=Rect(x1-100,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
            
    if frame2+1==len(cpics):
        attack1done2=True

def madaraattack22(x1,y1,direction):
    global frame2,pics,attack2done2,attackarea2,framedelay2,x,x5,countmadara
    cpics = pics[2][5]
    if countmadara==0:
        x5=x
        countmadara=5
    if frame2>len(cpics)-1:
        frame2=0
        
    if direction=="right": screen.blit(cpics[0],(x1,y1-cpics[0].get_size()[1]))
    else: screen.blit(transform.flip(cpics[0],x1,0),(x1,y1-cpics[0].get_size()[1]))
    
    if frame2==1:
        if direction=="right": screen.blit(cpics[1],(x1+50,y1-cpics[1].get_size()[1]))
        else: screen.blit(transform.flip(cpics[1],x1-100,0),(x1-100,y1-cpics[1].get_size()[1]))

    if frame2>1:
        if direction=="right": screen.blit(cpics[2],(x1+50,y1-cpics[2].get_size()[1]))
        else: screen.blit(transform.flip(cpics[2],x1-100,0),(x1-100,y1-cpics[2].get_size()[1]))

    if frame2>2:
         if direction=="right":
             #screen.blit(cpics[frame2],(x1+50*frame2,y1-cpics[frame2].get_size()[1]))
             #attackarea2=Rect(x1+50,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
             screen.blit(cpics[frame2],(x,y1-cpics[frame2].get_size()[1]+5))
             attackarea2=Rect(x5,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
         else:
             #screen.blit(transform.flip(cpics[frame2],x1-50*frame2,0),(x1-50*frame2,y1-cpics[frame2].get_size()[1]))
             #attackarea2=Rect(x1-50*frame2,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
             screen.blit(transform.flip(cpics[frame2],x5,0),(x5,y1-cpics[frame2].get_size()[1]))
             attackarea2=Rect(x5,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
         
    if frame2+1==len(cpics):
        attack2done2 =True
        countmadara=0


def madaraattack32(x1,y1,direction):
    global frame2,pics,attack3done2,attackarea2
    cpics = pics[2][6]
    if first:
        frame2=0
    if frame2<6:
        if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1]))
        else: screen.blit(transform.flip(cpics[frame2],x1,0),((x1,y1-cpics[frame2].get_size()[1])))
    else:
        if direction=="right":screen.blit(cpics[5],(x1,y1-cpics[5].get_size()[1]))
        else: screen.blit(transform.flip(cpics[5],x1,0),((x1,y1-cpics[5].get_size()[1])))
        
        if direction=="right":
            screen.blit(cpics[6+frame2%3],(x1+50,y1-cpics[6+frame2%3].get_size()[1]))
            attackarea2=Rect((x1+50,y1-cpics[6+frame2%3].get_size()[1],cpics[6+frame2%3].get_size()[0],cpics[6+frame2%3].get_size()[1]))
        else:
            screen.blit(transform.flip(cpics[6+frame2%3],x1-150,0),((x1-150,y1-cpics[6+frame2%3].get_size()[1])))
            attackarea2=Rect((x1-150,y1-cpics[6+frame2%3].get_size()[1],cpics[6+frame2%3].get_size()[0],cpics[6+frame2%3].get_size()[1]))

    if frame2>20: #longer than it looks
        attack3done2 =True

if counter==0:
    summond=15 #used to move things
    counter=1

#like narutoattack1 except we use summond instead of rincrease and lincrease
def kakashiattack1 (x1,y1,direction):
    global frame,pics,attack1done,attackarea,summond,first
    cpics = pics[3][4]
    if first:
        summond=15
    if frame<12:
        if direction=="right":screen.blit(cpics[frame%12],(x1,y1-cpics[frame%12].get_size()[1]))
        else:screen.blit(transform.flip(cpics[frame%12],x1,0),(x1,y1-cpics[frame%12].get_size()[1]))
    if frame>11:
        if direction=="right":
            screen.blit(dogs[frame%3],(x1+summond,y1-dogs[frame%3].get_size()[1]))
            screen.blit(cpics[11],(x1,y1-cpics[11].get_size()[1]))
            attackarea=Rect((x1+summond,y1-dogs[frame%3].get_size()[1],dogs[frame%3].get_size()[0],dogs[frame%3].get_size()[1]))
            summond+=15
        else:
            screen.blit(transform.flip(dogs[frame%3],x1+summond,0),(x1+summond,y1-dogs[frame%3].get_size()[1]))
            screen.blit(transform.flip(cpics[11],x1,0),(x1,y1-cpics[11].get_size()[1]))
            attackarea=Rect((x1+summond,y1-dogs[frame%3].get_size()[1],dogs[frame%3].get_size()[0],dogs[frame%3].get_size()[1]))
            summond-=15
    if x1+summond>999 or x1+summond<0:
        attack1done=True
        summond=15

#same as kakashiattack1
def kakashiattack2 (x1,y1,direction):
    global frame,pics,attack2done,attackarea,summond,first
    if first:
        summond=15
    cpics = pics[3][5]
    c2pics=pics[3][4]
    if frame<12:
        if direction=="right":screen.blit(c2pics[frame%12],(x1,y1-c2pics[frame%12].get_size()[1]))
        else:screen.blit(transform.flip(c2pics[frame%12],x1,0),(x1,y1-c2pics[frame%12].get_size()[1]))
    if frame>11:
        if direction=="right":
            screen.blit(cpics[frame%9],(x1+summond,y1-cpics[frame%9].get_size()[1]))
            screen.blit(c2pics[11],(x1,y1-c2pics[11].get_size()[1]))
            attackarea=Rect((x1+summond,y1-dogs[frame%3].get_size()[1],dogs[frame%3].get_size()[0],dogs[frame%3].get_size()[1]))
            summond+=15
        else:
            screen.blit(transform.flip(cpics[frame%9],x1+summond,0),(x1+summond,y1-cpics[frame%9].get_size()[1]))
            screen.blit(transform.flip(c2pics[11],x1,0),(x1,y1-c2pics[11].get_size()[1]))
            attackarea=Rect((x1+summond,y1-dogs[frame%3].get_size()[1],dogs[frame%3].get_size()[0],dogs[frame%3].get_size()[1]))
            summond-=15
    if x1+summond>999 or x1+summond<0:
        attack2done=True
        summond=15

#does hand signs, teleports infront of opponent and attacks
def kakashiattack3 (x1,y1,direction):
    global frame,pics,attack3done,attackarea,x2,x,q
    if frame==22: #teleporst at frame 22
        x=x2-50
        x1=x #gets opponent position
    cpics = pics[3][6]
    if direction=="right":screen.blit(cpics[frame%28],(x1,y1-cpics[frame%28].get_size()[1])) #hand signs
    if direction=="left":
        if frame>21:
            screen.blit(transform.flip(cpics[frame%28],x1,0),(x1+75,y1-cpics[frame%28].get_size()[1]))
            
        else:
            screen.blit(transform.flip(cpics[frame%28],x1,0),(x1,y1-cpics[frame%28].get_size()[1]))
            
    if frame>21:
        attackarea=Rect((x1,y1-cpics[frame%28].get_size()[1],cpics[frame%28].get_size()[0],cpics[frame%28].get_size()[1])) #teleports infront of opponent
    if frame>26:
        attack3done=True
        x=x+75


if counter2==0:
    summond2=15
    counter2=1
    
def kakashiattack12 (x1,y1,direction):
    global frame2,pics,attack1done2,attackarea2,summond2,first2
    if first2:
        summond2=15
    cpics = pics[3][4]
    #if frame2>len(cpics):
    #    frame2=0
    if frame2<12:
        if direc2=="right":screen.blit(cpics[frame2%12],(x1,y1-cpics[frame2%12].get_size()[1]))
        else:screen.blit(transform.flip(cpics[frame2%12],x1,0),(x1,y1-cpics[frame2%12].get_size()[1]))
    if frame2>11:
        if direc2=="right":
            screen.blit(dogs[frame2%3],(x1+summond2,y1-dogs[frame2%3].get_size()[1]))
            screen.blit(cpics[11],(x1,y1-cpics[11].get_size()[1]))
            attackarea2=Rect((x1+summond2,y1-dogs[frame2%3].get_size()[1],dogs[frame2%3].get_size()[0],dogs[frame2%3].get_size()[1]))
            summond2+=15
        else:
            screen.blit(transform.flip(dogs[frame2%3],x1+summond2,0),(x1+summond2,y1-dogs[frame2%3].get_size()[1]))
            screen.blit(transform.flip(cpics[11],x1,0),(x1,y1-cpics[11].get_size()[1]))
            attackarea2=Rect((x1+summond2,y1-dogs[frame2%3].get_size()[1],dogs[frame2%3].get_size()[0],dogs[frame2%3].get_size()[1]))
            summond2-=15
    if x1+summond2>999 or x1+summond2<0:
        attack1done2=True
        summond2=15
        
def kakashiattack22 (x1,y1,direction):
    global frame2,pics,attack2done2,attackarea2,summond2,dogs,first2
    if first2:
        summond2=15
    cpics = pics[3][5]
    c2pics=pics[3][4]
    if frame2<12:
        if direc2=="right":screen.blit(c2pics[frame2%12],(x1,y1-c2pics[frame2%12].get_size()[1]))
        else:screen.blit(transform.flip(c2pics[frame2%12],x1,0),(x1,y1-c2pics[frame2%12].get_size()[1]))
    if frame2>11:
        if direc2=="right":
            screen.blit(cpics[frame2%9],(x1+summond2,y1-cpics[frame2%9].get_size()[1]))
            screen.blit(c2pics[11],(x1,y1-c2pics[11].get_size()[1]))
            attackarea2=Rect((x1+summond2,y1-dogs[frame2%3].get_size()[1],dogs[frame2%3].get_size()[0],dogs[frame2%3].get_size()[1]))
            summond+=15
        else:
            screen.blit(transform.flip(cpics[frame2%9],x1+summond2,0),(x1+summond2,y1-cpics[frame2%9].get_size()[1]))
            screen.blit(transform.flip(c2pics[11],x1,0),(x1,y1-c2pics[11].get_size()[1]))
            attackarea2=Rect((x1+summond2,y1-dogs[frame2%3].get_size()[1],dogs[frame2%3].get_size()[0],dogs[frame2%3].get_size()[1]))
            summond2-=15
    if x1+summond2>999 or x1+summond2<0:
        attack2done2=True
        summond2=15

def kakashiattack32 (x1,y1,direction):
    global frame2,pics,attack3done2,attackarea2,x2,x,q
    if frame2==22:
        x2=x-50
        x1=x2
    cpics = pics[3][6]
    if direc2=="right":screen.blit(cpics[frame2%28],(x1,y1-cpics[frame2%28].get_size()[1]))
    if direc2=="left":
        if frame2>21:
            screen.blit(transform.flip(cpics[frame2%28],x1,0),(x1+75,y1-cpics[frame2%28].get_size()[1]))
            
        else:
            screen.blit(transform.flip(cpics[frame2%28],x1,0),(x1,y1-cpics[frame2%28].get_size()[1]))
            
    if frame2>21:
        attackarea2=Rect((x1,y1-cpics[frame2%28].get_size()[1],cpics[frame2%28].get_size()[0],cpics[frame2%28].get_size()[1]))
    if frame2>26:
        attack3done2=True
        x2=x2+75

#basic function blit everything around a center, like kisameattack2
        
def gaaraattack1(x1,y1,direction):
    global frame,pics,attack1done,attackarea,first
    cpics = pics[4][4]
    if first:
        frame=0
    if direction=="right":screen.blit(cpics[frame],(x1-((cpics[frame].get_size()[0])/2.0),y1-cpics[frame].get_size()[1])) 
    else: screen.blit(transform.flip(cpics[frame],x1,0),((x1-((cpics[frame].get_size()[0])/2.0),y1-cpics[frame].get_size()[1])))
    attackarea=Rect((x1-((cpics[frame].get_size()[0])/2.0),y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1]))
    if frame+1==len(cpics):
        attack1done =True

attackcoordinatex,attackcoordinatey=0,0

def gaaraattack2(x1,y1,direction):
    global frame,pics,attack2done,attackarea,x2,y2,yvalue,first,attackcoordinatex,attackcoordinatey,parea2,health2

    #the basis of this attack is that the sand appears below the character if the character is within the attackarea on the 31 frame, they become trapped within the ball and get hurt
    # so if the character moves out of the way before the 31 frame, then they are free. Else, they get trapped in a bubble of sand, so we make the opponent dissappear by bliting them
    #somewhere not on the map. But the problem is, is they are not on the screen, they are not within the attack area and therefore they won't lose any health. So this code manually
    #takes away the opponents health. Also we reset the attack area so the don't lose health in the while loop if some how the attack area collides with them. There is a case when the
    #attackarea collides with the player, we know why.
    
    cpics = pics[4][5]
    
    if first:
        frame=0
        attackcoordinatex=x2 #opponents coordinates
        attackcoordinatey=y2
       
    if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1])) #bliting character
    else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))

    
    if direction=="right":screen.blit(cpics[frame+21],(attackcoordinatex-25,attackcoordinatey-cpics[frame+21].get_size()[1])) #the ball
    else: screen.blit(transform.flip(cpics[frame+21],attackcoordinatex-25,0),(attackcoordinatex-25,attackcoordinatey-cpics[frame+21].get_size()[1]))     
        
    attackarea=Rect(attackcoordinatex-25,attackcoordinatey-cpics[frame+21].get_size()[1],cpics[frame+21].get_size()[0],cpics[frame+21].get_size()[1])

    if frame+21==31 and parea2.colliderect(attackarea): # we give them a chance to escape, on the this frame, if they are still here we trap them in the bubble
        x2=-100 #this is so the character dissappears, so it looks like they are trapped in the bubble
        y2=-100
    elif frame+21>31: #taking away health after they are trapped in the bubble
        health2-=2.5

    
    
    attackarea=Rect(0,0,0,0) #reset attackarea
        
    if frame+21==39:
        attack2done=True
        if x2==-100 and y2==-100:
            y2=yvalue
            x2=attackcoordinatex
            
#a gian monster appears, conjures up a ball and this ball goes toward the opponent on a 2d plane, goes up and down and left an right
def gaaraattack3(x1,y1,direction):
    global frame,pics,attack3done,attackarea,rincrease,ryincrease,x2,y2,first
    
    cpics = pics[4][6]
    
    if first:
        frame=0
        if direction=="right":
            rincrease,ryincrease=80,y1-cpics[9].get_size()[1]+100 #postition where ball is conjured
        else:
            rincrease,ryincrease=791,y1-cpics[9].get_size()[1]+100
        
    if frame<=8:
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1])) #the monster comming
        else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))

    elif frame<=16:
        if direction=="right":screen.blit(cpics[9],(0,y1-cpics[9].get_size()[1])) #the monster stays
        else: screen.blit(transform.flip(cpics[9],741,0),(741,y1-cpics[9].get_size()[1]))

        if direction=="right":screen.blit(cpics[frame],(80,y1-cpics[9].get_size()[1]+100)) #sonjurign th ball
        else: screen.blit(transform.flip(cpics[frame],791,0),(791,y1-cpics[9].get_size()[1]+100))
        
    else:
        #the ball follows the character (like example from good guy, bad guy ship)
        if x2<rincrease: 
            rincrease-=5
        elif x2>rincrease:
            rincrease+=5
        if y2<ryincrease:
            ryincrease-=5
        elif y2>ryincrease:
            ryincrease+=5

        if direction=="right":screen.blit(cpics[9],(0,y1-cpics[9].get_size()[1])) #the monster
        else: screen.blit(transform.flip(cpics[9],741,0),(741,y1-cpics[9].get_size()[1])) 

        if direction=="right":screen.blit(cpics[15],(rincrease,ryincrease-cpics[15].get_size()[1])) #bliting the ball
        else: screen.blit(transform.flip(cpics[15],rincrease,0),(rincrease,ryincrease-cpics[15].get_size()[1]))
        
        attackarea=Rect(rincrease,ryincrease-cpics[15].get_size()[1],cpics[15].get_size()[0],cpics[15].get_size()[1])

    if frame>60:
        attack3done=True
        rincrease,ryincrease=0,0


#GAARA PLAYER 2
        
def gaaraattack12(x1,y1,direction):
    global frame2,pics,attack1done2,attackarea2,first2
    cpics = pics[4][4]
    if first2:
        frame2=0
    if direction=="right":screen.blit(cpics[frame2],(x1-((cpics[frame2].get_size()[0])/2.0),y1-cpics[frame2].get_size()[1])) 
    else: screen.blit(transform.flip(cpics[frame2],x1,0),((x1-((cpics[frame2].get_size()[0])/2.0),y1-cpics[frame2].get_size()[1])))
    attackarea2=Rect((x1-((cpics[frame2].get_size()[0])/2.0),y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1]))
    if frame2+1==len(cpics):
        attack1done2 =True

attackcoordinatex2,attackcoordinatey2=0,0

def gaaraattack22(x1,y1,direction):
    global frame2,pics,attack2done2,attackarea2,x,y,yvalue2,first2,attackcoordinatex2,attackcoordinatey2,parea,health

    #the same as gaaraattack2, but with different variables for player 2

    cpics = pics[4][5]
    
    if first2:
        frame2=0
        attackcoordinatex2=x
        attackcoordinatey2=y
        
    if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))

    if direction=="right":screen.blit(cpics[frame2+21],(attackcoordinatex2-25,attackcoordinatey2-cpics[frame2+21].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame2+21],attackcoordinatex2-25,0),(attackcoordinatex2-25,attackcoordinatey2-cpics[frame2+21].get_size()[1]))
    
    attackarea2=Rect(attackcoordinatex2-25,attackcoordinatey2-cpics[frame2+21].get_size()[1],cpics[frame2+21].get_size()[0],cpics[frame2+21].get_size()[1])

    if frame2+21==31 and parea.colliderect(attackarea2):
        x = -100
        y = -100

    elif frame2+21>31:
        health-=2.5
        
         
    attackarea2=Rect(0,0,0,0)
        
    if frame2+21==39:
        attack2done2=True
        if x==-100 and y==-100:
            y=yvalue2
            x=attackcoordinatex2

def gaaraattack32(x1,y1,direction):
    global frame2,pics,attack3done2,attackarea2,rincrease2,ryincrease2,x,y,first2
    
    cpics = pics[4][6]
    
    if first2:
        frame2=0
        if direction=="right":
            rincrease2,ryincrease2=80,y1-cpics[9].get_size()[1]+100
        else:
            rincrease2,ryincrease2=791,y1-cpics[9].get_size()[1]+100
        
    if frame2<=8:
        if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1]))
        else: screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))
    elif frame2<=16:
        if direction=="right":screen.blit(cpics[9],(0,y1-cpics[9].get_size()[1]))
        else: screen.blit(transform.flip(cpics[9],741,0),(741,y1-cpics[9].get_size()[1]))

        if direction=="right":screen.blit(cpics[frame2],(80,y1-cpics[9].get_size()[1]+100))
        else: screen.blit(transform.flip(cpics[frame2],791,0),(791,y1-cpics[9].get_size()[1]+100))
    else:
        if x<rincrease2:
            rincrease2-=5
        elif x>rincrease2:
            rincrease2+=5
        if y<ryincrease2:
            ryincrease2-=5
        elif y>ryincrease2:
            ryincrease2+=5

        if direction=="right":screen.blit(cpics[9],(0,y1-cpics[9].get_size()[1]))
        else: screen.blit(transform.flip(cpics[9],748,0),(748,y1-cpics[9].get_size()[1]))

        if direction=="right":screen.blit(cpics[15],(rincrease2,ryincrease2-cpics[15].get_size()[1]))
        else: screen.blit(transform.flip(cpics[15],rincrease2,0),(rincrease2,ryincrease2-cpics[15].get_size()[1]))
        
        attackarea2=Rect(rincrease2,ryincrease2-cpics[15].get_size()[1],cpics[15].get_size()[0],cpics[15].get_size()[1])

    if frame2>60:
        attack3done2=True
        rincrease2,ryincrease2=0,0

#JIRAIYA'S SPECIAL MOVES

#basic function, blit every picture
def jiraiyaattack1(x1,y1,direction):
    global frame,pics,attack1done,attackarea,first
    cpics = pics[5][4]
    if first:
        frame=0
    if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1])) 
    else: screen.blit(transform.flip(cpics[frame],x1,0),((x1,y1-cpics[frame].get_size()[1])))
    attackarea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    if frame+1==len(cpics):
        attack1done =True

#basic funtion, except problem with left part, explained in bellow comment
def jiraiyaattack2(x1,y1,direction):
    global frame,pics,attack2done,attackarea,first,rincrease,ryincrease,x2,y2
    cpics = pics[5][5]
    if first:
        frame=0
    if direction=="right":
        screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))
        attackarea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    else:
        #we can't just blit this picture at normal x1, because if we do the beginning of the picture will be in the same place while the end will move
        #but we wan't the end to stay still and the beginning to expand out to the left.
        #so if we subtract the width of the picture from x1, then beginnning will move but the end will stay put, the plus 50 is just to adjust the piture to start a bit in front
        blitx=x1-cpics[frame].get_size()[0]+50
        screen.blit(transform.flip(cpics[frame],blitx,0),((blitx,y1-cpics[frame].get_size()[1])))
        attackarea=Rect(blitx,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    if frame+1==len(cpics):
        attack2done =True

#like gaaraattack3

def jiraiyaattack3(x1,y1,direction):
    global frame,pics,attack3done,attackarea,first,rincrease,ryincrease,x2,y2
    cpics = pics[5][6]
    if first:
        frame=0
        if direction=="right":
            rincrease,ryincrease=x1+50,y1
        else:
            rincrease,ryincrease=x1-250,y1
    if frame<3:
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))  #hand signs
        else: screen.blit(transform.flip(cpics[frame],x1,0),((x1,y1-cpics[frame].get_size()[1])))
        parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    else:
        #the ball follwing you
        if x2<rincrease:
            rincrease-=5
        elif x2>rincrease:
            rincrease+=5
        if y2<ryincrease:
            ryincrease-=5
        elif y2>ryincrease:
            ryincrease+=5
            
        if direction=="right":
            screen.blit(cpics[2],(x1,y1-cpics[2].get_size()[1]))  #character standing
            screen.blit(cpics[3+frame%3],(rincrease,ryincrease-cpics[3+frame%3].get_size()[1])) #the ball
            attackarea=Rect(rincrease,ryincrease-cpics[3+frame%3].get_size()[1],cpics[3+frame%3].get_size()[0],cpics[3+frame%3].get_size()[1])

        else:
            screen.blit(transform.flip(cpics[2],x1,0),((x1,y1-cpics[2].get_size()[1])))
            screen.blit(transform.flip(cpics[3+frame%3],rincrease,0),((rincrease,ryincrease-cpics[3+frame%3].get_size()[1])))
            attackarea=Rect(rincrease,ryincrease-cpics[3+frame%3].get_size()[1],cpics[3+frame%3].get_size()[0],cpics[3+frame%3].get_size()[1])
            
    if frame>25:
        attack3done =True 
        rincrease,ryincrease=0,0

#JIRAIYA AS SECOND PLAYER
def jiraiyaattack12(x1,y1,direction):
    global frame2,pics,attack1done2,attackarea2,first2
    cpics = pics[5][4]
    if first2:
        frame2=0
    if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1])) 
    else: screen.blit(transform.flip(cpics[frame2],x1,0),((x1,y1-cpics[frame2].get_size()[1])))
    attackarea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    if frame2+1==len(cpics):
        attack1done2 =True

def jiraiyaattack22(x1,y1,direction):
    global frame2,pics,attack2done2,attackarea2,first2
    cpics = pics[5][5]
    if first2:
        frame2=0
    if direction=="right":
        screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1]))
        attackarea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    else:
        #we can't just blit this picture at normal x1, because if we do the beginning of the picture will be in the same place while the end will move
        #but we wan't the end to stay still and the beginning to expand out to the left.
        #so if we subtract the width of the picture from x1, then beginnning will move but the end will stay put, the plus 50 is just to adjust the piture to start a bit in front

        blitx=x1-cpics[frame2].get_size()[0]+50
        screen.blit(transform.flip(cpics[frame2],blitx,0),((blitx,y1-cpics[frame2].get_size()[1])))
        
        attackarea2=Rect(blitx,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    if frame2+1==len(cpics):
        attack2done2 =True

def jiraiyaattack32(x1,y1,direction):
    global frame2,pics,attack3done2,attackarea2,parea2,first2,rincrease2,ryincrease2,x,y
    cpics = pics[5][6]
    if first2:
        frame2=0
        if direction=="right":
            rincrease2,ryincrease2=x1+50,y1
        else:
            rincrease2,ryincrease2=x1-250,y1
    if frame2<3:
        if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame2],x1,0),((x1,y1-cpics[frame2].get_size()[1])))
        parea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    else:
        if x<rincrease2:
            rincrease2-=5
        elif x>rincrease2:
            rincrease2+=5
        if y<ryincrease2:
            ryincrease2-=5
        elif y>ryincrease2:
            ryincrease2+=5
            
        if direction=="right":
            screen.blit(cpics[2],(x1,y1-cpics[2].get_size()[1])) 
            screen.blit(cpics[3+frame2%3],(rincrease2,ryincrease2-cpics[3+frame2%3].get_size()[1]))
            attackarea2=Rect(rincrease2,ryincrease2-cpics[3+frame2%3].get_size()[1],cpics[3+frame2%3].get_size()[0],cpics[3+frame2%3].get_size()[1])

        else:
            screen.blit(transform.flip(cpics[2],x1,0),(x1,y1-cpics[2].get_size()[1]))
            screen.blit(transform.flip(cpics[3+frame2%3],rincrease2,0),((rincrease2,ryincrease2-cpics[3+frame2%3].get_size()[1])))
            attackarea2=Rect(rincrease2,ryincrease2-cpics[3+frame2%3].get_size()[1],cpics[3+frame2%3].get_size()[0],cpics[3+frame2%3].get_size()[1])
            
    if frame2>25:
        attack3done2 =True 
        rincrease2,ryincrease2=0,0

#like madaraattack1
def itachiattack1(x1,y1,direction):
    global frame,pics,attack1done,attackarea,first
    cpics = pics[6][4]
    if first:
        frame=0
    if frame<=12:
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame],x1,0),((x1,y1-cpics[frame].get_size()[1])))
        
    else:
        if direction=="right":
            screen.blit(cpics[frame-(frame/10*9)+1],(x1,y1-cpics[0].get_size()[1]))
            screen.blit(cpics[frame],(x1+50,y1-cpics[frame].get_size()[1]))
            attackarea=Rect(x1+50,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
        else:
            screen.blit(transform.flip(cpics[frame-(frame/10*9)+1],x1,0),(x1,y1-cpics[0].get_size()[1]))
            screen.blit(transform.flip(cpics[frame],x1,0),(x1-150,y1-cpics[frame].get_size()[1]))
            attackarea=Rect(x1-100,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
        
    if frame+1==len(cpics):
        attack1done =True

#Like itachiattack1
def itachiattack2(x1,y1,direction):
    global frame,pics,attack2done,attackarea,first
    cpics = pics[6][5]
    if first:
        frame=0
    if frame<6:
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame],x1,0),((x1,y1-cpics[frame].get_size()[1])))
        attackarea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    else:
        if direction=="right":
            screen.blit(cpics[5],(x1,y1-cpics[5].get_size()[1]))
            screen.blit(cpics[frame],(x1+50,y1-cpics[frame].get_size()[1])) 
        else:
            screen.blit(transform.flip(cpics[5],x1,0),((x1,y1-cpics[5].get_size()[1])))
            screen.blit(transform.flip(cpics[frame],x1-50,0),((x1-50,y1-cpics[frame].get_size()[1])))
        attackarea=Rect(x1-50,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    
    if frame+1==len(cpics):
        attack2done =True

# he does some hand signes, and then a arrow moves through the whole screen, use summond to move the arrow a bit at a time
def itachiattack3(x1,y1,direction):
    global frame,pics,attack3done,attackarea,summond,fireitachi,first
    if first2:
        summond=15
    cpics=pics[6][6]
    if frame<6:
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame%12].get_size()[1]))  #handsignes
        else:screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame%12].get_size()[1]))
    else:
        if direction=="right":
            if frame<12:
                screen.blit(fireitachi[frame-6],(x1+summond,y1-fireitachi[frame-6].get_size()[1])) #all the frame thing is just to get the right frame
                screen.blit(cpics[5],(x1,y1-cpics[5].get_size()[1])) #character arrow
                attackarea=Rect((x1+summond,y1-fireitachi[frame-6].get_size()[1],fireitachi[frame-6].get_size()[0],fireitachi[frame-6].get_size()[1]))
                summond+=15
            else:
                screen.blit(fireitachi[5],(x1+summond,y1-fireitachi[5].get_size()[1]))
                screen.blit(cpics[5],(x1,y1-cpics[5].get_size()[1]))
                attackarea=Rect((x1+summond,y1-fireitachi[5].get_size()[1],fireitachi[5].get_size()[0],fireitachi[5].get_size()[1]))
                summond+=15
        else:
            if frame<12:
                screen.blit(transform.flip(fireitachi[frame-6],x1+summond,0),(x1+summond,y1-fireitachi[frame-6].get_size()[1]))
                screen.blit(transform.flip(cpics[5],x1,0),(x1,y1-cpics[5].get_size()[1]))
                attackarea=Rect((x1+summond,y1-fireitachi[frame-6].get_size()[1],fireitachi[frame-6].get_size()[0],fireitachi[frame-6].get_size()[1]))
                summond-=15
            else:
                screen.blit(transform.flip(fireitachi[5],x1+summond,0),(x1+summond,y1-fireitachi[5].get_size()[1]))
                screen.blit(transform.flip(cpics[5],x1,0),(x1,y1-cpics[5].get_size()[1]))
                attackarea=Rect((x1+summond,y1-fireitachi[5].get_size()[1],fireitachi[5].get_size()[0],fireitachi[5].get_size()[1]))
                summond-=15  
    if x1+summond>999 or x1+summond<0: #stops when oput of screen
        attack3done=True
        summond=15

def itachiattack12(x1,y1,direction):
    global frame2,pics,attack1done2,attackarea2,first2
    cpics = pics[6][4]
    if first2:
        frame2=0
    if frame2<=12:
        if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame2],x1,0),((x1,y1-cpics[frame2].get_size()[1])))
        
    else:
        if direction=="right":
            screen.blit(cpics[frame2-(frame2/10*9)+1],(x1,y1-cpics[0].get_size()[1]))
            screen.blit(cpics[frame2],(x1+50,y1-cpics[frame2].get_size()[1]))
            attackarea2=Rect(x1+50,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
        else:
            screen.blit(transform.flip(cpics[frame2-(frame2/10*9)+1],x1,0),(x1,y1-cpics[0].get_size()[1]))
            screen.blit(transform.flip(cpics[frame2],x1,0),(x1-150,y1-cpics[frame2].get_size()[1]))
            attackarea2=Rect(x1-100,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
        
    if frame2+1==len(cpics):
        attack1done2 =True
        
def itachiattack22(x1,y1,direction):
    global frame2,pics,attack2done2,attackarea2,first2
    cpics = pics[6][5]
    if first2:
        frame2=0
    if frame2<6:
        if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame2],x1,0),((x1,y1-cpics[frame2].get_size()[1])))
        attackarea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    else:
        if direction=="right":
            screen.blit(cpics[5],(x1,y1-cpics[5].get_size()[1]))
            screen.blit(cpics[frame2],(x1+50,y1-cpics[frame2].get_size()[1])) 
        else:
            screen.blit(transform.flip(cpics[5],x1,0),((x1,y1-cpics[5].get_size()[1])))
            screen.blit(transform.flip(cpics[frame2],x1,0),((x1-50,y1-cpics[frame2].get_size()[1])))
        attackarea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    
    if frame2+1==len(cpics):
        attack2done2 =True

def itachiattack32(x1,y1,direction):
    global frame2,pics,attack3done2,attackarea2,summond,fireitachi,first2
    if first2:
        summond=15
    cpics=pics[6][6]
    if frame2<6:
        if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2%12].get_size()[1]))
        else:screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2%12].get_size()[1]))
    else:
        if direction=="right":
            if frame2<12:
                screen.blit(fireitachi[frame2-6],(x1+summond,y1-fireitachi[frame2-6].get_size()[1]))
                screen.blit(cpics[5],(x1,y1-cpics[5].get_size()[1]))
                attackarea2=Rect((x1+summond,y1-fireitachi[frame2-6].get_size()[1],fireitachi[frame2-6].get_size()[0],fireitachi[frame2-6].get_size()[1]))
                summond+=15
            else:
                screen.blit(fireitachi[5],(x1+summond,y1-fireitachi[5].get_size()[1]))
                screen.blit(cpics[5],(x1,y1-cpics[5].get_size()[1]))
                attackarea2=Rect((x1+summond,y1-fireitachi[5].get_size()[1],fireitachi[5].get_size()[0],fireitachi[5].get_size()[1]))
                summond+=15
        else:
            if frame2<12:
                screen.blit(transform.flip(fireitachi[frame2-6],x1+summond,0),(x1+summond,y1-fireitachi[frame2-6].get_size()[1]))
                screen.blit(transform.flip(cpics[5],x1,0),(x1,y1-cpics[5].get_size()[1]))
                attackarea2=Rect((x1+summond,y1-fireitachi[frame2-6].get_size()[1],fireitachi[frame2-6].get_size()[0],fireitachi[frame2-6].get_size()[1]))
                summond-=15
            else:
                screen.blit(transform.flip(fireitachi[5],x1+summond,0),(x1+summond,y1-fireitachi[5].get_size()[1]))
                screen.blit(transform.flip(cpics[5],x1,0),(x1,y1-cpics[5].get_size()[1]))
                attackarea2=Rect((x1+summond,y1-fireitachi[5].get_size()[1],fireitachi[5].get_size()[0],fireitachi[5].get_size()[1]))
                summond-=15  
    if x1+summond>999 or x1+summond<0:
        attack3done2=True
        summond=15

#dissappears and appears infront of opponent and does attacks with sword
def sasukeattack1(x1,y1,direction):
    global frame,pics,attack1done,attackarea,first,x
    cpics = pics[7][4]
    if first:
        frame=0
    if frame==3:
        x=x2-50
        x1=x #opponent positions
    if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1])) 
    else:
        if frame>2:
            screen.blit(transform.flip(cpics[frame],x1,0),(x1+75,y1-cpics[frame].get_size()[1])) #bliting in front of opponent
            
        else:
            screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
    if frame>2:
        attackarea=Rect((x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1]))
    if frame>16:
        attack1done=True
        x=x+75

#same as jiraiyaattack2, basic with fix for left

def sasukeattack2(x1,y1,direction):
    global frame,pics,attack2done,attackarea,first
    cpics = pics[7][5]
    if first:
        frame=0
    if direction=="right":
        screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))
        attackarea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    else:
        blitx=x1-cpics[frame].get_size()[0]
        screen.blit(transform.flip(cpics[frame],blitx,0),((blitx,y1-cpics[frame].get_size()[1])))
        attackarea=Rect(blitx,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    if frame+1==len(cpics):
        attack2done =True

#same as sasukeattack1
def sasukeattack3(x1,y1,direction):
    global frame,pics,attack3done,attackarea,x2,x
    cpics = pics[7][6]
    if frame==20:
        x=x2-50
        x1=x
    if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))
    if direction=="left":
        if frame>19:
            screen.blit(transform.flip(cpics[frame],x1,0),(x1+75,y1-cpics[frame].get_size()[1]))
            
        else:
            screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
            
    if frame>19:
        attackarea=Rect((x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1]))
    if frame>36:
        attack3done=True
        x=x+50

def sasukeattack12(x1,y1,direction):
    global frame2,pics,attack1done2,attackarea2,first2,x2,x
    cpics = pics[7][4]
    if first2:
        frame2=0
    if frame2==3:
        x2=x-50
        x1=x2
    if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1])) 
    else:
        if frame2>2:
            screen.blit(transform.flip(cpics[frame2],x1,0),(x1+75,y1-cpics[frame2].get_size()[1]))
            
        else:
            screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))
    if frame2>2:
        attackarea2=Rect((x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1]))
    if frame2>16:
        attack1done2=True
        x=x+75

def sasukeattack22(x1,y1,direction):
    global frame2,pics,attack2done2,attackarea2,first2,middleaxis
    cpics = pics[7][5]
    if first2:
        frame2=0
    if direction=="right":
        screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1]))
        attackarea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    else:

        blitx=x1-cpics[frame2].get_size()[0]
        screen.blit(transform.flip(cpics[frame2],blitx,0),((blitx,y1-cpics[frame2].get_size()[1])))
        
        attackarea2=Rect(blitx,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])

    if frame2+1==len(cpics):
        attack2done2 =True

def sasukeattack32(x1,y1,direction):
    global frame2,pics,attack3done2,attackarea2,x2,x
    cpics = pics[7][6]
    if frame2==20:
        x2=x-50
        x1=x2
    if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1]))
    if direction=="left":
        if frame2>19:
            screen.blit(transform.flip(cpics[frame2],x1,0),(x1+75,y1-cpics[frame2].get_size()[1]))
            
        else:
            screen.blit(transform.flip(cpics[frame2],x1,0),(x1,y1-cpics[frame2].get_size()[1]))
            
    if frame2>19:
        attackarea2=Rect((x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1]))
    if frame2>36:
        attack3done2=True
        x=x+50
        
#defining the hokage attacks

def hokageattack1(x1,y1,direction):
    global frame,pics,attack1done,attackarea,first,parea
    cpics=pics[8][4]
    if first:
        frame=0
    if frame<=2:
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame],x1,0),((x1,y1-cpics[frame].get_size()[1])))
        parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    else:
        
        if direction=="right":
            screen.blit(cpics[2],(x1,y1-cpics[2].get_size()[1])) 
            screen.blit(cpics[frame],(x1+50,y1-cpics[frame].get_size()[1]))
            attackarea=Rect(x1+50,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
        else:
            screen.blit(transform.flip(cpics[2],x1,0),((x1,y1-cpics[2].get_size()[1])))
            #we can't just blit this picture at normal x1, because if we do the beginning of the picture will be in the same place while the end will move
            #but we wan't the end to stay still and the beginning to expand out to the left.
            #so if we subtract the width of the picture from x1, then beginnning will move but the end will stay put, the plus 50 is just to adjust the piture to start a bit in front

            blitx=x1-50-cpics[frame].get_size()[0]
            screen.blit(transform.flip(cpics[frame],blitx,0),((blitx,y1-cpics[frame].get_size()[1])))
            attackarea=Rect(blitx,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    if frame+1==len(cpics):
        attack1done=True

middleaxis=0
#same as jisraiyaattack2 and sasuke attack2,
def hokageattack2(x1,y1,direction):
    global frame,pics,attack2done,attackarea,first,middleaxis,parea
    cpics=pics[8][5]
    if first:
        frame=0
        middleaxis = cpics[12].get_size()[0]/2.00 #the distance to the middle of the largest image
        
    if frame<=2:
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame],x1,0),((x1,y1-cpics[frame].get_size()[1])))
        parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    else:
        if direction=="right":
            screen.blit(cpics[2],(x1,y1-cpics[2].get_size()[1]))
            blitx= x1 + 50 + middleaxis - (cpics[frame].get_size()[0])/2.00 #not neccessary
            screen.blit(cpics[frame],(blitx,y1-cpics[frame].get_size()[1]))
            attackarea=Rect(blitx,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
        else:
            screen.blit(transform.flip(cpics[2],x1,0),((x1,y1-cpics[2].get_size()[1])))
            blitx= x1 - middleaxis - (cpics[frame].get_size()[0])/2.00 #this blits the picture so it looks like it is growing from the middle, the plus 50 so it is in front of the character and not on him
            screen.blit(transform.flip(cpics[frame],blitx,0),((blitx,y1-cpics[frame].get_size()[1])))
            attackarea=Rect(blitx,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    if frame+1==len(cpics):
        attack2done=True
        middleaxis=0

#same as basic, except we make the picture grow from the middle of the largest image
        
def hokageattack3(x1,y1,direction):
    global frame,pics,attack3done,attackarea,first,middleaxis,parea
    cpics=pics[8][6]
    if first:
        frame=0
        middleaxis = cpics[12].get_size()[0]/2.00 #the distance to the middle of the largest image
        
    if frame<=2:
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame],x1,0),((x1,y1-cpics[frame].get_size()[1])))
        parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    else:
        if direction=="right":
            screen.blit(cpics[2],(x1,y1-cpics[2].get_size()[1]))
            blitx= x1 + 50 + middleaxis - (cpics[frame].get_size()[0])/2.00 #this blits the picture so it looks like it is growing from the middle, the plus 50 so it is in front of the character and not on him
            screen.blit(cpics[frame],(blitx,y1-cpics[frame].get_size()[1]))
            attackarea=Rect(blitx,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
        else:
            screen.blit(transform.flip(cpics[2],x1,0),((x1,y1-cpics[2].get_size()[1])))
            blitx= x1 - middleaxis - (cpics[frame].get_size()[0])/2.00
            screen.blit(transform.flip(cpics[frame],blitx,0),((blitx,y1-cpics[frame].get_size()[1])))
            attackarea=Rect(blitx,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    if frame+1==len(cpics):
        attack3done=True
        middleaxis=0
        
#hokage as player 2

def hokageattack12(x1,y1,direction):
    global frame2,pics,attack1done2,attackarea2,first2,parea2
    cpics=pics[8][4]
    if first2:
        frame2=0
    if frame2<=2:
        if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame2],x1,0),((x1,y1-cpics[frame2].get_size()[1])))
        parea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    else:
        
        if direction=="right":
            screen.blit(cpics[2],(x1,y1-cpics[2].get_size()[1])) 
            screen.blit(cpics[frame2],(x1+50,y1-cpics[frame2].get_size()[1]))
            attackarea2=Rect(x1+50,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
        else:
            screen.blit(transform.flip(cpics[2],x1,0),((x1,y1-cpics[2].get_size()[1])))
            #we can't just blit this picture at normal x1, because if we do the beginning of the picture will be in the same place while the end will move
            #but we wan't the end to stay still and the beginning to expand out to the left.
            #so if we subtract the width of the picture from x1, then beginnning will move but the end will stay put, the plus 50 is just to adjust the piture to start a bit in front
            blitx=x1-50-cpics[frame2].get_size()[0]
            screen.blit(transform.flip(cpics[frame2],blitx,0),((blitx,y1-cpics[frame2].get_size()[1])))
            attackarea2=Rect(blitx,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    if frame2+1==len(cpics):
        attack1done2=True

middleaxis2=0

def hokageattack22(x1,y1,direction):
    global frame2,pics,attack2done2,attackarea2,first2,middleaxis2,parea2
    cpics=pics[8][5]
    if first2:
        frame2=0
        middleaxis2 = cpics[12].get_size()[0]/2.00 #the distance to the middle of the largest image
        
    if frame2<=2:
        if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame2],x1,0),((x1,y1-cpics[frame2].get_size()[1])))
        parea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    else:
        if direction=="right":
            screen.blit(cpics[2],(x1,y1-cpics[2].get_size()[1]))
            blitx= x1 + 50 + middleaxis2 - (cpics[frame2].get_size()[0])/2.00 #this blits the picture so it looks like it is growing from the middle, the plus 50 so it is in front of the character and not on him
            screen.blit(cpics[frame2],(blitx,y1-cpics[frame2].get_size()[1]))
            attackarea2=Rect(blitx,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
        else:
            screen.blit(transform.flip(cpics[2],x1,0),((x1,y1-cpics[2].get_size()[1])))
            blitx= x1 - middleaxis2 - (cpics[frame2].get_size()[0])/2.00
            screen.blit(transform.flip(cpics[frame2],blitx,0),((blitx,y1-cpics[frame2].get_size()[1])))
            attackarea2=Rect(blitx,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    if frame2+1==len(cpics):
        attack2done2=True
        middleaxis2=0
        
def hokageattack32(x1,y1,direction):
    global frame2,pics,attack3done2,attackarea2,first2,middleaxis2,parea2
    cpics=pics[8][6]
    if first2:
        frame2=0
        middleaxis2 = cpics[12].get_size()[0]/2.00 #the distance to the middle of the largest image
        
    if frame2<=2:
        if direction=="right":screen.blit(cpics[frame2],(x1,y1-cpics[frame2].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame2],x1,0),((x1,y1-cpics[frame2].get_size()[1])))
        parea2=Rect(x1,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    else:
        if direction=="right":
            screen.blit(cpics[2],(x1,y1-cpics[2].get_size()[1]))
            blitx= x1 + 50 + middleaxis2 - (cpics[frame2].get_size()[0])/2.00 #this blits the picture so it looks like it is growing from the middle, the plus 50 so it is in front of the character and not on him
            screen.blit(cpics[frame2],(blitx,y1-cpics[frame2].get_size()[1]))
            attackarea2=Rect(blitx,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
        else:
            screen.blit(transform.flip(cpics[2],x1,0),((x1,y1-cpics[2].get_size()[1])))
            blitx= x1 - middleaxis2 - (cpics[frame2].get_size()[0])/2.00
            screen.blit(transform.flip(cpics[frame2],blitx,0),((blitx,y1-cpics[frame2].get_size()[1])))
            attackarea2=Rect(blitx,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
    if frame2+1==len(cpics):
        attack3done2=True
        middleaxis2=0

#there are three items, one slows time, one regenerates health and the other regenerates chakra, the items appear at random times, called in while loop
itemx,itemy=0,300 #starting positions
itemhealth=75 #you have to reduce health to zero to get item
itemdone=True #keeps track of wheter move is done or not
delay=False #to slow down, if delay, we do a time.wait
itemcount=0
itemfirst=False #wether first time in loop
randnumber=0

def randomitem():
    global itemx,itemy,itemhealth,attackarea,attackarea2,fdvalue,fdvalue2,itemdone,delay,itemcount,itemfirst,randnumber,healthitem,health,health2,chakraitem,chakra,chakra2

    if itemfirst:
        itemx,itemy=0,300
        itemhealth=75
        itemdone=False
        delay=False
        itemcount=0
        itemfirst=False
        randnumber=randint(1,3) # we pick a random item to do

    if randnumber==1: #slowmotion item
        if delay==False:
            
            if itemx>1000: #to return back on screen
                itemx=0
            
            screen.blit(slowmotion,(itemx,50*cos(radians(itemx))+itemy)) # moves through screen in a cos wave pattern
            itemrect = Rect(itemx,50*cos(radians(itemx))+itemy,75,75) #item area

            if itemrect.colliderect(attackarea): 
                itemhealth-=1 #losing item health
                if itemhealth==0:
                    delay=True #delay in the loop

            if itemrect.colliderect(attackarea2):
                itemhealth-=1
                if itemhealth==0:
                    delay=True

            itemhealthrect=Rect(itemx,50*cos(radians(itemx))+itemy-5,itemhealth,5) #drawing the health bar for the item
            draw.rect(screen,(0,255,50),itemhealthrect,0)
            itemx+=1.5 #moving
            
        else:
            itemcount+=1
            if itemcount==100:
                itemdone=True

    #the other two are basically same
    elif randnumber==2:
        if itemx>1000:
            itemx=0
            
        screen.blit(healthitem,(itemx,50*cos(radians(itemx))+itemy))
        itemrect = Rect(itemx,50*cos(radians(itemx))+itemy,75,75)
    
        if itemrect.colliderect(attackarea): 
            itemhealth-=1
            if itemhealth==0:
                health+=100 #gains health
                if health>250:
                    health=250 
                itemdone=True

        if itemrect.colliderect(attackarea2):
            itemhealth-=1
            if itemhealth==0:
                health2+=100
                if health2>250:
                    health2=250
                itemdone=True

        itemhealthrect=Rect(itemx,50*cos(radians(itemx))+itemy-5,itemhealth,5)
        draw.rect(screen,(0,255,50),itemhealthrect,0)
        itemx+=1.5

    elif randnumber==3:
        if itemx>1000:
            itemx=0
            
        screen.blit(chakraitem,(itemx,50*cos(radians(itemx))+itemy))
        itemrect = Rect(itemx,50*cos(radians(itemx))+itemy,75,75)
    
        if itemrect.colliderect(attackarea): 
            itemhealth-=1
            if itemhealth==0:
                chakra+=100 #gains chakra
                if chakra>250:
                    chakra=250 
                itemdone=True

        if itemrect.colliderect(attackarea2):
            itemhealth-=1
            if itemhealth==0:
                chakra2+=100
                if chakra2>250:
                    chakra2=250
                itemdone=True

        itemhealthrect=Rect(itemx,50*cos(radians(itemx))+itemy-5,itemhealth,5)
        draw.rect(screen,(0,255,50),itemhealthrect,0)
        itemx+=1.5


    
    
player="naruto" #starting character
screenanimationcount=0 #for a specail background
selection=0 #picking character
mx,my=0,0

# PLAYER 1 ----------------------------------------------------------------------------        

x,y=300,700
yvalue=700 #floor
rincrease,lincrease,ryincrease,lyincrease=0,0,0,0 #for some reason, if i defined these in the function i got an error
yincrease=-20 #for jump
char="" #character
direc="right" #facing direction
prevmove="" #keeps track of previous move
count=0
row=0

first=False
jumpdone=True #dones are all keeping track of wether a move is done
damagedone=True
attack1done=True
attack2done=True
attack3done=True
takedamagedonelevel1=True 
takedamagedonelevel2=True
frame=0 #for the picture i am going to blit
fdvalue=4#frame delay value, incase i need to change it
frameDelay=fdvalue
move="" #current move
attack="" #this was for testing purposes not used anymore
health=250 #max health
damage=0 #how much health you loose
chakra=0 #the madic used to use special moves
parea=Rect(0,0,0,0) #area of the player
attackarea = Rect(0,0,0,0) #where the player is attacking
healthbar = Rect(320-(250-health),10,250-health,30) #250-health gives the health that the player lost, 320-that is where we start since the end of the bar is 320, than the width is 250-health+1 so we end back at 321 (if we end at 320 not everything goes away)
chakrabar = Rect(70,50,chakra,20)
walkcountleft=0 #if a player tapes the walk left key twice the player will run, this variable is ued to keep tack of the taping
walkcountright=0 #if a player tapes the walk right key twice the player will run, this variable is ued to keep tack of the taping

# PLAYER 2 ----------------------------------------------------------------------------
#we use all the same variables except, we add a 2 in the end for character 2
#all the vaiables have the same purpose has player one variables

x2,y2=700,700
yvalue2=700
rincrease2,lincrease2,ryincrease2,lyincrease2=0,0,0,0 
yincrease2=-20
char2=""
direc2="left"
prevmove2=""
move2=""
attack2=""
count2=0
row2=0
counter2=0
first2=False
jumpdone2=True
attack1done2=True
attack2done2=True
attack3done2=True
takedamagedonelevel12=True
takedamagedonelevel22=True
frame2=0
fdvalue2=fdvalue
frameDelay2=4
health2=250
damage2=0
chakra2=0
p2area=Rect(0,0,0,0)
attackarea2=Rect(0,0,0,0)
healthbar2 = Rect(679,10,250-health2,30) #this bar is easier since it starts at the begining of the picture and the width is the amount of health lost, the picture starts at 680 but we start one back to cover everything
chakrabar2 = Rect(930,50,(-1)*chakra2,20) #this bar starts near the end and goes back
walkcountleft2=0
walkcountright2=0

resetfile = open("reset.txt").read().split("\n")

while running:

    mx,my = mouse.get_pos()
    keys = key.get_pressed()
    mb = mouse.get_pressed()
    
    for evt in event.get():
        if evt.type == QUIT:
            running=False
        
        if evt.type == MOUSEBUTTONDOWN:
            sx,sy=mouse.get_pos()

            if conformrect.collidepoint((mx,my)): #if you click confirm on you pick the character and election goes to one
                if selection==0:
                    char=player
                elif selection==1: #if you conform while selections is one, you pick player 2
                    char2=player
                    imageload(char,char2) #loads all the pictures for the characters
                    for line in range(len(pics)): #finds the row with all the character 1 pics
                        if pics[line][12]==char:
                            row=line

                    for line in range(len(pics)): #finds the row with all the character 2 pics
                        if pics[line][12]==char2:
                            row2=line
                    page="stageselection" #goes to next stage selection
                    mugshot=pics[row][13]
                    mugshot2=pics[row2][13]
                    
        if evt.type == MOUSEBUTTONUP:
            if conformrect.collidepoint((mx,my)):
                if char!="":
                    selection+=1
            if page=="stageselection":
                if mb[0]==1: #goes to the next stage in backlist
                    column+=1
                    if column==5:
                        column=0

    if page=="startpage":
        screen.blit(ifrontpage,(0,0))
        screen.blit(istart,(401,5))
        screen.blit(icontrols,(1000-193,0))

        if start.collidepoint((mx,my)) and mb[0]==1:
            page="selectionpage" #goes to next page

        elif controls.collidepoint((mx,my)) and mb[0]==1:
            page="controlsscreen"
            

        if mb[0]==1:
            draw.rect(screen,(255,0,0),(sx,sy,mx-sx,my-sy),2)
            rectarea = "Rect"+str((sx,sy,mx-sx,my-sy))

    elif page=="controlsscreen":
        screen.blit(image.load("controls screen.png"),(0,0))

        if back.collidepoint((mx,my)) and mb[0]==1:
            page="startpage" #goes back to start
        
    elif page=="selectionpage":
        screen.blit(selectionpage,(0,0))
        screen.blit(eval(player+"stance"),(0,0))

        #this is for hover if over confirm, look under mousebutton down to see confirming character
        if conformrect.collidepoint((mx,my)):
            screen.blit(conform2,(500,450))
        else:
            screen.blit(conform,(500,450))

        #for each character, a rect that is defined above,
        if narutorect.collidepoint(mx,my):
            if mb[0]==1:
                player="naruto"
            screen.blit(hover,(narutorect[0],narutorect[1]))  #there is a hover image, simply blit it on the coordinates of the rectangle of the character
        elif madararect.collidepoint(mx,my):
            if mb[0]==1:
                player="madara"
            screen.blit(hover,(madararect[0],madararect[1]))
        elif kisamerect.collidepoint(mx,my):
            if mb[0]==1:
                player="kisame"
            screen.blit(hover,(kisamerect[0],kisamerect[1]))
        elif sakurarect.collidepoint(mx,my):
            if mb[0]==1:
                player="sakura"
            screen.blit(hover,(sakurarect[0],sakurarect[1]))
        elif jiraiyarect.collidepoint(mx,my):
            if mb[0]==1:
                player="jiraiya"
            screen.blit(hover,(jiraiyarect[0],jiraiyarect[1]))
        elif itachirect.collidepoint(mx,my):
            if mb[0]==1:
                player="itachi"
            screen.blit(hover,(itachirect[0],itachirect[1]))
        elif gaararect.collidepoint(mx,my):
            if mb[0]==1:
                player="gaara"
            screen.blit(hover,(gaararect[0],gaararect[1]))
        elif hokagerect.collidepoint(mx,my):
            if mb[0]==1:
                player="hokage"
            screen.blit(hover,(hokagerect[0],hokagerect[1]))
        elif sasukerect.collidepoint(mx,my):
            if mb[0]==1:
                player="sasuke"
            screen.blit(hover,(sasukerect[0],sasukerect[1]))
        elif kakashirect.collidepoint(mx,my):
            if mb[0]==1:
                player="kakashi"
            screen.blit(hover,(kakashirect[0],kakashirect[1]))
        screen.blit(select,(eval(player+"rect[0]"),eval(player+"rect[1]")))

        #tells ou which player you are on
        if selection==0:
            screen.blit(player1,(10,600))
        else:
            screen.blit(player2,(10,600))

    elif page=="stageselection":
        background=backlist[column][0] #look under mousebutton up to see when clumn changes
        platforms =backlist[column][1]

        screen.blit(background,(0,0))
        screen.blit(selectintructions,(0,581)) #tells you to click to go to next background, and press enter to select background
        
        if keys[13]==1:
            page="fightpage"
            mixer.music.load(backlist[column][2]) #music is different for each background, look in backlist near top
            mixer.music.play(-1)
            if background==backlist[2][0]:
                #in the valley of the end backgroudn we have to animate a water fall with the pictures we are loading below
                valleyoftheend=[image.load("valley of the end "+str(x)+".png") for x in range(1,4)]
                screenanimationcount=0

    if health<=0 or health2<=0: #this is for when characters die
        if health<=0: 
            health=0
            screen.blit(player2victory,(300,200))
            winner=timesFont.render(char2.upper(),1,(0,0,255))
            screen.blit(winner,(500-(winner.get_size()[0])/2.0,375)) #allign the winner name in the middle
            

        elif health2<=0:
            health2=0
            screen.blit(player1victory,(300,200))
            winner=timesFont.render(char.upper(),1,(0,0,255))
            screen.blit(winner,(500-(winner.get_size()[0])/2.0,375))

        screen.blit(playagain,(415,425))

        if playagainrect.collidepoint((mx,my)): #they want to play again
            draw.rect(screen,(0,0,0),playagainrect,1)
            if mb[0]==1: #resetting all the variables
                page="startpage"
                player="naruto"
                screenanimationcount=0
                selection=0
                mx,my=0,0
                x,y=300,700
                yvalue=700
                rincrease,lincrease,ryincrease,lyincrease=0,0,0,0 
                yincrease=-20
                char=""
                direc="right"
                prevmove=""
                count=0
                row=0
                first=False
                jumpdone=True
                damagedone=True
                attack1done=True
                attack2done=True
                attack3done=True
                takedamagedonelevel1=True
                takedamagedonelevel2=True
                frame=0
                fdvalue=4
                frameDelay=fdvalue
                move=""
                attack=""
                health=250
                damage=0
                chakra=0
                parea=Rect(0,0,0,0)
                attackarea = Rect(0,0,0,0)
                healthbar = Rect(320-(250-health),10,250-health,30)
                chakrabar = Rect(70,50,chakra,20)
                chakracharge=0.05
                walkcountleft=0 
                walkcountright=0 
                x2,y2=700,700
                yvalue2=700
                rincrease2,lincrease2,ryincrease2,lyincrease2=0,0,0,0 
                yincrease2=-20
                char2=""
                direc2="left"
                prevmove2=""
                move2=""
                attack2=""
                count2=0
                row2=0
                first2=False
                jumpdone2=True
                attack1done2=True
                attack2done2=True
                attack3done2=True
                takedamagedonelevel12=True
                takedamagedonelevel22=True
                frame2=0
                fdvalue2=fdvalue
                frameDelay2=4
                health2=250
                damage2=0
                chakra2=0
                p2area=Rect(0,0,0,0)
                attackarea2=Rect(0,0,0,0)
                healthbar2 = Rect(679,10,250-health2,30)
                chakrabar2 = Rect(930,50,(-1)*chakra2,20)
                counter=0
                chakracharge2=0.05           
                walkcountleft2=0
                walkcountright2=0
                mixer.music.load("intro.mp3")
                mixer.music.play(-1)
        
    elif page=="fightpage": #the main fight page
        chakracharge2=0.07

        screen.blit(background,(0,0)) #blit background each time to cover previous picks
        
        if background==backlist[2][0]: #if valley of the end background
            if screenanimationcount==3: #there are three pictures that are always switching to animate waterfall
                screenanimationcount=0
            
            screen.blit(valleyoftheend[screenanimationcount],(0,0)) #the screenanimationcount increases by one each time near the bottom
               
        #the health bar is a curved picture, so we copy a part of the background and put it on top of the health bar so it looks like the bar is shrinking when the opponent loses health
        #the health bar is the part where they lose the health
        screen.blit(grayhealthbarpic,(70,10))
        healthcover = screen.subsurface(healthbar).copy()
        screen.blit(healthbarpic,(70,10))
        screen.blit(healthcover,(healthbar[0],healthbar[1]))

        screen.blit(grayhealthbarpic,(680,10))
        healthcover = screen.subsurface(healthbar2).copy()
        screen.blit(healthbarpic,(680,10))
        screen.blit(healthcover,(healthbar2[0],healthbar2[1]))
        
        draw.rect(screen,(111,111,111),(68,48,254,24),0)
        draw.rect(screen,(111,111,111),(932,48,-254,24),0)
        draw.rect(screen,(50,0,255),chakrabar,0) #rectangle that we draw
        draw.rect(screen,(50,0,255),chakrabar2,0)

        screen.blit(mugshot,(0,0))
        screen.blit(mugshot2,(930,0))

        attackarea=Rect(0,0,0,0) # reset the atatack area so if there is no moves, the opponent does not take damage
        attackarea2=Rect(0,0,0,0)
         
            
        # PLAYER 1 ----------------------------------------------------------------------------

        if x<0: #if the player leaves the screen they come out the other side
            x=1000
            direc="left"
        elif x>1000:
            x=0
            direc="right"
            
        if attack1done and attack2done and attack3done and jumpdone and takedamagedonelevel1 and takedamagedonelevel2: #this is so that you can't stop these moves in the middle
            if keys[K_a]==1:
                move="walk"
                if walkcountleft>0 and prevmove!="walk": #walkcount becomes eight, and near the bottom, we decrease it by 1, so if they let go, so prevmove is not walk and tap walk again before the 8 becomes 0, then we run
                    move="run"    
                walkcountleft=8
            elif keys[K_d]==1:
                move="walk"
                if walkcountright>0 and prevmove!="walk":
                    move="run"    
                walkcountright=8
                
            elif keys[K_w]==1 and keys[K_s]==1 and prevmove!="jump": #chakra charge
                chakra+=0.25
            elif keys[K_s]==1:
                move="crouch"
            elif keys[K_w]==1 and y<=yvalue:
                jumpdone=False
                move="jump"
                first=True #only first when we clik because, it does not come back here till jumpdone is true, same for all other attacks
            elif keys[K_t]==1 and prevmove!="attack1" and prevmove!="attack2" and prevmove!="attack3" and chakra>=83:
                move="attack1"
                chakra-=40 #loose chakra for using special moves
                first=True 
                attack1done=False
            elif keys[K_y]==1 and prevmove!="attack2" and prevmove!="attack3" and prevmove!="attack1" and chakra>=166:
                move="attack2"
                chakra-=100
                first=True
                attack2done=False
            elif keys[K_u]==1 and prevmove!="attack3" and prevmove!="attack2" and prevmove!="attack1" and chakra>=250:
                move="attack3"
                chakra-=200
                first=True
                attack3done=False
            elif keys[K_h]==1 and keys[K_g]==1:
                move="combo" 
            elif keys[K_g]==1 :
                move="punch"
            elif keys[K_h]==1 :
                move="hardpunch"
            elif keys[K_j]==1:
                move="guard"
            else:
                move="stance" #if no keys are pressed they ar just standing

        #this is so if the moves are not done, they can't be stopped, so the move does not change in the middle, a precation
        if takedamagedonelevel1==False:
            move="takedamage1"

        elif takedamagedonelevel2==False:
            move="takedamage2"

        elif jumpdone==False: #so if jump is not done, the move does not change
            move="jump"
            if keys[K_w]!=1 and yincrease<-10: #this is so when the user lets go of the up key the player comes down again, since i am making it -9 they will go up a bit before coming down, otherwise it looks odd
                yincrease=-9
            
        elif attack1done==False:
            move="attack1"
       
        elif attack2done==False:
            move="attack2"

        elif attack3done==False:
            move="attack3"

        if move=="jump":
            if keys[K_a]==1: #the character can move left and right in the air
                x-=5
                direc="left"
            elif keys[K_d]==1:
                x+=5
                direc="right"
            elif keys[K_s]==1: #if the press doen in the air, they come down faster
                if yincrease<0:
                    yincrease=5
                y+=5

        elif move!="jump":
            y=yvalue #resets eveyrthing for jump
            yincrease=-20
        
        # PLAYER 2 (same as player one) ------------------------------------------

        if x2<0:
            x2=1000
            direc2="left"
        elif x2>1000:
            x2=0
            direc2="right"

        if attack1done2 and attack2done2 and attack3done2 and jumpdone2:
            if keys[K_LEFT]==1:
                move2="walk"
                if walkcountleft2>0 and prevmove2!="walk":
                    move2="run"    
                walkcountleft2=8
            elif keys[K_RIGHT]==1:
                move2="walk"
                if walkcountright2>0 and prevmove2!="walk":
                    move2="run"    
                walkcountright2=8
            elif keys[K_UP]==1 and keys[K_DOWN]==1:
                chakra2+=0.25
            elif keys[K_DOWN]==1:
                move2="crouch"
            elif keys[K_UP]==1 and y2<=yvalue2:
                jumpdone2=False
                move2="jump"
                first2=True
            elif keys[K_KP4]==1 and prevmove2!="attack1" and prevmove2!="attack2" and prevmove2!="attack3" and chakra2>=83:
                move2="attack1"
                chakra2-=40
                first2=True
                attack1done2=False
            elif keys[K_KP5]==1 and prevmove2!="attack1" and prevmove2!="attack2" and prevmove2!="attack3" and chakra2>=166:
                move2="attack2"
                chakra2-=80
                first2=True
                attack2done2=False
            elif keys[K_KP6]==1 and prevmove2!="attack1" and prevmove2!="attack2" and prevmove2!="attack3" and chakra2>=250:
                move2="attack3"
                chakra2-=125
                first2=True
                attack3done2=False
            elif keys[K_KP1]==1 and keys[K_KP2]==1:
                move2="combo" 
            elif keys[K_KP1]==1 :
                move2="punch"
            elif keys[K_KP2]==1 :
                move2="hardpunch"
            elif keys[K_KP3]==1 :
                move2="guard"
            else:
                move2="stance"

        if jumpdone2==False:
            move2="jump"
            if keys[K_UP]!=1 and yincrease2<-10:
                yincrease2=-9

        elif takedamagedonelevel12==False:
            move2="takedamage1"

        elif takedamagedonelevel22==False:
            move2="takedamage2"
            
        elif attack1done2==False:
            move2="attack1"
       
        elif attack2done2==False:
            move2="attack2"

        elif attack3done2==False:
            move2="attack3"
            damage=0.1
            
        if move2!="jump":
            y2=yvalue2
            yincrease2=-20

        elif move2=="jump":
            if keys[K_LEFT]==1:
                x2-=5
                direc2="left"
            elif keys[K_RIGHT]==1:
                x2+=5
                direc2="right"
            elif keys[K_DOWN]==1:
                if yincrease2<0:
                    yincrease2=5
                y2+=5

        #this is calling player 2 functions, player ones are beloe, the reason is explained below aswell

        if move2!="": 
            if move2=="stance":
                stance2(x2,y2,direc2,row2)
            elif move2=="walk":
                walk2(x2,y2,direc2,row2)
                if keys[K_LEFT]==1:
                    direc2="left"
                elif keys[K_RIGHT]==1:
                    direc2="right"
            elif move2=="run":
                run2(x2,y2,direc2,row2)
                if keys[K_LEFT]==1:
                    direc2="left" #changing directions between left and right
                elif keys[K_RIGHT]==1:
                    direc2="right"
            elif move2 == "crouch":
                crouch2(x2,y2,direc2,row2)
            elif move2 == "jump":
                #how jump works is we have a yincrease2 that starts as a negative, so when we add this to y2
                # the character goes up. But yincrease2 increases by one each time, eventually it becomes positive
                #and the character goes down. But as the the character goes up he slows down, and as he comes down he speeds up due
                #to the increase of yincrease2
                if frameDelay2%2==0:
                    y2+=yincrease2
                    yincrease2+=.75
                if y2>=yvalue2: #if the are back on the ground the jump is over
                    jumpdone2=True
                #this is so the characters can do punches in the air
                if keys[K_KP1]==1 and keys[K_KP2]==1: 
                    move2="combo"
                elif keys[K_KP1]==1:
                    move2="punch"
                elif keys[K_KP2]==1:
                    move2="hardpunch"
                else: #we only show jumping sprites if they are not punching
                    jump2(x2,y2,direc2,row2)
            elif move2 == "guard":
                guard2(x2,y2,direc2,row2)
                
        # PLAYER 1 ----------------------------------------------------------------------------
        # i put player one here so player one's special moves pictures are on top of player 2's normal moves
        #thats also why player 2's specail moves are below this, so there special moves are on top of these

        if move!="":
            if move=="stance":
                stance(x,y,direc,row)
            elif move=="walk":
                walk(x,y,direc,row)
                if keys[K_a]==1:
                    direc="left"
                elif keys[K_d]==1:
                    direc="right"
            elif move=="run":
                run(x,y,direc,row)
                if keys[K_a]==1:
                    direc="left"
                elif keys[K_d]==1:
                    direc="right"
            elif move == "crouch":
                crouch(x,y,direc,row)
            elif move == "jump":
                if frameDelay%2==0:
                    y+=yincrease
                    yincrease+=.75
                if y>=yvalue:
                    jumpdone=True
                if keys[K_g]==1 and keys[K_h]==1:
                    move="combo"
                elif keys[K_g]==1:
                    move="punch"
                elif keys[K_h]==1:
                    move="hardpunch"
                else:
                    jump(x,y,direc,row)
            elif move == "attack1":
                eval(char+"attack1(x,y,direc)") #the functions are named so this will work
            elif move == "attack2":
                eval(char+"attack2(x,y,direc)")
            elif move == "attack3":
                eval(char+"attack3(x,y,direc)")
            elif move=="guard":
                guard(x,y,direc,row)
            if move == "combo":  #this becomes if statement so the character can jump and punch at the same time
                combo(x,y,direc,row)
            elif move == "punch":
                punch(x,y,direc,row)
            elif move == "hardpunch":
                hardpunch(x,y,direc,row)
            elif move == "takedamage1":
                takedamage(x,y,direc,row,1)
            elif move == "takedamage2":
                takedamage(x,y,direc,row,2)


        #Player 2 attacks, they are here so they are on top
        if move2!="":
            if move2 == "attack1":
                eval(char2+"attack12(x2,y2,direc2)")
            elif move2 == "attack2":
                eval(char2+"attack22(x2,y2,direc2)")
            elif move2 == "attack3":
                eval(char2+"attack32(x2,y2,direc2)")
            elif move2 == "combo":
                combo2(x2,y2,direc2,row2)
            elif move2 == "punch":
                punch2(x2,y2,direc2,row2)
            elif move2 == "hardpunch":
                hardpunch2(x2,y2,direc2,row2)
            elif move2 == "takedamage1":
                takedamage2(x2,y2,direc2,row2,1)
            elif move2 == "takedamage2":
                takedamage2(x2,y2,direc2,row2,2)
        
        
        if parea.colliderect(attackarea2): #this checks to see if the player 1 is within the player 2 attack area
            #the damage is based on the move
            #take damage is when the opponent just moves back, 2 is they actually fall down
            if move2=="punch":
                damage=0.08
                chakra2+=0.08
                move="takedamage1" #this is the recoil
                takedamagedonelevel1=False
            elif move2=="hardpunch":
                damage=1
                chakra2+=0.18
                move="takedamage2" # a hard punch should knock the opponent down
                takedamagedonelevel2=False
            elif move2=="combo":
                damage=1.3
                chakra2+=0.23
                move="takedamage1"
                takedamagedonelevel1=False
            elif move2=="attack1":
                damage=1.2
                move="takedamage2"
                takedamagedonelevel2=False
            elif move2=="attack2":
                damage=1.7
                move="takedamage2"
                takedamagedonelevel2=False
            elif move2=="attack3":
                damage=2.5
                move="takedamage2"
                takedamagedonelevel2=False
            if keys[K_j]==1: #use this instead of move=="guard", because in the above if statements the move gets changed
                damage-=0.08
                #print "1"
                if move2!="attack1" and move2!="attack2" and move2!="attack3": #weak punches should not break the guard
                    move="guard"
                    takedamagedonelevel2=True
                    takedamagedonelevel1=True
                    #print "2"

            health-=damage
            
        #same as above
        if parea2.colliderect(attackarea):
            if move=="punch":
                damage2=0.08
                chakra+=0.08
                move2="takedamage1"
                takedamagedonelevel12=False
            elif move=="hardpunch":
                damage2=1
                chakra+=0.18
                move2="takedamage2"
                takedamagedonelevel22=False
            elif move=="combo":
                damage2=1.3
                chakra+=0.23
                move2="takedamage1"
                takedamagedonelevel12=False
            elif move=="attack1":
                damage2=1.2
                move2="takedamage2"
                takedamagedonelevel22=False
            elif move=="attack2":
                damage2=1.7
                move2="takedamage2"
                takedamagedonelevel22=False
            elif move=="attack3":
                damage2=2.5
                move2="takedamage2"
                takedamagedonelevel22=False
            if keys[K_KP3]==1:
                #print "1"
                damage2-=0.08
                if move!="attack1" and move!="attack2" and move!="attack3":
                    move2="guard"
                    takedamagedonelevel22=True
                    takedamagedonelevel12=True
                    #print "2"

            health2-=damage2

        
        if background==backlist[2][0]: #if the are in valley of the end, they can't be on the bottom because there ois no platform, so they have to move up again
            if y==700:
                health-=1.5
            if y2==700:
                health2-=1.5

            
        #the explosions when two moves collide
        if move=="attack1" or move=="attack2" or move=="attack3":
            if move2=="attack1" or move2=="attack2" or move2=="attack3":
                if attackarea.colliderect(attackarea2): # if two special attacks collide they cancel each other out
                    move=""
                    move2=""
                    attack1done=True
                    attack2done=True
                    attack3done=True
                    attack1done2=True
                    attack2done2=True
                    attack3done2=True
                    screencopy=screen.copy()
                    #collision is called at the average of the x's and y's of the 2 attackareas
                    collision((attackarea[0]+attackarea2[0])/2.0,attackarea[1]+attackarea[3])
         
        if chakra>=250: #250 is max xhakra can't gain anymore than that
            chakra=250

        if chakra2>=250:
            chakra2=250

        
        # Checking to see if charachter is on a platform

        if yincrease>0: #this makes the landing smoother, they can only land if they are going down
            footarea= Rect(parea[0],parea[1]+parea[3]-10,parea[2],10) #this rectangular region defiens the bottom of the feet as a rectangle. Also parea[1]+parea[3] gives us the bottom of parea and approximately 10 above that is where the foot starts.
            for rect in platforms:
                if rect.colliderect(footarea): #if the platform rectangle collides withg the feet
                    yvalue=rect[1]+1 #this ensures that once they get on platform they stay there
                    break

        if move!="jump" and yvalue!=700: #if move is jump, the yincrease gets messed up
            
            for rect in platforms:
                if rect.colliderect(parea): #it is ok to use parea here since the footarea is part of the parea and it does not matter here
                    break
                if rect==platforms[-1]: #if it is the last platform and the character is not on it, we go back to ground level
                    move="jump"
                    jumpdone=False
                    yincrease=5
                    y+=15
                    yvalue=700
           
        # same as above      
        if yincrease2>0:
            footarea2= Rect(parea2[0],parea2[1]+parea2[3]-10,parea2[2],10)
            for rect in platforms:
                if rect.colliderect(footarea2) :
                    yvalue2=rect[1]+1
                    break
                else:
                    yvalue2=700

        if move2!="jump" and yvalue2!=700: 
            for rect in platforms:
                if rect.colliderect(parea2):
                    break
                if rect==platforms[-1]: 
                    move2="jump"
                    jumpdone2=False
                    yincrease2=5
                    yvalue2=700
                       
        
        if itemdone: #this is getting the item functions
            if 3==randint(0,1000): #this makes it a random choice when the item appears
                itemdone=False
                itemfirst=True

        if itemdone==False:
            randomitem()

        #getting all the health and chakra

        healthbar = Rect(320-(250-health),10,250-health+1,30) #250-health gives the health that the player lost, 320-that is where we start since the end of the bar is 320, than the width is 250-health+1 so we end back at 321 (if we end at 320 not everything goes away)
        healthbar2 = Rect(680,10,250-health2,30)

        chakrabar = Rect(70,50,chakra,20)
        chakrabar2 = Rect(930,50,(-1)*chakra2,20)
            
        walkcountleft-=1 #for the running
        walkcountright-=1

        walkcountleft2-=1
        walkcountright2-=1
        
        frameDelay -= 1                         # count down to zero
        if frameDelay == 0:                     # then advance frame like normal
            frameDelay = fdvalue
            frame+=1
            if background==backlist[2][0]:
                screenanimationcount+=1
        prevmove=move
        

        frameDelay2 -= 1                         # count down to zero
        if frameDelay2 == 0:                     # then advance frame like normal
            frameDelay2 = fdvalue2
            frame2 += 1
        prevmove2=move2
        
        if delay: #item effect
            time.wait(75)

    #reset first each time  
    first=False 
    first2=False
    display.flip()
    
quit()

