def eh_bissexto(ano):
    return ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)

# Entrada do ano pelo usuário
ano = int(input("Digite o ano: "))

# Verifica se o ano é bissexto e exibe o resultado
if eh_bissexto(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
