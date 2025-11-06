def divisao_inteira(num_1: int, num_2: int) -> int:
    if num_1 < num_2:
        return 0
    else:
        return 1 + divisao_inteira(num_1 - num_2, num_2)

print(divisao_inteira(21, 2))