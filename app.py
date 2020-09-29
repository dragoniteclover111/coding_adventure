name = input("What is your name?")
print("Hello " + name)
age = input("What is your age?")
age_in_days = int(age) * 365
print("You are " + age + " years old. You’ve lived for more than " + str(age_in_days) + " days!")


print("Title of program: Somebot to talk to")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("tomorrow will be a better day")
      counter += 1
    if each_word == "stressed":
      feelings_list.append("stressed")
      encouragement_list.append("that you can overcome this obstacle! 加油!!")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling")
      counter += 1
    if each_word == "useless":
      feelings_list.append("useless")
    if each_word == "depressed":
      feelings_list.append("depressed")
      encouragement_list.append("every cloud has a silver lining")
      counter += 1
 
      encouragement_list.append("Everyone has a purpose in life")
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you are stronger than you think")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"
  print()
  print(output)
  print()
  
  
  
  
Clover's code

print("Title of program: Somebot to talk to")
print()
name = input("What is your name?")
print("Hello " + name)
age = input("What is your age?")
age_in_days = int(age) * 365
print("You are " + age + " years old. You’ve lived for more than " + str(age_in_days) + " days!")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("tomorrow will be a better day")
      counter += 1
    if each_word == "stressed":
      feelings_list.append("stressed")
      encouragement_list.append("that you can overcome this obstacle! 加油!!")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling")
      counter -= 1
    if each_word == "useless":
      feelings_list.append("useless")
      encouragement_list.append("Everyone has a purpose in life")
      counter += 1
    if each_word == "depressed":
      feelings_list.append("depressed")
      encouragement_list.append("every cloud has a silver lining")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you are stronger than you think")
      counter += 1
    if each_word == "ok":
      feelings_list.append("ok")
      encouragement_list.append("that that's great and keep up this way")
      counter -= 1
    if each_word == "good":
      feelings_list.append("good")
      encouragement_list.append("to continue being the way you are")
      counter -= 1
    if each_word == "lonely":
      feelings_list.append("lonely")
      encouragement_list.append("you are never alone and there would always be someone alongside you on this journey")
      counter += 1
    if each_word == "hurt":
      feelings_list.append("hurt")
      encouragement_list.append("you can always share your pains with your close ones")
      counter += 1
    if each_word == "afraid":
      feelings_list.append("afraid")
      encouragement_list.append("you will overcome any challenges you face as long as you stay strong")
      counter += 1
    if each_word == "worried":
      feelings_list.append("worried")
      encouragement_list.append("there's nothing to be worried about")
      counter += 1
    
      
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"
  print()
  print(output)
  print()
