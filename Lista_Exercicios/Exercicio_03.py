#Write a Python code to accept a string from the user and display characters present at an even index number.

#For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.


palavra = str(input("Digite a palavra "))

for i in range(0, len(palavra), 2):
    print(palavra[i])