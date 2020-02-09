def china():
  print("Food? Religion? Landmark? ")
  b = str(input("What do you want to learn about?"))
  if b==("Food"):
    print("Sichuan food - ")
    print("Famous for super spicy food, its crazy.")
    print("There are resteraunts where you have to sign contracts if their spicy meal results into death, it's not their responsibility")
  if b==("Religion"):
    print("In China, there aren't that many people who are religious")
    print("Only 26.45% of the people are religious")
  if b==("Landmarks"):
    print("Great wall of China")
    print("Did you know that The Great Wall of China's size 21,196 km (13,171 mi) long")
def japan():
  print("Food? Religion? Landmark? ")
  d = str(input("What do you want to learn about?" ))
  if d == ("Food"):
    print("Yakiniku-")
    print("yakiniku is a japanese food where its like an indoor barbeque and cook your own meat")
    print("Yakiniku can vary from local street food to fancy meals")
  if d==("Religion"):
    print("In Japan 52% aren’t religious and 35% are buddist, 11% are shinto and 10% are Christian.")
  if d==("Landmarks"):
    print("Tokyo Tower")
    print("Tokyo tower is 333m tall")
    print("It was used as a tower to get radio satelite but now it is just a decoration")
def singapore():
  print("Food? Religion? Landmark?")
  e=str(input("What do you want to learn about?"))
  if e==("Food"):
    print("Hainan Chicken rice - ")
    print("Hainan Chicken is a very famous Singaporian food.")
    print("You eat Chicken with rice by dipping it with a thick soy sauce")
  if e==("Religion"):
    print("Singapore is home to 10 religions, with Buddhism/Taoism, Islam,")
    print("Hinduism and Christianity as its principal religions. Sikhism, Judaism, Zoroastrianism,") 
    print ("Baha'I, Jainism and the non-religious form the minority cluster.")
  if e==("Landmarks"):
    print("The Marina Bay Sands - ")
    print("It is a hotel with three towers and on top of that tower is a long boat like structure that has the rooftop pool")
def south_korea():
    print("Food? Religion? Landmarks?")
    f=str(input("Choose an option "))
    if f==("Food"):
      print("Tteokbokki -")
      print("Spicy korean street food. Also served with odeng soup.")
    if f==("Religion"):
      print("43% of the people are buddist 34.5% of the people are protestants and 20% of the people are Roman Catholics.")
    if f==("Landmarks"):
      print("Bukchon Hanok Village - ")
      print("is a Korean traditional village in Seoul with a long history")
name=input("Hello kiddo, whats your name? ")
print("okay "+ name)
answer=input("Do you want to learn about countries in Asia? ")
if answer == ("yes"):
  print("cool beans")
  print("Your choices are: \n 1.China \n 2.Japan \n 3.Singapore \n 4.South Korea")
else:
  print("Too bad you're going to be learning about it anyways")
  print("Your choices are: \n 1.China \n 2.Japan \n 3.Singapore \n 4.South Korea")
a = str(input("Choose one option ")) 
if a==("China"):
    china() 

  #add countries
if a==("Japan"):
    japan()
if a==("Singapore"):
    singapore()
if a==("South Korea"):
    south_korea()
 

  #add whatever the stuff you need to add
