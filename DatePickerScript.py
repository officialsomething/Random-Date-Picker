import random
from datetime import datetime
 
def generator(flag):
    
    if(flag == 1):
        toGen = 364
    else:
        toGen = 365
    
    num1 = random.randrange(toGen)
    num2 = random.randrange(toGen)
    if(num1 == num2):
        num2 = random.randrange(toGen)
    
    num3 = random.randrange(364)
    if((num1==num3) | (num2==num3)):
        num3 = random.randrange(toGen)
        
    num4 = random.randrange(toGen)
    if((num1==num4) | (num2==num4) | (num3==num4)):
        num4 = random.randrange(toGen)
        
    num5 = random.randrange(toGen)
    if((num1==num5) | (num2==num5) | (num3==num5) | (num4==num5)):
        num5 = random.randrange(toGen)
        
        
    myArr = [num1,num2,num3,num4,num5]
    return myArr


def convertToDate(toConv):    
    str = ""
    
    if(toConv <= 31):
        str = "January {num}".format(num = toConv)
        
    elif(toConv <= 59):
        toConv = toConv - 31
        str = "February {num}".format(num = toConv)
        
    elif(toConv <= 90):
        toConv = toConv - 59
        str = "March {num}".format(num = toConv)
        
    elif(toConv <= 120):
        toConv = toConv - 90
        str = "April {num}".format(num = toConv)
        
    elif(toConv <= 151):
        toConv = toConv - 120
        str = "May {num}".format(num = toConv)
        
    elif(toConv <= 181):
        toConv = toConv - 151
        str = "June {num}".format(num = toConv)
        
    elif(toConv <= 212):
        toConv = toConv - 181
        str = "July {num}".format(num = toConv)
        
    elif(toConv <= 243):
        toConv = toConv - 212
        str = "August {num}".format(num = toConv)
        
    elif(toConv <= 273):
        toConv = toConv - 243
        str = "September {num}".format(num = toConv)
        
    elif(toConv <= 304):
        toConv = toConv - 273
        str = "October {num}".format(num = toConv)
        
    elif(toConv <= 334):
        toConv = toConv - 304
        str = "November {num}".format(num = toConv)
        
    else:
        toConv = toConv - 334
        str = "December {num}".format(num = toConv)
    
    print(str)
    
def convertToDate_LeapYear():
    str = ""
    
    if(toConv <= 31):
        str = "January {num}".format(num = toConv)
        
    elif(toConv <= 60):
        toConv = toConv - 31
        str = "February {num}".format(num = toConv)
        
    elif(toConv <= 91):
        toConv = toConv - 60
        str = "March {num}".format(num = toConv)
        
    elif(toConv <= 121):
        toConv = toConv - 91
        str = "April {num}".format(num = toConv)
        
    elif(toConv <= 152):
        toConv = toConv - 121
        str = "May {num}".format(num = toConv)
        
    elif(toConv <= 182):
        toConv = toConv - 152
        str = "June {num}".format(num = toConv)
        
    elif(toConv <= 213):
        toConv = toConv - 182
        str = "July {num}".format(num = toConv)
        
    elif(toConv <= 244):
        toConv = toConv - 213
        str = "August {num}".format(num = toConv)
        
    elif(toConv <= 274):
        toConv = toConv - 244
        str = "September {num}".format(num = toConv)
        
    elif(toConv <= 305):
        toConv = toConv - 274
        str = "October {num}".format(num = toConv)
        
    elif(toConv <= 335):
        toConv = toConv - 305
        str = "November {num}".format(num = toConv)
        
    else:
        toConv = toConv - 335
        str = "December {num}".format(num = toConv)
    
    print(str)

def main():
    
    currYear = datetime.now().year
    if((currYear % 4) == 0):
        flag = 1
    else:
        flag = 0

    dateArr = generator(flag)
    
    if(flag == 0):                
        toConv = dateArr[0]
        convertToDate(toConv)
            
        toConv = dateArr[1]
        convertToDate(toConv)
            
        toConv = dateArr[2]
        convertToDate(toConv)
            
        toConv = dateArr[3]
        convertToDate(toConv)
            
        toConv = dateArr[4]
        convertToDate(toConv)
        
    else:
        toConv = dateArr[0]
        convertToDate_LeapYear(toConv)
            
        toConv = dateArr[1]
        convertToDate_LeapYear(toConv)
            
        toConv = dateArr[2]
        convertToDate_LeapYear(toConv)
            
        toConv = dateArr[3]
        convertToDate_LeapYear(toConv)
            
        toConv = dateArr[4]
        convertToDate_LeapYear(toConv)
    
    
if __name__ == "__main__":
    main()
    