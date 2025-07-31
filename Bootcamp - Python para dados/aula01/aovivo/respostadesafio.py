'''Instruções:
O programa deve começar solicitando ao usuário que insira seu nome.
Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".'''

nome = input("Digite o seu nome:")
salario = float (input("Digite o seu salário:"))
bonus = float(input("Digite o percentual do seu bônus:"))
CONSTANTE_BONUS = 1000
KPI_BONUS = CONSTANTE_BONUS + salario * bonus
print (f"Olá {nome}, o seu valor KPI bônus foi de R$ {KPI_BONUS:.2f}")