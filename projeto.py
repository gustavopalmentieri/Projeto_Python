qtd_pacientes = int(input("Digite a quantidade de pacientes: ")) #Definir que o programa vai pegar dados de 3 pacientes
lista_pacientes = [] #Uma lista para armazenar futuras informações do dicionário
escolhas = 5 #Defini um loop que irá mostrar os campos de opções para o usuário 5 vezes contendo as informções necessárias


for paciente in range(qtd_pacientes):  #Loop para cadastrar os pacientes

    print(" ---- Dados Cadastrais ----")

    pacientes = {"nome" : input("Informe seu nome completo: "),
                 "peso" : float(input("Informe seu peso em 'KG': ")),
                 "sexo" : input("Digite 'M'- para Masculino e 'F' - para feminino: "),
                 "altura" : int(input("Informe sua altura em 'CM': ")),
                 "idade" : int(input("Informe sua idade: "))}
      
    
    altura_metros = pacientes["altura"] / 100 #Estou convertendo a altura em CM para Metros (Para conseguir calcular o IMC)

    imc = pacientes["peso"] / (altura_metros ** 2) #Fórmula do IMC
    pacientes["imc"] = imc #Armazena a informção de IMC no dicionário do paciente

    if pacientes["sexo"] == 'M': #Se caso for homem a infromação que entrar, irá fazer parte da fórmula de TMB para esse sexo em especifico

        tmb = 9.99 * pacientes["peso"] + 6.25 * pacientes["altura"] - 4.92 * pacientes["idade"] + 5 #Fórmula do TMB - Masculino
        pacientes["tmb"] = tmb #Armazena a informção de IMC no dicionário do paciente masculino (homem)

    else: #Se caso for mulher a informação que entrar, irá fazer parte da fórmula de TMB para esse sexo em específico

        tmb = 9.99 * pacientes["peso"] + 6.25 * pacientes["altura"] - 4.92 * pacientes["idade"] - 161 #Fórmula do TMB - Feminino
        pacientes["tmb"] = tmb #Armazena a informção de IMC no dicionário do paciente feminino (mulher)

    lista_pacientes.append(pacientes) #Na lista e adicionado todas as informações recebidas dos pacientes no loop

#Assumi que a primeira posição dos pacientes seria a maior, e determinei uma váriavel para isso e logo comparei, se uma informação nova chegasse e fosse maior ou menor da que já estava, ele faz a troca e mantém a maior independente da ordem de entrada dos dados.

maior_imc = lista_pacientes[0]["imc"]
maior_tmb = lista_pacientes[0]["tmb"]
menor_imc = lista_pacientes[0]["imc"]
menor_tmb = lista_pacientes[0]["tmb"]

for paciente in lista_pacientes: #Um loop para comparar e determinar qual a entrada vai ser o maior ou menor independente da ordem de entrada desses dados

    #* Troquei os ELIFs por IFs pq do jeito que tava antes com elif ele poderia ignorar o "tmb" por exemplo e não registrar caso um pacientes tivesse o maior imc e tmb, ele só salvaria o primeiro, no caso aqui o imc.

    #* Removi os nomes daqui pois não tem necessidade de salvar esses valores aqui.
    if paciente["imc"] > maior_imc: 
        maior_imc = paciente["imc"]
        
    if paciente["tmb"] > maior_tmb:
        maior_tmb = paciente["tmb"]

    if paciente["imc"] < menor_imc:
        menor_imc = paciente["imc"]

    if paciente["tmb"] < menor_tmb:
        menor_tmb = paciente["tmb"]


for escolha in range(escolhas): #Um loop do painel de escolha para permitir que a pessoa consiga acessar uma ou mais informações de uma vez

    print("\n ----- Menu de Opções ----\n")
    print("---> 1 - Maior IMC\n")
    print("---> 2 - Maior TMB\n")
    print("---> 3 - Menor IMC\n")
    print("---> 4 - Menor TMB\n")
    print("---> 5 - Encerrar o Programa\n")


    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        #* Apenas uma ideia! Não precisa fazer as verificações e exibir quem tem o maior imc direto na opção.

        # * Esse for aqui é para pegar mais de um paciente com o maior imc ex: se 2 pacientes tiverem 25 de imc ele vai mostrar os 2 (apenas uma correção do que foi pedido no exercicio) 

        # * OBS: vou deixar o bloco de codigo que fiz aqui de exemplo no primeiro IF das escolhas. se achar interessante e que faz sentido para você, faça a mesma coisa nos outros IFs, a logica vai ser a mesma que essa, só vai mudar o que você ta querendo pegar. 
        if paciente["imc"] > maior_imc: 

            maior_imc = paciente["imc"]
            nome_maior_imc = paciente["nome"]

            for paciente in pacientes:
                if paciente["imc"] == maior_imc:
                    print(f"Nome: {paciente['nome']}, IMC: {paciente['imc']:.2f}")

    if escolha == 2:
        print(f"Paciente: {nome_maior_tmb}, está com: {round(maior_tmb, 2)} de TMB")

    if escolha == 3:
        print(f"Paciente: {nome_menor_imc}, está com: {round(menor_imc, 2)} de IMC")  

    if escolha == 4:
        print(f"Paciente: {nome_menor_tmb}, está com: {round(menor_tmb,2)} de TMB")

    if escolha == 5:
        print("Encerrando o programa...")
        break