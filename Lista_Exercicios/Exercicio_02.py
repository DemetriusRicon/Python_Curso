#Write Python code to iterate through the first 10 numbers and, in each iteration,
#print the sum of the current and previous number.

numero_anterior = 0 

for index in range(1,10):
    resultado = index + numero_anterior
    (print(f'Numero atual é {index} e somado ao numero anterior é igual a {resultado}'))
    numero_anterior = index