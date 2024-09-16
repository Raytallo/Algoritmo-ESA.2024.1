def obter_vazao_entrada():
    while True:
        try:
            vazao = float(input("Digite a vazão de entrada (em m3/h): "))
            if vazao <= 0:
                print("A vazão de entrada deve ser um valor positivo.")
            else:
                return vazao
        except ValueError:
            print("Por favor, digite um valor numérico para a vazão de entrada.")

# Exemplo de uso:
vazao_entrada = obter_vazao_entrada()
print("Vazão de entrada:", vazao_entrada, "m3/h")
