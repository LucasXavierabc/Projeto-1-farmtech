plantacoes = []


def calcular_area(cultura):
    if cultura == "laranja":
        raio = float(input("Digite o raio do pomar (m): "))
        area = round(3.14 * (raio ** 2), 3)  # Área do círculo
        print(f"Área = {area} m²")
        return area
    elif cultura == "milho":
        largura = float(input("Digite a largura do terreno (m): "))
        comprimento = float(input("Digite o comprimento do terreno (m): "))
        area = largura * comprimento  # Área do retângulo
        print(f"Área = {area} m²")
        return area
    else:
        print("Cultura inválida!")
        return 0


def cadastrar_plantacao():
    nome = input("Digite o nome da plantação: ")
    while True:
        cultura = input("Digite a cultura (laranja/milho): ").lower()
        if cultura == "laranja" or cultura == "milho":
            area = calcular_area(cultura)
            break
        else:
            print("\n ! Cultura inválida ! \n")
    sementes_mudas, agua, nitrogenio, fosforo, potassio = '', '', '', '', ''
    plantacoes.append({"nome": nome, "cultura": cultura, "area": area,
                       "sementes/mudas": sementes_mudas, "agua": agua,
                       "nitrogenio": nitrogenio, "fosforo": fosforo, "potassio": potassio})
    print("Plantação cadastrada com sucesso!")


def exibir_plantacoes():
    if not plantacoes:
        print("Nenhuma plantação cadastrada.")
    else:
        print("\n ---> Plantações: ")
        for i, plantacao in enumerate(plantacoes):
            print(
                f"{i} - Nome: {plantacao['nome'].capitalize()} || Cultura: {plantacao['cultura'].capitalize()} || Área: {plantacao['area']} m²")


def atualizar_area():
    exibir_plantacoes()
    indice = int(input("Digite o índice da plantação que deseja atualizar: "))
    if 0 <= indice < len(plantacoes):
        nova_area = calcular_area(plantacoes[indice]["cultura"])
        plantacoes[indice]["area"] = nova_area
        print("Área atualizada com sucesso!")
    else:
        print("Índice inválido!")


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


def calcular_insumos():
    exibir_plantacoes()
    indice = int(input("Digite o índice da plantação para calcular insumos: "))
    if 0 <= indice < len(plantacoes):
        cultura = plantacoes[indice]["cultura"]
        area = plantacoes[indice]["area"]
        ########## Dados coletados do site da EMBRAPA ##########
        if cultura == "milho":
            sementes = 2.3 * area  # Média de 2.3g por m²
            plantacoes[indice]["sementes/mudas"] = sementes

            agua = 5 * area  # Aproximadamente 5 litros por m²
            plantacoes[indice]["agua"] = agua

            nitrogenio = 10 * area  # Média de 10g de N por m²
            plantacoes[indice]["nitrogenio"] = nitrogenio

            fosforo = 5 * area  # Média de 5g de P por m²
            plantacoes[indice]["fosforo"] = fosforo

            potassio = 8 * area  # Média de 8g de K por m²
            plantacoes[indice]["potassio"] = potassio

        elif cultura == "laranja":
            mudas = round(area / 30, 3)  # Média de uma muda a cada 30m²
            plantacoes[indice]["sementes/mudas"] = mudas

            agua = 15 * area  # Aproximadamente 15 litros por m²
            plantacoes[indice]["agua"] = agua

            nitrogenio = 8 * area  # Média de 8g de N por m²
            plantacoes[indice]["nitrogenio"] = nitrogenio

            fosforo = 4 * area  # Média de 4g de P por m²
            plantacoes[indice]["fosforo"] = fosforo

            potassio = 6 * area  # Média de 6g de K por m²
            plantacoes[indice]["potassio"] = potassio

        else:
            print("Cultura inválida!")
            return
        print(f"\nInsumos necessários para {cultura.capitalize()} em {area} m²:")
        if cultura == "milho":
            print(f"Sementes: {converter_peso(sementes)}")
        else:
            print(f"Mudas: {converter_mudas(mudas)}")
        print(f"Água: {converter_peso(agua)}")
        print(f"Nitrogênio (N): {converter_peso(nitrogenio)}")
        print(f"Fósforo (P): {converter_peso(fosforo)}")
        print(f"Potássio (K): {converter_peso(potassio)}")
    else:
        print("Índice inválido!")


def main():
    while True:
        print("\n==== Menu de Opções ====")
        print("1 - Cadastrar plantação")
        print("2 - Exibir plantações")
        print("3 - Atualizar área de plantação")
        print("4 - Calcular insumos")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_plantacao()
        elif opcao == "2":
            exibir_plantacoes()
        elif opcao == "3":
            atualizar_area()
        elif opcao == "4":
            calcular_insumos()
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")


########## Plantações exemplo para o programa em R ##########
plantacoes.append({'nome': 'Plantação laranja 1', 'cultura': 'laranja', 'area': 47505.06, 'sementes/mudas': 1583.502,
                   'agua': 712575.8999999999, 'nitrogenio': 380040.48, 'fosforo': 190020.24, 'potassio': 285030.36})
plantacoes.append({'nome': 'Plantação laranja 2', 'cultura': 'laranja', 'area': 652919.04, 'sementes/mudas': 21763.968,
                   'agua': 9793785.600000001, 'nitrogenio': 5223352.32, 'fosforo': 2611676.16, 'potassio': 3917514.24})
plantacoes.append({'nome': 'Plantação laranja 3', 'cultura': 'laranja', 'area': 1954715.94, 'sementes/mudas': 65157.198,
                   'agua': 29320739.099999998, 'nitrogenio': 15637727.52, 'fosforo': 7818863.76,
                   'potassio': 11728295.64})
plantacoes.append(
    {'nome': 'Plantação milho 1', 'cultura': 'milho', 'area': 15129.0, 'sementes/mudas': 34796.7, 'agua': 75645.0,
     'nitrogenio': 151290.0, 'fosforo': 75645.0, 'potassio': 121032.0})
plantacoes.append(
    {'nome': 'Plantação milho 2', 'cultura': 'milho', 'area': 207936.0, 'sementes/mudas': 478252.8, 'agua': 1039680.0,
     'nitrogenio': 2079360.0, 'fosforo': 1039680.0, 'potassio': 1663488.0})
plantacoes.append(
    {'nome': 'Plantação milho 3', 'cultura': 'milho', 'area': 622521.0, 'sementes/mudas': 1431798.2999999998,
     'agua': 3112605.0, 'nitrogenio': 6225210.0, 'fosforo': 3112605.0, 'potassio': 4980168.0})

main()