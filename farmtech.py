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
            print("Entrada de dados")
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