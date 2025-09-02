def converter(valor, origem, destino):
    # Converte a unidade de origem para metros
    if origem == "mm":
        valor_m = valor / 1000
    elif origem == "cm":
        valor_m = valor / 100
    elif origem == "m":
        valor_m = valor
    elif origem == "km":
        valor_m = valor * 1000
    else:
        print("Unidade de origem inválida")
        exit()
    
    # Converte de metros para a unidade de destino
    if destino == "mm":
        return valor_m * 1000
    elif destino == "cm":
        return valor_m * 100
    elif destino == "m":
        return valor_m
    elif destino == "km":
        return valor_m / 1000
    else:
        print("Unidade de destino inválida")
        exit()

# Solicita ao usuário o valor e a unidade de origem (ex: 1500 m)
entrada = input("Digite o valor e a unidade de medida: ")
# Solicita ao usuário a unidade de destino
destino = input("Digite a unidade de medida da conversão: ").lower()

# Separa o valor e a unidade de origem
partes = entrada.split()
valor = float(partes[0])
origem = partes[1].lower()

# Exibe o resultado da conversão
print(valor, origem, "para", destino, "=", converter(valor, origem, destino), destino)