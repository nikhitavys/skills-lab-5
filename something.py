import random

fortunes = {
1:"you will have a great week",
2:"you will have an eh so good week",
3:"you will have a terrible week"
}
randomNum = random.randint(1,3)
name1 = input("Hello, what is your name? I will predict how your week will go: ")

if(randomNum == 1):
	print(name1 + ",", fortunes[1])
elif(randomNum == 2):
	print(name1 + ",", fortunes[2])
else:
	print(name1 + ",", fortunes[3])
