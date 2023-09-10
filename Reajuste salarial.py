print('=•'*5,'ORGANIZAÇÕES TABAJARA','•='*5,'\n')
nome = str(input('Informe o nome do colaborador: '))
salario = float(input('Informe o salário do colaborador: R$'))
print('=-'*20)
print('''Nome do colaborador: {}
Antigo salário: R${:.2f}'''.format(nome, salario, ))
if salario <= 280:
    aumento = salario * 20/100
    novoSalario = salario + aumento
    print('Percentual de aumento: 20%')
elif 280 < salario <= 700:
    aumento = salario * 15/100
    novoSalario = salario + aumento 
    print('Percentual de aumento: 15%')
elif 700 > salario <= 1500:
    aumento = salario * 10/100
    novoSalario = salario + aumento
    print('Percentual de aumento: 10%')
else:
    aumento = salario * 5/100
    novoSalario = salario + aumento
    print('Peecentual de aumento: 5%')
print('Valor aumentado: R${:.2f}'.format(aumento))
print('Novo salário: R${:.2f}'.format(novoSalario))
print('=-'*20)
