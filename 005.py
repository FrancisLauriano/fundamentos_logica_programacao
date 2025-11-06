def fibonacci(numero: int) -> int:
    if numero <= 1:
        return numero
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(8))
