#Desafio 2

def calcular_rankeadas(vitorias, derrotas):
    return vitorias - derrotas

v = int(input("vitorias do jogador: "))
d = int(input("derrotas do jogador: "))

resultado = calcular_rankeadas(v, d)
#print(resultado)

if resultado < 10:
    nivel = "Ferro"
elif resultado > 11 and  resultado < 20:
    nivel = "Bronze"
elif resultado > 21 and resultado < 50:
    nivel = "Prata"
elif resultado > 51 and resultado < 80:
    nivel = "Ouro"
elif resultado > 81 and resultado < 90:
    nivel = "Diamante"
elif resultado > 91 and resultado < 100:
    nivel = "Lendário"
else:
    resultado >= 101
    nivel = "Imortal"

print(f"O Herói tem de saldo de **{resultado}** está no nível de **{nivel}**")
