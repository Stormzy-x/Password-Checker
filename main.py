CapitalLetters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]
SmallLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Symbols= ["!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]","|","<",">"]
Numbers=["0","1","2","3","4","5","6","7","8","9"]
#Length,Caps,SmallLETTERS,Symbols,num
Checklist=[False,False,False,False,False]
print("Hello")
Password=input("Pls enter a password")
if len(Password)>8:
   Checklist[0]=True
for C in Password:
  if (C in CapitalLetters):
     Checklist[1]=True
  if (C in SmallLetters):
     Checklist[2]=True
  if (C in Symbols):
     Checklist[3]=True
  if (C in  Numbers):
     Checklist[4]=True  
print(Checklist)
if Checklist==[True,True,True,True,True]: 
  print("Fully Safe Password")
if Checklist[0]==False: 
  print("Requires a standard length of more than 8 characters")
if Checklist[1]==False: 
  print("Requires Capital Letters")
if Checklist[2]==False: 
  print("Requires Small Letters")
if Checklist[3]==False: 
  print("Requires Numbers")
if Checklist[4]==False:
    print("Requires Symbols")


