import random

fortunes = {
1:"You will have a great week",
2:"You will have an eh so good week",
3:"You will have a terrible week"
}
randomNum = random.randint(1,3)
name1 = input("Hello, what is your name? I will predict how your week will go: ")

if(randomNum == 1):
	print(fortunes[1])
elif(randomNum == 2):
	print(fortunes[2])
else:
	print(fortunes[3])
