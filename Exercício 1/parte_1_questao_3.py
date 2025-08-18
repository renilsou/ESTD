salario_hora = float(input("Digite o quanto você ganha por hora: "))
horas_trabalhadas = int(input("Digite a quantidade de horas que você trabalha por mês: "))

salario_mensal = salario_hora*horas_trabalhadas

print(f"Seu salário mensal é de: R$ {salario_mensal:.2f}")