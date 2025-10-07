# Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.

# Entrada
# A entrada contém um valor inteiro N (N < 10000).


N = int(input('Digite número: '))

i = 1

while i < 10000:
    if i % N == 2:
        print(i)
    
    i += 1

