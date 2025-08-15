# 2.Faça um algoritmo e um fluxograma que receba as notas de um aluno e verifique se ele passou ou não, 
# são 3 avaliações e a aprovação por média é 6, caso ele não tenha sido aprovado ele deve fazer a final, 
# a média final é a média aritimética entre a média e a final, por fim a aprovação por final também é 6.

nota1 = float(input('Informe a 1º nota: '))
nota2 = float(input('Informe a 2º nota: '))
nota3 = float(input('Informe a 3º nota: '))

media = (nota1 + nota2 + nota3) / 3
print(f'Média inicial do aluno é: {media:.2f}')

if media >= 6:
    print(f'\nAluno aprovado por média.')
else:
    print(f'\nAluno reprovado por média. Deverá realizar a final.')    

    notaFinal = float(input(f'Informe a nota do aluno na final: '))

    mediaFinal = (media + notaFinal) / 2
    print(f'Média final do aluno: {mediaFinal:.2f}')
    
    if mediaFinal >= 6:
        print(f'Aluno aprovado após a final.')
    else:
        print(f'Aluno reprovado após a final.')    