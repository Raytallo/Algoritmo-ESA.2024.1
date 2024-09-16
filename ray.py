def inserir_dados_industria():
    """Insere novos dados de uma indústria e retorna a eficiência calculada."""
    industria = input("Qual o nome da indústria? ")
    DBOi = float(input("Qual valor de DBO inicial? "))
    DBOf = float(input("Qual valor de DBO final? "))
    eficiencia = ((DBOi - DBOf) / DBOi) * 100
    return industria, eficiencia


def calcular_eficiencia(eficiencia):
    """Exibe se a eficiência está adequada ou inadequada."""
    status = "adequada" if eficiencia >= 60 else "inadequada"
    print(f"Eficiência {status}")


def verificar_industria(dados_industrias):
    """Verifica a eficiência de uma indústria existente."""
    industria = input("Qual o nome da indústria? ")
    for dados in dados_industrias:
        if dados["industria"] == industria:
            print(f"Eficiência da indústria {industria}: {dados['eficiencia']:.2f}%")
            return True
    print("Indústria não encontrada.")
    return False


def corrigir_dados(dados_industrias):
    """Corrige os dados de uma indústria existente."""
    industria = input("Qual o nome da indústria que deseja corrigir? ")
    for dados in dados_industrias:
        if dados["industria"] == industria:
            DBOi_corrigido = float(input(f"Novo valor de DBO inicial para {industria}: "))
            DBOf_corrigido = float(input(f"Novo valor de DBO final para {industria}: "))
            eficiencia_corrigida = ((DBOi_corrigido - DBOf_corrigido) / DBOi_corrigido) * 100
            dados["eficiencia"] = eficiencia_corrigida
            print(f"Dados corrigidos para a indústria {industria}.")
            calcular_eficiencia(eficiencia_corrigida)
            return True
    print("Indústria não encontrada.")
    return False


def verificar_parametros_agua():
    """Verifica os parâmetros de qualidade da água de acordo com a CONAMA 357/2005."""
    coliformes = float(input("Digite o valor de coliformes totais (NMP/100 mL): "))
    turbidez = float(input("Digite o valor de turbidez (NTU): "))


    # Limites definidos pela CONAMA 357/2005
    limites = {
        'coliformes': 0,  # Coliformes totais recomendados (0 NMP/100 mL para água potável)
        'turbidez': 5    # Turbidez recomendada (NTU)
    }


    erro = False
    if coliformes > limites['coliformes']:
        print(f"Erro: Coliformes totais acima do limite recomendado ({limites['coliformes']} NMP/100 mL)")
        erro = True
    if turbidez > limites['turbidez']:
        print(f"Erro: Turbidez acima do limite recomendado ({limites['turbidez']} NTU)")
        erro = True


    if not erro:
        print("Todos os parâmetros de qualidade da água estão dentro dos limites recomendados.")


def realizar_calculos():
    """Realiza os cálculos relacionados a esgoto e contribuição pluviométrica."""
    volumecolet = int(input("Digite o valor do esgoto coletado em metros cúbicos: "))
    volumeaguacons = int(input("Digite o valor da água consumida em metros cúbicos: "))
    volumeaguatrat = int(input("Digite o valor da água tratada em metros cúbicos: "))
   
    # Check if the denominator is zero and handle it
    if volumeaguacons - volumeaguatrat == 0:
        print("Erro: A diferença entre água consumida e água tratada é zero. Não é possível calcular o controle.")
    else:
        calculocontrol = volumecolet / (volumeaguacons - volumeaguatrat)
        print(f"Controle de cálculo: {calculocontrol:.2f} m³")


    chuv = float(input("Digite a quantidade no período chuvoso em (mm): "))
    seco = float(input("Digite a quantidade no período seco em (mm): "))
    km = float(input("Digite a extensão em quilômetros da rede coletora: "))
    qcp = chuv - seco
    porcentagem = (qcp / seco) * 100
    taxa = (qcp / km) * 100
    print(f"A contribuição pluviométrica do período chuvoso é: {qcp:.2f} mm")
    print(f"O percentual em relação ao tempo seco é: {porcentagem:.2f}%")
    print(f"A taxa de contribuição é: {taxa:.2f}%")


    p = float(input("Digite a quantidade de precipitação em (mm): "))
    seco = 50
    km = float(input("Digite a extensão em quilômetros da rede coletora: "))
    qcp = p - seco
    taxa = (qcp / km) * 100
    print(f"A contribuição pluviométrica nesse período é: {qcp:.2f} mm")
    print(f"A taxa de contribuição é: {taxa:.2f}%")


    if p >= 200 or taxa >= 30.00:
        print("CUIDADO! SUA ETE CORRE RISCO DE TRANSBORDAR!!!")
    else:
        print("Sua ETE está dentro do limite aceitável")


def main():
    """Função principal que gerencia o fluxo do programa."""
    print('Seja bem-vindo(a) ao Fiscal Append! Insira as informações necessárias.')
    print("Olá, fiscal")


    dados_industrias = []


    while True:
        dados_novos = input("Você quer inserir novos dados? (sim/não/Sair do programa): ").strip().lower()


        if dados_novos == "sim":
            industria, eficiencia = inserir_dados_industria()
            dados_industrias.append({"industria": industria, "eficiencia": eficiencia})
            calcular_eficiencia(eficiencia)
       
        elif dados_novos == "não":
            while True:
                opcao = input("Você quer verificar dados antigos, corrigir dados ou encerrar o programa? (verificar/corrigir/encerrar): ").strip().lower()
                if opcao == "verificar":
                    if verificar_industria(dados_industrias):
                        break
                elif opcao == "corrigir":
                    if corrigir_dados(dados_industrias):
                        break
                elif opcao == "encerrar":
                    print("Encerrando o programa... Obrigado por usar o Fiscal Append!")
                    return
                else:
                    print("Opção inválida. Por favor, insira 'verificar', 'corrigir' ou 'encerrar'.")
       
        elif dados_novos == "sair do programa":
            print("Saindo do programa... Obrigado por usar o Fiscal Append!")
            break
       
        else:
            print("Opção inválida. Por favor, insira 'sim', 'não' ou 'Sair do programa'.")


        realizar_calculos()
        verificar_parametros_agua()


        # Perguntar novamente após a realização dos cálculos
        while True:
            dados_novos = input("Você quer inserir novos dados, verificar dados antigos ou encerrar o programa? (inserir/verificar/encerrar): ").strip().lower()
            if dados_novos == "inserir":
                break
            elif dados_novos == "verificar":
                while True:
                    if verificar_industria(dados_industrias):
                        break
                break
            elif dados_novos == "encerrar":
                print("Encerrando o programa... Obrigado por usar o Fiscal Append!")
                return
            else:
                print("Opção inválida. Por favor, insira 'inserir', 'verificar' ou 'encerrar'.")


# Executar a função principal
if __name__ == "__main__":
    main()
