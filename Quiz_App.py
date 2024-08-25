import time

print("Welcome to Quiz_App")
name = input("What's your name and surname? ")
print(name)
print("Information!!")
print("The first letter of your answers should be capitalized.")
print("QUIZ APP IS STARTING!!!")

# 3 saniyelik geri sayım
for i in range(3, 0, -1):
    print(f"Starting in {i}...")
    time.sleep(1)

print("Let's go!")

answer = input("I'm not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I? ")
if answer == "Fire":
    print("CORRECT!!!!")
else:
    print(f"The answer is 'Fire', not {answer!r}")

answer1 = input("What goes up and down but stays in the same place? ")
if answer1 == "Stair":
    print("CORRECT!!!!")
else:
    print(f"The answer is 'Stair', not {answer1!r}")

answer2 = input("In which year did the Titanic sink? ")
if answer2 == "1912":
    print("CORRECT!!!!")
else:
    print(f"The answer is '1912', not {answer2!r}")

answer3 = input("Who was the first president of the United States? ")
if answer3 == "George Washington":
    print("CORRECT!!!!")
else:
    print(f"The answer is 'George Washington', not {answer3!r}")

answer4 = input("Who was the founder of the Republic of Turkey? ")
if answer4 == "Mustafa Kemal Atatürk":
    print("CORRECT!!!!")
else:
    print(f"The answer is 'Mustafa Kemal Atatürk', not {answer4!r}")
