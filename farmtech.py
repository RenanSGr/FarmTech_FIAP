registros = []

def salvar_fazenda(nome_fazenda, cultura, area_m2, tipo_insumo, quantidade_insumo, unidade_insumo):
    registro_novo = {"fazenda": nome_fazenda,"cultura": cultura,"area_m2": area_m2, "tipo_insumo": tipo_insumo, "quantidade_insumo": quantidade_insumo, "unidade_insumo": unidade_insumo}
    registros.append(registro_novo)
    print(f"Nova fazenda registrada: {registro_novo}")

def calcular_area_retangular(largura, comprimento):
    return largura * comprimento

def incluir_fazenda():
    while True:
        print("1. Cana-de-açúcar")

        cultura = input("Insira a cultura: ")

        if cultura == "1":
            fazenda = input("\nInsira o nome da fazenda: ")
            cultura = "Cana-de-açúcar"
            largura = float(input("Insira a largura do terreno em metros: "))
            comprimento = float(input("Insira a comprimento do terreno em metros: "))
            area_m2 = calcular_area_retangular(largura, comprimento)
            tipo_insumo = "Fertilizante NPK"
            unidade_insumo = "kg"
            quantidade_insumo_kg = 500 * (area_m2 / 10000)
        else:
            print("Opção Inválida!\n")
            continue

        salvar_fazenda(fazenda,cultura,area_m2,tipo_insumo,unidade_insumo,quantidade_insumo_kg)
        break

def menu():
    while True:
        print("\n### FarmTech Solutions ###")
        print("1. Entrada de dados")
        print("2. Saída de dados")
        print("3. Atualização de dados")
        print("4. Exclusão de dados")
        print("5. Sair")

        opcao = input("\nEscolha uma opção (Somente o número):")
        print("")

        if opcao == "1":
            incluir_fazenda()
        elif opcao == "2":
            print("Saída de dados")
        elif opcao == "3":
            print("Atualização de dados")
        elif opcao == "4":
            print("Exclusão de dados")
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção Inválida!")

if __name__ == "__main__":
    menu()