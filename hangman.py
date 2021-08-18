import random
chance=5
genre=["sports person","food","country"]
print("genres:\n","1.",genre[0],"\n2.",genre[1],"\n3.",genre[2])
choice=int(input("Enter choice number"))
sports=["nadia comaneci","pele","sebastian vettel","charles leclerc","robert james fischer","floyd mayweather"]
food=["bruschetta","quinoa","edamame","tzatziki","charcuterie","bourguignon"]
country=["belarus","papua new guinea","guadeloupe","mozambique","liechtenstein","cambodia"]
if(choice==1):
    question=random.choice(sports)
elif(choice==2):
    question=random.choice(food)
else:
    question=random.choice(country)
question.upper()
print(question)
answer=[]
for k in question:
	answer.append(None)
print(answer)
while(chance!=0):
    print(f"Chances left={chance}")
    char=input("\nEnter any letter")                                         
    char.upper()
    indices=[]
    for i in range(len(question)):
        if question[i]==char:
            indices.append(i)
    if indices:  
        for index in indices:
            if answer[index]==None:
                answer[index]=char
                break 
        print(answer)
        if None not in answer:
            print("Sucess")
            break            
    else:
        chance-=1
    
if chance==0:
    print("Fail")

