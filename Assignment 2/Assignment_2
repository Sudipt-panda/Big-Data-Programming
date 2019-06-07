from random import randrange,choice,shuffle
from time import sleep
#################################################
clist=[]
outdated=set() #initialise outdated set
rstatus=False
def main():
    q1=input('Enter name of player 1 :: ') #input player names
    q2=input('Enter name of player 2 :: ')
    p1=Player(q1) #storing player details
    p2=Player(q2)
    distribute_cards(p1,p2) #calling function to distribute cards to players
    print('Throw Dice.....')
    sleep(1)
    #dice throw to determine who will start the game
    ps1=p1.throw_dice()
    print('For Player ',p1.name,' Dice Score is ',ps1)
    sleep(1)
    ps2=p2.throw_dice()
    print('For Player ',p2.name,' Dice Score is ',ps2)
    p=None
    if ps1>ps2:
        print(p1.name,' has to start Game...')
        start_round(p1,p2)
    else:
        print(p2.name,' has to start Game...')
        start_round(p2,p1)        
#################################################
def show_winner(p1,p2): #function to display winner
    sleep(2)
    if p1.point>p2.point :
        print('Congratulations ',p1.name,' u have won the Game....')
    elif p1.point==p2.point :
        print('Congratulations The Game is DRAW....')    
    else:
        print('Congratulations ',p2.name,' u have won the Game....')    

#################################################
def resurrect_spell(p2): #resurrect spell for player 2
     global rstatus
     if not p2.resurrect_status and  rstatus:
        conf=input(p2.name+' ,Do u want to take Resurrect Spell Now (press y or n) ')
        if conf.lower()=='y' :
            p2.resurrect_status=True
            if len(outdated)!=0:
                n=randrange(0,len(outdated)-1)
                outdated.add(n)
                p2.card.append(outdated.pop())
                #p2.card.append(outdated.pop(randrange(0,(len(outdated)-1))))
#################################################
def start_round(p1,p2): #function for each round
    global rstatus
    if((len(p1.card)==0) or (len(p1.card)==0)): #checking if either player's deck is empty
        show_winner(p1,p2)       #display winner, which marks end of the game 
        return 
    
    print('=======Round  Starts=====================================')
    sleep(2)
    p1.show_cards() #display card id's left in each players deck
    sleep(1)
    p2.show_cards()
    sleep(1)
    st_p1resurrect=False #resurrect spell cannot be used in the 1st round as there are no cards in outdated deck
    if not p1.resurrect_status and  rstatus :
        conf=input(p1.name+' ,Do u want to take Resurrect Spell Now (press y or n) ') #resurrect spell for 1st player
        if conf.lower()=='y' :
            p1.resurrect_status=True
            st_p1resurrect=True
            if len(outdated)!=0:
                n=randrange(0,len(outdated)-1) #picking random card from outdated deck
                outdated.add(n)
                p1.card.append(outdated.pop()) #adding random card from outdated deck as the topmost card in player deck
                #p1.card.append(outdated.pop(randrange(0,len(outdated)-1)))
    n1=p1.pop()
    print('===========',p1.name,"'s picked Card=====================")
    clist[n1-1].show_details()
    sleep(1)
    challenge=input(p1.name+',pls Enter Character to Challenge(population/gdp/area/lexpectancy) ')
    n2=0
    if not p1.god_status and not st_p1resurrect :
        conf=input(p1.name+' ,Do u want to take God Spell Now (press y or n) ')
        if conf.lower()=='y' :
            p1.god_status=True
            n2=p2.get(p2.retrieve_gspell())
            if not p2.resurrect_status :
                resurrect_spell(p2)      #resurrect spell for player 2 when player 1 chooses god spell      
        else:
            resurrect_spell(p2) # unconditional resurrect spell for player 2
            n2=p2.pop()
    else:
        resurrect_spell(p2)
        n2=p2.pop()
    print('===========',p2.name,"'s picked Card=====================")
    clist[n2-1].show_details()
    sleep(1)
    #checking stregth of the characteristic of each player
    if(challenge.lower()=='population'):
        cn1=clist[n1-1].getpopulation_strength()
        cn2=clist[n2-1].getpopulation_strength()
    elif(challenge.lower()=='gdp'):
        cn1=clist[n1-1].getgdp_strength()
        cn2=clist[n2-1].getgdp_strength()
    elif(challenge.lower()=='area'):
        cn1=clist[n1-1].getarea_strength()
        cn2=clist[n2-1].getarea_strength()    
    elif(challenge.lower()=='lexpectancy'):
        cn1=clist[n1-1].getlexpectancy_strength()
        cn2=clist[n2-1].getlexpectancy_strength() 

    outdated.add(n1) #adding current cards of players used in current round to outdated deck
    outdated.add(n2)    
    print('=====outdated ===',outdated)
    rstatus=True
    #incrementing points
    if(cn1>cn2):
        p1.incr_points()
        print('=======This round won by ',p1.name,'==============')
        start_round(p1,p2)
    else:
        p2.incr_points()
        print('=======This round won by ',p2.name,'==============')
        start_round(p2,p1)
        
    
#################################################
        
def distribute_cards(p1,p2): #function to distribute cards to players evenly
    global clist
    clist=init_characters()
    shuffle(clist)
#     for i in clist:
#           i.show_details()
         
    #flag=True
    
    #method to distribute even position cards to one player and odd position cards to 2nd player
    lst=[]
    while True:
        c=randrange(1,len(clist)+1)
        if c in lst:
            continue
        lst.append(c)    
        '''if flag:
           p1.push(c)
        else:
           p2.push(c)
        flag=not flag'''
        if c%2==0:
            p1.push(c)
        else:
            p2.push(c)
        if p1.current_cards()==len(clist)/2 and p2.current_cards()==len(clist)/2:
            break
    sleep(1)    #lag the display
    p1.show_cards()
    sleep(1)
    p2.show_cards()
###################################################
class Player: #function to store player details
    def __init__(self,name): 
        self.name=name #player name
        self.card=[] #list to hold cards for each player
        self.point=0 #points of player
        self.god_status=False #boolean value to check whether player has used spell or not
        self.resurrect_status=False

    def push(self,cno): #push cards into individual player deck
        self.card.append(cno)
    def pop(self): #pop top-most card from player deck
        if(len(self.card)!=0):
           return self.card.pop()
        return 0
    def get(self,pos): #pop specific card from the player's deck (to be used in god-spell)
        if(len(self.card)!=0):
           return self.card.pop(pos)
        return 0
    def show_cards(self): #display current card of player
        print('----------------------------')
        print('Name Player : ',self.name)
        print('Cards are...',self.card)
        print('Current point of Player is ::',self.point)
        
    def current_cards(self): #return total number of cards in player deck
        return len(self.card)
    def throw_dice(self): #funciton to generate dice throw
        return randrange(1,7)
    def incr_points(self): #increment points for winning player
        self.point+=1
    def retrieve_gspell(self): #function to get count of opponent's deck for god spel;
        n=int(input('Enter card no between 0 & '+str(len(self.card)-1)))
    #    return randrange(0,len(self.card))
        return n
    
##################################################
def init_characters(): #function to initialise card values
    
    
#     no=int(input('Enter No of Cards :: '))
#     cnames=[]
#     for i in range(1,no+1):
#         cnames.append('Character :'+str(i))
    clist=[]    
#     for i in cnames:
#        c=Character(i,randrange(1,500,2),randrange(-100,-20,1),randrange(90,250,1))
#        #c.show_details()
    c=Character('India',1339,2651,3287,68)
    clist.append(c)
    c1=Character('Germany',82,3693,35,81)
    clist.append(c1)
    c2=Character('USA',325,19485,9834,78)
    clist.append(c2)
    c3=Character('Japan',126,4872,37,86)
    clist.append(c3)
    c4=Character('France',67,2583,64,82)
    clist.append(c4)
    c5=Character('Italy',60,1944,30,83)
    clist.append(c5)
    c6=Character('China',1386,12238,9597,76)
    clist.append(c6)
    c7=Character('Britain',31,2709,25,74)
    clist.append(c7)
    c8=Character('Malaysia',32,314,33,77)
    clist.append(c8)
    c9=Character('Singapore',5,323,7,80)
    clist.append(c9)
    c10=Character('Brazil',209,2054,8516,75)
    clist.append(c10)
    c11=Character('Australia',24,1323,769,84)
    clist.append(c11)
    c12=Character('Pakistan',197,30,88,66)
    clist.append(c12)
    c13=Character('Bangladesh',164,24,14,71)
    clist.append(c13)
    c14=Character('Kenya',49,79,58,67)
    clist.append(c14)
    c15=Character('South-Africa',56,348,122,63)
    clist.append(c15)
    c17=Character('Zimbave',16,22,39,61)
    clist.append(c17)
    c18=Character('Russia',144,1578,17123,72)
    clist.append(c18)
   

#        clist.append(c)
    return clist   
       
#################################################       
class Character: #class character which holds details of each card
    c=1
    def __init__(self,name,fv,sv,hv,kv):
        self.id=Character.c #store the id
        self.name=name #store name of the card
        self.d={"population":fv,"gdp":sv,"area":hv,"lexpectancy":kv} #store charcaters and its stregth in a dictionary as key-value pair
        Character.c=Character.c+1 #increment card id
    
    def show_details(self): #function to display card detai;s
        print('Details of Character & its Characterstics Strength are ::')
        print('*****Id :'+str(self.id))
        print('*****Name : ',self.name)
        for k,v in self.d.items():
            print(k,'*****',v)
        print('---------------')    

    #functions to get stregth of each characteristics     
    def getpopulation_strength(self): 
         return self.d['population']

    def getgdp_strength(self):
         return self.d['gdp']
        
    def getarea_strength(self):
         return self.d['area'] 
                
    def getlexpectancy_strength(self):
         return self.d['lexpectancy']
        

########################################################################
    
if __name__ == '__main__': #function to call main
    main()
