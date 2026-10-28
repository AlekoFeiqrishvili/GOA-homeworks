# 2) მომხმარებელს შემოაყვანინე სამი რიცხვი, ხოლო პროგრამამ დაბეჭდოს მათი საშუალო არითმეტიკული.

# 3) მომხმარებელს შემოატანინე ორი რიცხვი და დაბეჭდე მათი ჯამი.

# 4) input ფუნქციის საშუალებით შემოიყვანეთ თქვენი და თქვენი ოჯახის წევრების სახელები და დაპრინტეთ ერთი დიდი წინადადება კონკატენაციის სახით.

# 5) მომხმარებელს შემოატანინეთ მისი ქალაქის, უბნის, კორპუსის და სართულის შესახებ ინფორმაცია
#  (რომლებიც უნდა შეინახოთ ცალ-ცალკე ცვლადებში). მაგ. city = "Tbilisi", District = "{თქვენი უბანი}"
#  და ა.შ. საბოლოოდ print() ბრძანების საშუალებით ტერმინალში გამოიტანეთ მომხმარებლის სრული მისამართი.

# 6) მომხმარებელს შემოატანინეთ ასაკი და ამოყენებითმსგავსი ფორმატის წინადადება: 
# "You are ასაკი years old".

num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
num3 = int(input("Third Number: "))
print((num1 + num2 + num3)/3)

num_1 = int(input("First Number: "))
num_2 = int(input("Second Number: "))
print(num_1 + num_2)

Me = input("My name: ")
Mom = input("My mom's name: ")
Dad = input("My dad's name: ")
print(Me + Mom + Dad)

City = "Tbilisi"
District = " Varketili"
Building = " Archi's B"
Floor = " Sixth"
print(City + District + Building + Floor)

Age = str(input("Your Age: "))
print("You are " + Age + " years old")