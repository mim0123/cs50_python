question = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
if question == "42":
    print("Yes")
elif question.strip().lower() == "forty-two":
    print("Yes")
elif question.strip().lower() == "forty two":
    print("Yes")
else: 
    print("No")