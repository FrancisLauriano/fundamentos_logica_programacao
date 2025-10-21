n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end = ' ')
#     print()

# OU

for i in range(1, n + 1):
    resposta = ''
    for j in range(1, i + 1):
        resposta = resposta + str(j) + ' '

    print(resposta)

# # OU
# resposta = ''
# for i  in range(1, n + 1):
