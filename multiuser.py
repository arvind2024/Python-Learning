class multiple_functions():
    def odd_even():
        numb=int(input("enter your numb :"))
        if numb%2==0:
            print("the given num is even")
        else:
            print("the given num is odd")
     
    def gender():
        gender=input("your gender :")
        age=int(input("your age :"))
        if(gender=="male"):
            if(age<21):
                print("not-eligible")
            else:
                print('eligible')
        else:
            if(age<18):
                print("not-eligible")
            else:
                print("eligible")
                
    def sub():
        sub1=int(input("subject1="))
        sub2=int(input("subject2="))
        sub3=int(input("subject3="))
        sub4=int(input("subject4="))
        sub5=int(input("subject5="))
        total=(sub1+sub2+sub3+sub4+sub5)
        percentage=total/5
        print("total:",total)
        print("percentage:",percentage)
        
    def age():
        age=int(input("enter your age ="))
        if(0<age<12):
            print("child")
        elif(13<age<18):
            print("adult")
        elif(19<age<25):
            print("man or woman")
        elif(26<age<50):
            print("citizen")
        else:
            print("senior citizen")