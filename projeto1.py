from time import sleep
plantacoes = []





######################### Outras funções 

def limpar_tela():
    print("\n"*100)

def converter_peso(gramas):
    if gramas >= 1_000_000:
        return f"{gramas / 1_000_000:.2f} toneladas"
    elif gramas >= 1_000:
        return f"{gramas / 1_000:.2f} kg"
    else:
        return f"{gramas:.2f} g"


def converter_mudas(mudas):
    if mudas >= 1_000:
        return f"{mudas / 1_000:.2f} milhares"
    elif mudas >= 100:
        return f"{mudas / 100:.2f} centenas"
    else:
        return f"{mudas:.2f} unidades"





######################### 1 - cadastrar uma plantação 

def cadastrar_plantacao():
    print("Digite o nome da plantação ")
    nome = input("--> ")
    while True:
        print("Digite a cultura (laranja/milho) ")
        cultura = input("--> ").lower()
        if cultura == "laranja" or cultura == "milho":
            area = calcular_area()
            sementes_mudas, agua, nitrogenio, fosforo, potassio = calcular_insumos(cultura, area)
            plantacoes.append({"nome": nome, "cultura": cultura, "area":area,
                               "sementes_mudas":sementes_mudas, "agua":agua,
                               "nitrogenio":nitrogenio, "fosforo":fosforo,
                               "potassio":potassio})
            sleep(1)
            print("Plantação cadastrada com sucesso")
            break
        else:
            print("! Cultura inválida !\n")

def calcular_area():
    print("Digite a largura do terreno (m) ")
    largura = float(input("--> "))
    print("Digite o comprimento do terreno (m) ")
    comprimento = float(input("--> "))
    area = largura * comprimento 
    print(f"Área = {area} m²")
    return area

def calcular_insumos(cultura, area):
    match cultura:
        case "laranja":
            sementes_mudas = round(area / 30, 3)  # Média de uma muda a cada 30m²
            agua = 15 * area  # Aproximadamente 15 litros por m²
            nitrogenio = 8 * area  # Média de 8g de N por m²
            fosforo = 4 * area  # Média de 4g de P por m²
            potassio = 6 * area  # Média de 6g de K por m²
        case "milho":
            sementes_mudas = 2.3 * area  # Média de 2.3g por m²
            agua = 5 * area  # Aproximadamente 5 litros por m²
            nitrogenio = 10 * area  # Média de 10g de N por m²
            fosforo = 5 * area  # Média de 5g de P por m²
            potassio = 8 * area  # Média de 8g de K por m²
    return sementes_mudas, int(agua), nitrogenio, fosforo, potassio





######################### 2 - exibir_plantações 

def exibir_plantacoes():
    if not plantacoes:
        print("Nenhuma plantação cadastrada.")
    else:
        print("\n ---> Plantações: ")
        for i, plantacao in enumerate(plantacoes):
            print(
                f"Índice {i} - Nome: {plantacao['nome'].capitalize()} || Cultura: {plantacao['cultura'].capitalize()} || Área: {plantacao['area']} m²")



######################### 3 - Atualizar dados de plantação 

def atualizar_dados():
    print("Digite o índice da plantação que deseja atualizar ")
    exibir_plantacoes()

    while True:
        indice = int(input("--> "))
        if 0 <= indice < len(plantacoes):
            print("Qual dado será atualizado? ")
            print(" 0 - Nome"
                "\n 1 - Area"
                "\n 2 - Cultura")

            while True:
                resposta = int(input("--> "))
                if resposta > 2 or resposta < 0:
                    print("! Opção inválida ! \n")
                else:
                    break

            match resposta:
                case 0:
                    print("\n Novo nome ")
                    plantacoes[indice]["nome"] = input("--> ")
                    print("Nome atualizado com sucesso")
                case 1:
                    plantacoes[indice]["area"] = calcular_area()
                    plantacoes[indice]["sementes_mudas"], plantacoes[indice]["agua"], plantacoes[indice]["nitrogenio"], plantacoes[indice]["fosforo"], plantacoes[indice]["potassio"] = calcular_insumos(plantacoes[indice]["cultura"], plantacoes[indice]["area"])
                    print("Área atualizada com sucesso")
                case 2:
                    while True:
                        print("\n Nova cultura (laranja/milho) ")
                        plantacoes[indice]["cultura"] = input("--> ")
                        if plantacoes[indice]["cultura"] != "laranja" and plantacoes[indice]["cultura"] != "milho":
                            print("! Cultura inválida !\n")
                        else:
                            plantacoes[indice]["sementes_mudas"], plantacoes[indice]["agua"], plantacoes[indice]["nitrogenio"], plantacoes[indice]["fosforo"], plantacoes[indice]["potassio"] = calcular_insumos(plantacoes[indice]["cultura"], plantacoes[indice]["area"])
                            break
                        print("Cultura atualizada com sucesso")
            break

        else:
            print("! Opção inválida !\n")





######################### 4 - Exibir insumos
def exibir_insumos():
    print("Digite o índice da plantação para calcular os insumos ")
    exibir_plantacoes()
    while True:
        indice = int(input("--> "))
        if 0 <= indice < len(plantacoes):
            print(f"Insumos necessários para '{plantacoes[indice]['nome']}': ")
            if plantacoes[indice]["cultura"] == "laranja":
                print(f"Mudas:          {converter_mudas(plantacoes[indice]['sementes_mudas'])}")
            else:
                print(f"Sementes:       {converter_peso(plantacoes[indice]['sementes_mudas'])}")
            print(f"Agua:           {plantacoes[indice]['agua']:,} L".replace(",", "."),
                f"\nNitrogênio (N): {converter_peso(plantacoes[indice]['nitrogenio'])}",
                f"\nFósforo    (P): {converter_peso(plantacoes[indice]['fosforo'])}",
                f"\nPotássio   (K): {converter_peso(plantacoes[indice]['potassio'])}")
            break
        else:
            print("! indice inválido ! \n")




######################### apagar uma plantação
def apagar_plantacao():
    print("Digite o índice da plantação a ser apagada ")
    exibir_plantacoes()
    while True:
        indice = int(input("--> "))
        if 0 <= indice < len(plantacoes):
            del(plantacoes[indice])
            print("Plantação apagada com sucesso")
            break
        else:
            print("! índice inválido ! \n")




######################### menu

def main():
    while True:
        sleep(1)
        confirmação = input("\nPressione [ENTER] para continuar")
        limpar_tela()
        sleep(1)
        print("\n====== Menu de Opções ======")
        print("   1 - Cadastrar plantação")
        print("   2 - Exibir plantações")
        print("   3 - Exibir insumos")
        print("   4 - Atualizar dados")
        print("   5 - Apagar dados")
        print("   0 - Sair")
        print("Escolha uma opção ")

        opcao = input("--> ")

        if opcao == "1":
            cadastrar_plantacao()
        elif opcao == "2":
            exibir_plantacoes()
        elif opcao == "3":
            exibir_insumos()
        elif opcao == "4":
            atualizar_dados()
        elif opcao == "5":
            apagar_plantacao()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("! Opção inválida !\n")





plantacoes.append({'nome': 'Plantação exemplo 1', 'cultura': 'laranja', 'area': 10_000.0, 'sementes_mudas': 333.333, 'agua': 150_000, 'nitrogenio': 80_000.0, 'fosforo': 40_000.0, 'potassio': 60_000.0})
plantacoes.append({'nome': 'Plantação exemplo 2', 'cultura': 'laranja', 'area': 11_000.0, 'sementes_mudas': 366.667, 'agua': 165_000, 'nitrogenio': 88_000.0, 'fosforo': 44_000.0, 'potassio': 66_000.0})
plantacoes.append({'nome': 'Plantação exemplo 3', 'cultura': 'laranja', 'area': 12_100.0, 'sementes_mudas': 403.333, 'agua': 181_500, 'nitrogenio': 96_800.0, 'fosforo': 48_400.0, 'potassio': 72_600.0})
plantacoes.append({'nome': 'Plantação exemplo 4', 'cultura': 'laranja', 'area': 10_000.0, 'sementes_mudas': 333.333, 'agua': 150_000, 'nitrogenio': 80_000.0, 'fosforo': 40_000.0, 'potassio': 60_000.0})
plantacoes.append({'nome': 'Plantação exemplo 5', 'cultura': 'laranja', 'area': 14_400.0, 'sementes_mudas': 480.0, 'agua': 216_000, 'nitrogenio': 115_200.0, 'fosforo': 57_600.0, 'potassio': 86_400.0})
plantacoes.append({'nome': 'Plantação exemplo 6', 'cultura': 'milho', 'area': 10_000.0, 'sementes_mudas': 23_000.0, 'agua': 50_000, 'nitrogenio': 100_000.0, 'fosforo': 50_000.0, 'potassio': 80_000.0})
plantacoes.append({'nome': 'Plantação exemplo 7', 'cultura': 'milho', 'area': 11_000.0, 'sementes_mudas': 25_300.0, 'agua': 55_000, 'nitrogenio': 110_000.0, 'fosforo': 55_000.0, 'potassio': 88_000.0})
plantacoes.append({'nome': 'Plantação exemplo 8', 'cultura': 'milho', 'area': 12_100.0, 'sementes_mudas': 27_830.0, 'agua': 60_500, 'nitrogenio': 121_000.0, 'fosforo': 60_500.0, 'potassio': 96_800.0})
plantacoes.append({'nome': 'Plantação exemplo 9', 'cultura': 'milho', 'area': 10_000.0, 'sementes_mudas': 23_000.0, 'agua': 50_000, 'nitrogenio': 100_000.0, 'fosforo': 50_000.0, 'potassio': 80_000.0})
plantacoes.append({'nome': 'Plantação exemplo 10', 'cultura': 'milho', 'area': 14_400.0, 'sementes_mudas': 33_120.0, 'agua': 72_000, 'nitrogenio': 144_000.0, 'fosforo': 72_000.0, 'potassio': 115_200.0})





main()