def soma_n(numero: int) -> int:
    if numero == 1:
        return 1
    else: 
        return numero + soma_n(numero - 1)
    
print(soma_n(3))
    