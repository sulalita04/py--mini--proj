ques=[
    ["who wrote romio & juliet ?","leo","harry","sekspear","none",3],
    ["What is the chemical symbol for water?", "H2O","No2","chcl","NaCl",1],
    ["Ram mandir was established in which date of dec. 2024?","12","23","06","22",4],
     ["What is the largest planet in our solar system?", "earth","Jupiter","mars","moon",2],
     ["Who painted the Mona Lisa?", "robat sketch","niploma","lopita sekh","Leonardo da Vinci",4],
     [" Shri jagannath temple is in which state?","andhra","bangalor","odisha","gujurat",3],
     ["Shri krishna belong to which bansa ?","surya","jadu","kansa","chandra",2],
     ["Ayodhya is in which state of india?","mp","ad","up","uk",3],
     ["oldest name of odisha?","orisha","utkal","prachina","nabin",2],
     ["Father of java ?"," James Gosling","james croton","robert james","none",1],
     ["Which of the following is a non-volatile memory?","RAM","ROM","Cache","Registers",2],
     ["Which of the following languages is primarily used for artificial intelligence?","C","Java","Lisp","HTML",3],
     ["What does SQL stand for?","Structured Query Language","Stylish Question Language","Statement Question Language","Standard Query Language",1],
     [" Which data structure uses LIFO (Last In, First Out) method?","Queue","Stack","Array","Linked list",2],
     ["In object-oriented programming, encapsulation is most closely related to:","Inheritance","Polymorphism","Abstraction","Information hiding",4],
     [" What is the time complexity of a binary search algorithm?","O(n)","O(n^2)","O(log n)","O(n log n)",3]
  ]
levels =[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,10000000]
money=0

for i in range(0,len(ques)):
    que=ques[i]
    print(f"Question for Rs .{levels[i]}\n")
    print(f"{que[0]}")
  
    print(f"a.{que[1]}      b.{que[2]}")
    print(f"c.{que[3]}      d.{que[4]}")

    ans = int(input("enter your answer :(1-4) "))

    if (ans == que[-1]):
        print(f"correct answer ,you have won Rs .{levels[i]}\n\n")
        if(i==4):
            money =10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
    else:
        print("Wrong answer !!!")
        break
print(f"Your take home money is {money}")
        
