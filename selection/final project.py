#Final Project
#Vinay Jayachandiran and Anas Saqib

from pygame import*
from random import*
from math import*

counter=0
screen = display.set_mode((1000,700))
count=0


start = Rect(402,5,197,82)
page="startpage"

count=0
running=True

pics=[[""]*13  for i in range(8)] # ends up a 3-dim list goes character,move,picture
mixer.init(22050,-16,2,4096)
jumpsound = mixer.music.load("Jump Sound.mp3")

collisionl = [image.load("collision"+str(x)+".png") for x in range(1,15)]

ifrontpage = image.load("Front Page copy.jpg")
istart = image.load("start.png")
icontrols = image.load("controls.png")

#setting up all naruto pics
pics[0][0]=[image.load("Naruto\\Stance1"+str(x)+".png") for x in range(1,6)]
pics[0][1]=[image.load("Naruto\\walk1"+str(x)+".jpg") for x in range(1,7)]
pics[0][2]=[image.load("Naruto\\crouch.jpg")]
pics[0][3]=[image.load("Naruto\\jump"+str(x)+".jpg") for x in range(0,4)]
pics[0][4]=[image.load("Naruto\\summon1"+str(x)+".jpg") for x in range(1,13)]
pics[0][5]=[image.load("Naruto\\attack2"+str(x)+".jpg") for x in range(1,49)]
pics[0][6]=[image.load("Naruto\\attack3"+str(x)+".jpg") for x in range(0,58)]
pics[0][7]=[image.load("Naruto\\punch"+str(x)+".jpg") for x in range(0,4)]
pics[0][8]=[image.load("Naruto\\hard punch"+str(x)+".jpg") for x in range(0,4)]
pics[0][9]=[image.load("Naruto\\combo"+str(x)+".jpg") for x in range(0,12)]
pics[0][10] = [image.load("Naruto\\attack30.jpg")]
pics[0][11] = [image.load("Naruto\\run" +str(x)+".png")for x in range(1,7)]
pics[0][12] = "naruto" #so we can keep track of which character we are using
mugshot = image.load("Naruto\\naruto mugshot.png")

#setting up all kisame pics
pics[1][0]=[image.load("Kisame\\stance"+str(x)+".png") for x in range(0,5)]
pics[1][1]=[image.load("Kisame\\walk"+str(x)+".jpg") for x in range(1,6)]
pics[1][2]=[image.load("Kisame\\crouch0.jpg")]
pics[1][3]=[image.load("Kisame\\jump"+str(x)+".jpg") for x in range(0,4)]
pics[1][4]=[image.load("Kisame\\attack2"+str(x)+".jpg") for x in range(0,8)]+[image.load("Kisame\\attack1"+str(x)+".jpg") for x in range(0,14)] #this picture had no hand sign, so we used attack2s signs
pics[1][5]=[image.load("Kisame\\attack2"+str(x)+".jpg") for x in range(0,22)]
pics[1][6]=[image.load("Kisame\\attack3"+str(x)+".jpg") for x in range(0,26)]
pics[1][7]=[image.load("Kisame\\punch"+str(x)+".jpg") for x in range(0,7)]
pics[1][8]=[image.load("Kisame\\hard punch"+str(x)+".jpg") for x in range(0,7)]
pics[1][9]=[image.load("Kisame\\combo"+str(x)+".jpg") for x in range(0,13)]
pics[1][10]=[image.load("Kisame\\guard.jpg")]
pics[1][11]=[image.load("Kisame\\run"+str(x)+".png") for x in range(1,6)]
pics[1][12]="kisame"

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
pics[2][11]=[image.load("Madara\\run"+str(x)+".png") for x in range(1,7)]
pics[2][12]="madara"
mugshot2=image.load("Madara\\Madara mugshot.png")

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
#pics[3][10]=[image.load("Kakashi\\guard.jpg")]
#pics[3][11]=[image.load("Kakashi\\run"+str(x)+".png") for x in range(1,7)]
pics[3][12]="kakashi"
dogs=[image.load("Kakashi\\dogs"+str(x)+".png") for x in range(0,4)]

background = image.load("Ninja Academy.png")
platforms = [Rect(234, 527, 277, 14),Rect(270, 415, 203, 16),Rect(305, 307, 142, 14),Rect(740, 306, 143, 13),Rect(706, 417, 206, 13),Rect(670, 526, 277, 15)]

def stance(x1,y1,direction,row):
    global frame,pics,parea
    cpics = pics[row][0]
    if frame>len(cpics)-1:
        frame=0
    if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1])) #y1-cpics[frame].get_size()[1]), this allows us to blit all picture so that the bottom is at the y level(400)
    else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
    parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    
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



def crouch(x1,y1,direction,row):
    global parea
    cpics = pics[row][2]
    if direction=="right":screen.blit(cpics[0],(x1,y1-cpics[0].get_size()[1]))
    else: screen.blit(transform.flip(cpics[0],x1,0),(x1,y1-cpics[0].get_size()[1]))
    parea=Rect(x1,y1-cpics[0].get_size()[1],cpics[0].get_size()[0],cpics[0].get_size()[1])

def jump(x1,y1,direction,row):
    global pics,frame,jumpdone,parea,yvalue
    cpics = pics[row][3]
    if frame>len(cpics)-2:
        frame=len(cpics)-2
    if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
    if y1>=yvalue:
        jumpdone=True
        mixer.music.load("Jump Sound.mp3")
        mixer.music.play(1,0)
    parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])  

def punch(x1,y1,direction,row):
    global frame,pics,parea,attackarea
    cpics = pics[row][7]
    if frame>len(cpics)-1:
        frame=0
    if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
    parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    attackarea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])    
    
def hardpunch(x1,y1,direction,row):
    global frame,pics,parea,attackarea
    cpics = pics[row][8]
    if frame>len(cpics)-1:
        frame=0
        move="stance"
    if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
    parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    attackarea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])

def combo(x1,y1,direction,row):
    global frame,pics,parea,attackarea
    cpics = pics[row][9]
    if frame>len(cpics)-1:
        frame=0
    if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
    parea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    attackarea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    
def guard(x1,y1,direction,row):
    global parea
    cpics = pics[row][10]
    if direction=="right":screen.blit(cpics[0],(x1,y1-cpics[0].get_size()[1]))
    else: screen.blit(transform.flip(cpics[0],x1,0),(x1,y1-cpics[0].get_size()[1]))
    parea=Rect(x1,y1-cpics[0].get_size()[1],cpics[0].get_size()[0],cpics[0].get_size()[1])
    
# Player 2 -------------------------------------------------------------------

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

def collision(x1,y1):
    global collision,background
    
    for i in collisionl:
        screen.blit(background,(0,0))
        screen.blit(i,(x1,y1))
        display.flip()
        time.wait(100)

#special moves: most special moves are different so each one requires it own code

def narutoattack1(x1,y1,direction):
    global frame,pics,count,attack1done,x,attackarea
    cpics = pics[0][4]
    if frame>len(cpics)-2:
        frame=len(cpics)-2
    if frame>=7:
        if direc=="right": x+=6
        else: x-=6
    if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
    if frame>=7:
         attackarea=Rect(x1,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    count+=1
    if count==150:
        attack1done=True
        count=0
        
def narutoattack2(x1,y1,direction):
    global frame,pics,first,rincrease,lincrease,count,attack2done,attackarea,x,x2
    cpics = pics[0][5]
    if first:
        frame=0
        rincrease=0
        lincrease=100
    if frame<=43:
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
    else:
        if direction=="right":
            screen.blit(cpics[42],(x1,y1-cpics[42].get_size()[1]))
            screen.blit(cpics[44+frame%4],(x1+rincrease,y1-cpics[44+frame%4].get_size()[1]))
            attackarea=Rect(x1+rincrease,y1-cpics[44+frame%4].get_size()[1],cpics[44+frame%4].get_size()[0],cpics[44+frame%4].get_size()[1])
            rincrease+=(x2-(x1+rincrease))/15.0
        else:
            screen.blit(transform.flip(cpics[42],x1,0),(x1,y1-cpics[42].get_size()[1]))
            screen.blit(cpics[44+frame%4],(x1-lincrease,y1-cpics[44+frame%4].get_size()[1]))
            attackarea=Rect(x1-lincrease,y1-cpics[44+frame%4].get_size()[1],cpics[44+frame%4].get_size()[0],cpics[44+frame%4].get_size()[1])
            lincrease+=(x2-(x1-lincrease))/15.0
    if frame>100:
        attack2done=True
    

def narutoattack3(x1,y1,direction):
    global frame,pics,first,attack3done,attackarea,x2,y2,x
    cpics = pics[0][6]
    if frame==35:
       x=x2-100
       x1=x
    if first:
        frame=0
    if frame==44:
        frame=48
    if frame<=43:
        if direction=="right":screen.blit(cpics[frame],(x1,y1-cpics[frame].get_size()[1])) 
        else: screen.blit(transform.flip(cpics[frame],x1,0),(x1,y1-cpics[frame].get_size()[1]))
    elif frame!=36 and frame!=37 and frame!=35:
        if direction=="right":
            screen.blit(cpics[46],(x1,y1-cpics[46].get_size()[1]))
            screen.blit(cpics[frame],(x1+50,y1-cpics[frame].get_size()[1]))
            attackarea=Rect(x1+50,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
        else:
            screen.blit(transform.flip(cpics[46],x1,0),(x1,y1-cpics[46].get_size()[1]))
            screen.blit(cpics[frame],(x1-100,y1-cpics[frame].get_size()[1]))
            attackarea=Rect(x1-100,y1-cpics[frame].get_size()[1],cpics[frame].get_size()[0],cpics[frame].get_size()[1])
    if frame+1==len(cpics):
        attack3done=True

def kisameattack1(x1,y1,direction):
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

def kisameattack2(x1,y1,direction):
    global frame2,pics,attack2done2,attackarea2
    cpics = pics[1][5]
    if frame2>len(cpics)-1:
        frame2=0
    if direction=="right":screen.blit(cpics[frame2],(x1-((cpics[frame2].get_size()[0])/2.0),y1-cpics[frame2].get_size()[1])) #(x1-((cpics[frame2].get_size()[0])/2.0), since the sharks come around him, he has to stay in the middle, this is what it does
    else: screen.blit(transform.flip(cpics[frame2],x1,0),((x1-((cpics[frame2].get_size()[0])/2.0),y1-cpics[frame2].get_size()[1])))
    attackarea2=Rect((x1-((cpics[frame2].get_size()[0])/2.0),y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1]))
    if frame2+1==len(cpics):
        attack2done2 =True
    

def kisameattack3(x1,y1,direction):
    global frame2,pics,attack3done2,attackarea2
    cpics = pics[1][6]
    if frame2>len(cpics)-1:
        frame2=0
    if direction=="right":screen.blit(cpics[frame2],(x1-((cpics[frame2].get_size()[0])/2.0),y1-cpics[frame2].get_size()[1]))
    else: screen.blit(transform.flip(cpics[frame2],x1,0),((x1-((cpics[frame2].get_size()[0])/2.0),y1-cpics[frame2].get_size()[1])))
    attackarea2=Rect((x1-((cpics[frame2].get_size()[0])/2.0),y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1]))
    if frame2+1==len(cpics):
        attack3done2 =True

def madaraattack1(x1,y1,direction):
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

def madaraattack2(x1,y1,direction):
    global frame2,pics,attack2done2,attackarea2,framedelay2,x
    cpics = pics[2][5]
    
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
             attackarea2=Rect(x,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
         else:
             #screen.blit(transform.flip(cpics[frame2],x1-50*frame2,0),(x1-50*frame2,y1-cpics[frame2].get_size()[1]))
             #attackarea2=Rect(x1-50*frame2,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
             screen.blit(transform.flip(cpics[frame2],x,0),(x,y1-cpics[frame2].get_size()[1]))
             attackarea2=Rect(x,y1-cpics[frame2].get_size()[1],cpics[frame2].get_size()[0],cpics[frame2].get_size()[1])
         
    if frame2+1==len(cpics):
        attack2done2 =True


def madaraattack3(x1,y1,direction):
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
    summond=15
    counter=1
def kakashiattack1 (x1,y1,direction):
    global frame2,pics,attack1done2,attackarea2,summond
    cpics = pics[3][4]
    #if frame2>len(cpics):
    #    frame2=0
    if frame2<12:
        if direc2=="right":screen.blit(cpics[frame2%12],(x1,y1-cpics[frame2%12].get_size()[1]))
        else:screen.blit(transform.flip(cpics[frame2%12],x1,0),(x1,y1-cpics[frame2%12].get_size()[1]))
    if frame2>11:
        if direc2=="right":
            screen.blit(dogs[frame2%3],(x1+summond,y1-dogs[frame2%3].get_size()[1]))
            screen.blit(cpics[11],(x1,y1-cpics[11].get_size()[1]))
            attackarea2=Rect((x1+summond,y1-dogs[frame2%3].get_size()[1],dogs[frame2%3].get_size()[0],dogs[frame2%3].get_size()[1]))
            summond+=15
        else:
            screen.blit(transform.flip(dogs[frame2%3],x1+summond,0),(x1+summond,y1-dogs[frame2%3].get_size()[1]))
            screen.blit(transform.flip(cpics[11],x1,0),(x1,y1-cpics[11].get_size()[1]))
            attackarea2=Rect((x1+summond,y1-dogs[frame2%3].get_size()[1],dogs[frame2%3].get_size()[0],dogs[frame2%3].get_size()[1]))
            summond-=15
    if x1+summond>999 or x1+summond<0:
        attack1done2=True
        summond=15
def kakashiattack2 (x1,y1,direction):
    global frame2,pics,attack2done2,attackarea2,summond  
    cpics = pics[3][5]
    c2pics=pics[3][4]
    if frame2<12:
        if direc2=="right":screen.blit(c2pics[frame2%12],(x1,y1-c2pics[frame2%12].get_size()[1]))
        else:screen.blit(transform.flip(c2pics[frame2%12],x1,0),(x1,y1-c2pics[frame2%12].get_size()[1]))
    if frame2>11:
        if direc2=="right":
            screen.blit(cpics[frame2%9],(x1+summond,y1-cpics[frame2%9].get_size()[1]))
            screen.blit(c2pics[11],(x1,y1-c2pics[11].get_size()[1]))
            attackarea2=Rect((x1+summond,y1-dogs[frame2%3].get_size()[1],dogs[frame2%3].get_size()[0],dogs[frame2%3].get_size()[1]))
            summond+=15
        else:
            screen.blit(transform.flip(cpics[frame2%9],x1+summond,0),(x1+summond,y1-cpics[frame2%9].get_size()[1]))
            screen.blit(transform.flip(c2pics[11],x1,0),(x1,y1-c2pics[11].get_size()[1]))
            attackarea2=Rect((x1+summond,y1-dogs[frame2%3].get_size()[1],dogs[frame2%3].get_size()[0],dogs[frame2%3].get_size()[1]))
            summond-=15
    if x1+summond>999 or x1+summond<0:
        attack2done2=True
        summond=15

def kakashiattack3 (x1,y1,direction):
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
        
# PLAYER 1 ----------------------------------------------------------------------------        

x,y=300,700
yvalue=700
rincrease,lincrease,ryincrease,lyincrease=0,0,0,0 #for some reason, if i defined these in the function i got an error
yincrease=-20
char="naruto"
direc="right"
prevmove=""
count=0
row=0
first=False
jumpdone=True
attack1done=True
attack2done=True
attack3done=True
frame=0
frameDelay=4
move=""
attack=""
health=250
damage=0
chakra=0
parea=Rect(0,0,0,0)
attackarea = Rect(0,0,0,0)
healthbar = Rect(70,10,health,30)
chakrabar = Rect(70,50,chakra,20)
walkcount=0
# PLAYER 2 ----------------------------------------------------------------------------
#we use all the same variables except add a 2 in the end for character 2


x2,y2=700,700
yvalue2=700
rincrease2,lincrease2=0,0 
yincrease2=-20
char2="kakashi"
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
frame2=0
frameDelay2=4
health2=250
damage2=0
chakra2=0
p2area=Rect(0,0,0,0)
attackarea2=Rect(0,0,0,0)
healthbar2 = Rect(930,10,(-1)*health2,30)
chakrabar2 = Rect(930,50,(-1)*chakra2,20)
counter=0
             
for line in range(len(pics)): #finds the row with all the character 1 pics
    if pics[line][12]==char:
        row=line

for line in range(len(pics)): #finds the row with all the character 2 pics
    if pics[line][12]==char2:
        row2=line
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running=False
        elif key.get_pressed():
            if move=="stance":
                first=True
        if evt.type == MOUSEBUTTONDOWN:
            sx,sy=mouse.get_pos()
        #if evt.type == MOUSEBUTTONUP:
            #print rectarea
            
    mx,my = mouse.get_pos()
    keys = key.get_pressed()
    mb = mouse.get_pressed()

    if page=="startpage":
        screen.blit(ifrontpage,(0,0))
        screen.blit(istart,(401,5))
        screen.blit(icontrols,(1000-193,0))
        if start.collidepoint((mx,my)) and mb[0]==1:
            page="fightpage"

    elif page=="fightpage":
        screen.blit(background,(0,0))
        #screen.fill((0,128,1))

        chakra=250
        chakra2=250
        
        draw.rect(screen,(111,111,111),(68,8,254,34),0)
        draw.rect(screen,(111,111,111),(932,8,-254,34),0)
        draw.rect(screen,(0,255,100),healthbar,0)
        draw.rect(screen,(0,255,100),healthbar2,0)

        draw.rect(screen,(111,111,111),(68,48,254,24),0)
        draw.rect(screen,(111,111,111),(932,48,-254,24),0)
        draw.rect(screen,(50,0,255),chakrabar,0)
        draw.rect(screen,(50,0,255),chakrabar2,0)

        screen.blit(mugshot,(0,0))
        screen.blit(mugshot2,(930,0))

        attackarea=Rect(0,0,0,0)
        attackarea2=Rect(0,0,0,0)

        if mb[0]==1:
            draw.rect(screen,(255,0,0),(sx,sy,mx-sx,my-sy),2)
            rectarea = "Rect"+str((sx,sy,mx-sx,my-sy))

        # PLAYER 1 ----------------------------------------------------------------------------

        if x<0:
            x=1000
            direc="left"
        elif x>1000:
            x=0
            direc="right"

        if keys[K_a]==1:
            move="walk"
        elif keys[K_d]==1:
            move="walk"
            if walkcount>0 and prevmove!="walk":
                move="run"    
            walkcount=15
            
        elif keys[K_w]==1 and keys[K_s]==1 and prevmove!="jump":
            chakra+=0.25
        elif keys[K_s]==1:
            move="crouch"
        elif keys[K_w]==1 and y<=yvalue:
            jumpdone=False
            move="jump"
        elif keys[K_t]==1 and prevmove!="attack1" and prevmove!="attack2" and prevmove!="attack3" and chakra>=83:
            move="attack1"
            chakra-=40
            attack1done=False
        elif keys[K_y]==1 and prevmove!="attack2" and prevmove!="attack3" and prevmove!="attack1" and chakra>=166:
            move="attack2"
            chakra-=80
            attack2done=False
        elif keys[K_u]==1 and prevmove!="attack3" and prevmove!="attack2" and prevmove!="attack1" and chakra>=250:
            move="attack3"
            chakra-=125
            attack3done=False
        elif keys[K_h]==1 and keys[K_g]==1:
            move="combo" 
        elif keys[K_g]==1 :
            move="punch"
        elif keys[K_h]==1 :
            move="hardpunch"
        elif keys[K_j]==1:
            move="guard"
        elif keys[K_r]==1:
            move="run"
        else:
            move="stance"
            
        if jumpdone==False:
            move="jump"
       
        if move=="jump":
            if keys[K_a]==1:
                x-=5
                direc="left"
            elif keys[K_d]==1:
                x+=5
                direc="right"
            elif keys[K_s]==1:
                if yincrease<0:
                    yincrease=5
                y+=5
                
        elif attack1done==False:
            move="attack1"
       
        elif attack2done==False:
            move="attack2"

        elif attack3done==False:
            move="attack3"

        if move!="jump":
            y=yvalue
            yincrease=-20
        
        # PLAYER 2 ----------------------------------------------------------------------------

        if x2<0:
            x2=1000
            direc2="left"
        elif x2>1000:
            x2=0
            direc2="right"

        if keys[K_LEFT]==1:
            move2="walk"
        elif keys[K_RIGHT]==1:
            move2="walk"
        elif keys[K_UP]==1 and keys[K_DOWN]==1:
            chakra2+=0.25
        elif keys[K_DOWN]==1:
            move2="crouch"
        elif keys[K_UP]==1 and y2<=yvalue2:
            jumpdone2=False
            move2="jump"
        elif keys[K_KP4]==1 and prevmove2!="attack1" and prevmove2!="attack2" and prevmove2!="attack3" and chakra2>=83:
            move2="attack1"
            chakra2-=40
            attack1done2=False
        elif keys[K_KP5]==1 and prevmove2!="attack1" and prevmove2!="attack2" and prevmove2!="attack3" and chakra2>=166:
            move2="attack2"
            chakra2-=80
            attack2done2=False
        elif keys[K_KP6]==1 and prevmove2!="attack1" and prevmove2!="attack2" and prevmove2!="attack3" and chakra2>=250:
            move2="attack3"
            chakra2-=125
            attack3done2=False
        elif keys[K_KP1]==1 and keys[K_KP2]==1:
            move2="combo" 
        elif keys[K_KP1]==1 :
            move2="punch"
        elif keys[K_KP2]==1 :
            move2="hardpunch"
        elif keys[K_KP3]==1 :
            move2="guard"
        elif keys[K_KP9]==1:
            move2="run"
        else:
            move2="stance"

        if jumpdone2==False:
            move2="jump"

        if move2=="jump":
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

        

        if move2!="":
            if move2=="stance":
                eval("stance2(x2,y2,direc2,row2)")
            elif move2=="walk":
                eval("walk2(x2,y2,direc2,row2)")
                if keys[K_LEFT]==1:
                    direc2="left"
                elif keys[K_RIGHT]==1:
                    direc2="right"
            elif move2=="run":
                eval("run2(x2,y2,direc2,row2)")
                if keys[K_LEFT]==1:
                    direc2="left"
                elif keys[K_RIGHT]==1:
                    direc2="right"
            elif move2 == "crouch":
                eval("crouch2(x2,y2,direc2,row2)")
            elif move2 == "jump":
                if frameDelay2%2==0:
                    y2+=yincrease2
                    yincrease2+=.75
                if y2>=yvalue2:
                    jumpdone2=True
                if keys[K_KP1]==1 and keys[K_KP2]==1:
                    move2="combo"
                elif keys[K_KP1]==1:
                    move2="punch"
                elif keys[K_KP2]==1:
                    move2="hardpunch"
                else:
                    eval("jump2(x2,y2,direc2,row2)")
            elif move2 == "guard":
                eval("guard2(x2,y2,direc2,row2)")
                
        # PLAYER 1 ----------------------------------------------------------------------------
        
        if move!="":
            if move=="stance":
                eval("stance(x,y,direc,row)")
            elif move=="walk":
                eval("walk(x,y,direc,row)")
                if keys[K_a]==1:
                    direc="left"
                elif keys[K_d]==1:
                    direc="right"
            elif move=="run":
                eval("run(x,y,direc,row)")
                if keys[K_a]==1:
                    direc="left"
                elif keys[K_d]==1:
                    direc="right"
            elif move == "crouch":
                eval("crouch(x,y,direc,row)")
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
                    eval("jump(x,y,direc,row)")
            elif move == "attack1":
                eval(char+"attack1(x,y,direc)")
            elif move == "attack2":
                eval(char+"attack2(x,y,direc)")
            elif move == "attack3":
                eval(char+"attack3(x,y,direc)")
            elif move=="guard":
                eval("guard(x,y,direc,row)")
            if move == "combo":
                eval("combo(x,y,direc,row)")
            elif move == "punch":
                eval("punch(x,y,direc,row)")
            elif move == "hardpunch":
                eval("hardpunch(x,y,direc,row)")

            #Player 2 attacks, they are here so they are in front of Naruto
            if move2 == "attack1":
                eval(char2+"attack1(x2,y2,direc2)")
            elif move2 == "attack2":
                eval(char2+"attack2(x2,y2,direc2)")
            elif move2 == "attack3":
                eval(char2+"attack3(x2,y2,direc2)")
            elif move2 == "combo":
                eval("combo2(x2,y2,direc2,row2)")
            elif move2 == "punch":
                eval("punch2(x2,y2,direc2,row2)")
            elif move2 == "hardpunch":
                eval("hardpunch2(x2,y2,direc2,row2)")

        if parea.colliderect(attackarea2):
            if move2=="punch":
                damage=0.01
                chakra2+=0.02
            elif move2=="hardpunch":
                damage=0.09
                chakra2+=0.18
            elif move2=="combo":
                damage=0.1
                chakra2+=0.2
            elif move2=="attack1":
                damage=1
            elif move2=="attack2":
                damage=1.5
            elif move2=="attack3":
                damage=2
            if move=="guard":
                damage-=0.08
            health-=damage

        if parea2.colliderect(attackarea):
            if move=="punch":
                damage2=0.01
                chakra+=0.02
            elif move=="hardpunch":
                damage2=0.09
                chakra+=0.4
            elif move=="combo":
                damage2=0.1
                chakra+=0.2
            elif move=="attack1":
                damage2=1
            elif move=="attack2":
                damage2=1.5
            elif move=="attack3":
                damage2=2
            if move2=="guard":
                damage2=0.08
            health2-=damage2

        if move=="attack1" or move=="attack2" or move=="attack3":
            if move2=="attack1" or move2=="attack2" or move2=="attack3":
                if attackarea.colliderect(attackarea2):
                    move=""
                    move2=""
                    attack1done=True
                    attack2done=True
                    attack3done=True
                    attack1done2=True
                    attack2done2=True
                    attack3done2=True
         
        if chakra>=250:
            chakra=250

        if chakra2>=250:
            chakra2=250

        # Checking to see if charachter is on a platform

        if yincrease>0: #this makes the landing smoother, they can only land if they are going down
            for rect in platforms:
                if rect.colliderect(parea):
                    yvalue=rect[1]+1 #this ensures that once they get on platform they stay there
                    break

        if move!="jump" and yvalue!=700: #if move is jump, the yincrease gets messed up
            
            for rect in platforms:
                if rect.colliderect(parea):
                    break
                if rect==platforms[-1]: #if it is the last platform and the character is not on it, we go back to ground level
                    move="jump"
                    jumpdone=False
                    yincrease=5
                    yvalue=700
                    
        if yincrease2>0:
            for rect in platforms:
                if rect.colliderect(parea2) :
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

        
        
        healthbar = Rect(70,10,1*health,30)
        healthbar2 = Rect(930,10,(-1)*health2,30)

        chakrabar = Rect(70,50,chakra,20)
        chakrabar2 = Rect(930,50,(-1)*chakra2,20)

        if health<0 or health2<0:
            page="startpage"
            health=250
            health2=250
            chakra,chakra2 = 0,0
        
        walkcount-=1
        frameDelay -= 1                         # count down to zero
        if frameDelay == 0:                     # then advance frame like normal
            frameDelay = 4
            frame+=1
        prevmove=move

        frameDelay2 -= 1                         # count down to zero
        if frameDelay2 == 0:                     # then advance frame like normal
            frameDelay2 = 4
            frame2 += 1
        prevmove2=move2
        counter+=1
        
    first=False
    display.flip()
quit()
