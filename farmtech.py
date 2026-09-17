import csv
import math

registros = []


def exportar_dados():
    if not registros:
        print("Nenhum dado para exportar.")
        return
    colunas = ['fazenda', 'cultura', 'area_m2', 'tipo_insumo', 'quantidade_insumo', 'unidade_insumo']
    with open('dados_farmtech.csv', mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(registros)
    print("Dados exportados para 'dados_farmtech.csv' com sucesso!")

def salvar_fazenda(nome_fazenda, cultura, area_m2, tipo_insumo, quantidade_insumo, unidade_insumo):
    registro_novo = {"fazenda": nome_fazenda,"cultura": cultura,"area_m2": area_m2, "tipo_insumo": tipo_insumo, "quantidade_insumo": quantidade_insumo, "unidade_insumo": unidade_insumo}
    registros.append(registro_novo)
    print(f"Nova fazenda registrada: {registro_novo}")

def calcular_area_retangular(largura, comprimento):
    return largura * comprimento

def calcular_area_circular(raio):
    return math.pi * raio ** 2

def incluir_fazenda():
    while True:
        print("1. Cana-de-açúcar")
        print("2. Laranja")

        cultura = input("Insira a cultura: ")

        if cultura == "1":
            fazenda = input("\nInsira o nome da fazenda: ")
            cultura = "Cana-de-açúcar"
            largura = float(input("Insira a largura do terreno em metros: "))
            comprimento = float(input("Insira a comprimento do terreno em metros: "))
            area_m2 = calcular_area_retangular(largura, comprimento)
            tipo_insumo = "Fertilizante NPK"
            unidade_insumo = "kg"
            quantidade_insumo = 500 * (area_m2 / 10000)
        elif cultura == "2":
            fazenda = input("\nInsira o nome da fazenda: ")
            cultura = "Laranja"
            raio = float(input("Insira o raio do terreno em metros: "))
            area_m2 = calcular_area_circular(raio)
            tipo_insumo = "Defensivo Foliar"
            unidade_insumo = "litros"
            quantidade_insumo = 2000 * (area_m2 / 10000)
        else:
            print("Opção Inválida!\n")
            continue

        salvar_fazenda(fazenda,cultura,area_m2,tipo_insumo,quantidade_insumo,unidade_insumo)
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
            exportar_dados()
        elif opcao == "2":
            print("Saída de dados")
        elif opcao == "3":
            print("Atualização de dados")
            exportar_dados()
        elif opcao == "4":
            print("Exclusão de dados")
            exportar_dados()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção Inválida!")

if __name__ == "__main__":
    menu()