#full_name = input("Enter your full names: ")
#length = len(full_name)
#first,second = full_name[0],full_name[-1]
#print(f"Your name is {full_name.upper()}. The length of your name is {length}. first and last characters are: {first,second}")


#sentence = input("Enter a sentence: ").strip()
#words = sentence.split()
#words = sentence.replace(" ","___")
#length = len(words)
#print(f"Your sentence is: {sentence.upper()}. The sentence is now {words} and the length is {length}")

first = input("Enter your first name: ").strip().lower()
last = input("Enter your last name: ").strip().lower()
username = first[:4] + last[-1] + "1234"
print(f"Your username is {username}")
