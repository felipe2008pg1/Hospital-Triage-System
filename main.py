filatipon = []
filatipou = []
filatipop = []

logindosmedicos = {
    "usuario": "admin@hospital.com", 
    "senha": "123"
}

while True:
    print("\n" + "=" * 20)
    print(" FILA DE ATENDIMENTO!")
    print("="*20)
    print("N = Normal | U = Urgente | P = Prioritário | A = Área Médica")
    
    opcao = input("\nEscolha uma opção: ").upper()

    if opcao in ["N", "U", "P"]:
        nome = input("Digite o nome do paciente: ")
        try:
            idade = int(input("Digite a idade: "))
            dados = f"{nome} ({idade} anos)"
            
            if opcao == "N":
                filatipon.append(dados)
            elif opcao == "U":
                filatipou.append(dados)
            elif opcao == "P":
                filatipop.append(dados)
            
            print(f"Paciente {nome} adicionado com sucesso!")
        except ValueError:
            print("ERRO: Idade deve ser um número inteiro!")

    elif opcao == "A":
        loginm = input("E-mail: ")
        senham = input("Senha: ")

        if loginm == logindosmedicos["usuario"] and senham == logindosmedicos["senha"]:
            while True:
                print("\n--- PAINEL MÉDICO ---")
                print("1 - Fila Normal\n2 - Fila Urgente\n3 - Fila Prioritária\n4 - Sair")
                opcaomedica = input("Selecione: ")

                if opcaomedica == "1":
                    print(f"Fila Normal: {filatipon}")
                elif opcaomedica == "2":
                    print(f"Fila Urgente: {filatipou}")
                elif opcaomedica == "3":
                    print(f"Fila Prioritária: {filatipop}")
                elif opcaomedica == "4":
                    break
                else:
                    print("Opção inválida.")
        else:
            print("Login ou senha incorretos.")

    else:
        print("Opção inválida.")
