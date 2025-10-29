import exe_001 as exer

numero_e_par = int(input('Digite um valor: '))
paridade = exer.paridade(numero_e_par)
print(f'O número {numero_e_par} é {paridade}')


numero_e_perfeito = int(input('Informe um valor: '))
num_perfeito = exer.num_perfeito(numero_e_perfeito)
print(f'Número {numero_e_perfeito}: {num_perfeito}')

numero_primo = int(input('Informe um número inteiro: '))
num_primo = exer.num_primo(numero_primo)
print(f'Número {numero_primo}: {num_primo}')
