import random
from datetime import datetime
 
def generator():
    
    num1 = random.randrange(366)
    num2 = random.randrange(366)
    if(num1 == num2):
        num2 = random.randrange(366)
    
    num3 = random.randrange(366)
    if((num1==num3) | (num2==num3)):
        num3 = random.randrange(366)
        
    num4 = random.randrange(366)
    if((num1==num4) | (num2==num4) | (num3==num4)):
        num4 = random.randrange(366)
        
    num5 = random.randrange(366)
    if((num1==num5) | (num2==num5) | (num3==num5) | (num4==num5)):
        num5 = random.randrange(366)
        
        
    myArr = [num1,num2,num3,num4,num5]
    return myArr


def convertToDate(toConv):
    
    str = ""
    
    if(toConv < 31):
        str = "January {num}".format(num = toConv)
        print(str)
        
    elif(toConv < 59):
        toConv = toConv - 31
        str = "February {num}".format(num = toConv)
        print(str)
        
    elif(toConv < 90):
        toConv = toConv - 59
        str = "March {num}".format(num = toConv)
        print(str)
        
    elif(toConv < 120):
        toConv = toConv - 90
        str = "April {num}".format(num = toConv)
        print(str)
        
    elif(toConv < 151):
        toConv = toConv - 120
        str = "May {num}".format(num = toConv)
        print(str)
        
    elif(toConv < 181):
        toConv = toConv - 151
        str = "June {num}".format(num = toConv)
        print(str)
        
    elif(toConv < 212):
        toConv = toConv - 181
        str = "July {num}".format(num = toConv)
        print(str)
        
    elif(toConv < 243):
        toConv = toConv - 212
        str = "August {num}".format(num = toConv)
        print(str)
        
    elif(toConv < 273):
        toConv = toConv - 243
        str = "September {num}".format(num = toConv)
        print(str)
        
    elif(toConv < 304):
        toConv = toConv - 273
        str = "October {num}".format(num = toConv)
        print(str)
        
    elif(toConv < 334):
        toConv = toConv - 304
        str = "November {num}".format(num = toConv)
        print(str)
        
    else:
        toConv = toConv - 334
        str = "December {num}".format(num = toConv)
        print(str)
    


def main():
    dateArr = generator()
    
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
    
    
if __name__ == "__main__":
    main()
    