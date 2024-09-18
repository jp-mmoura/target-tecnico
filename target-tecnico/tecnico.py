#1 
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print(f"O valor de SOMA é: {SOMA}")

#2
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n  

numero = int(input("Informe um número: "))

if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

#3
import json

dados_faturamento = '''
{
    "faturamento_diario": [1000, 2000, 0, 1500, 2300, 0, 1800, 1300, 2500, 0]
}
'''


faturamento = json.loads(dados_faturamento)["faturamento_diario"]


faturamento_validos = [valor for valor in faturamento if valor > 0]

menor_faturamento = min(faturamento_validos)
maior_faturamento = max(faturamento_validos)
media_faturamento = sum(faturamento_validos) / len(faturamento_validos)


dias_acima_da_media = sum(1 for valor in faturamento_validos if valor > media_faturamento)

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

#4
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_estados.values())

for estado, valor in faturamento_estados.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")


#5
def inverter_string(s):
    invertida = ''
    for char in s:
        invertida = char + invertida
    return invertida

string = input("Informe uma string: ")
print(f"String invertida: {inverter_string(string)}")
