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
    cultura = input("Digite a cultura (laranja/milho): ").lower()
    area = calcular_area(cultura)

    plantacoes.append({"cultura": cultura, "area": area})
    print("Plantação cadastrada com sucesso!")


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
        if cultura == "milho":
            sementes = 2.3 * area  # Média de 2.3g por m²
            agua = 5 * area  # Aproximadamente 5 litros por m²
            nitrogenio = 10 * area  # Média de 10g de N por m²
            fosforo = 5 * area  # Média de 5g de P por m²
            potassio = 8 * area  # Média de 8g de K por m²
        elif cultura == "laranja":
            mudas = round(area / 30, 3)  # Média de uma muda a cada 30m²
            agua = 15 * area  # Aproximadamente 15 litros por m²
            nitrogenio = 8 * area  # Média de 8g de N por m²
            fosforo = 4 * area  # Média de 4g de P por m²
            potassio = 6 * area  # Média de 6g de K por m²
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


def exibir_plantacoes():
    if not plantacoes:
        print("Nenhuma plantação cadastrada.")
    else:
        for i, plantacao in enumerate(plantacoes):
            print(f"{i} - Cultura: {plantacao['cultura'].capitalize()}, Área: {plantacao['area']} m²")


def menu():
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


menu()