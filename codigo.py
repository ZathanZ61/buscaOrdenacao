# Inicializa o dicionário 'estoque' para armazenar o nome da polpa como chave e a quantidade como valor.

estoque = {}

#Lista para armazenar o histórico de vendas. Cada venda será um dicionário contendo o nome da polpa e a quantidade vendida.

historico_vendas = []

# Funções de Ordenação

def ordenar_estoque(estoque_dict, criterio="nome"):

# Ordena o estoque com base no critério fornecido.

    if criterio == "nome":
        return sorted(estoque_dict.items(), key=lambda item: item[0])
    elif criterio == "quantidade":
        return sorted(estoque_dict.items(), key=lambda item: item[1])
    else:
        return list(estoque_dict.items())


def ordenar_historico_vendas(historico, criterio="nome"):
  
#Ordena o histórico de vendas com base no critério fornecido

    if criterio == "nome":
        return sorted(historico, key=lambda venda: venda['polpa'])
    elif criterio == "quantidade":
        return sorted(historico, key=lambda venda: venda['quantidade'])
    else:
        return historico


# Funções de Busca

def buscar_polpa(estoque, nome_polpa):
  
# Busca a quantidade de uma polpa específica no estoque.
    
    return estoque.get(nome_polpa)


def buscar_vendas_por_polpa(historico, nome_polpa):

# Busca todas as vendas de uma polpa específica no histórico de vendas.
  
    resultados = []
    for venda in historico:
        if venda['polpa'] == nome_polpa:
            resultados.append(venda)
    return resultados

def buscar_polpas_abaixo_quantidade(estoque, limite):
    """
    Busca polpas no estoque com quantidade abaixo de um limite especificado.
    Esta função é uma busca que identifica um subconjunto de dados (polpas com estoque baixo).
    """
    resultados = []
    for polpa, quantidade in estoque.items():
        if quantidade < limite:
            resultados.append((polpa, quantidade))
    return resultados


# Funções de Gerenciamento

def adicionar_polpa(estoque, nome_polpa, quantidade):

# Adiciona uma nova polpa ao estoque ou aumenta a quantidade de uma existente.

    if nome_polpa in estoque:
        estoque[nome_polpa] += quantidade
        print(f"Adicionadas {quantidade} unidades de {nome_polpa}. Novo total em estoque: {estoque[nome_polpa]}.")
    else:
        estoque[nome_polpa] = quantidade
        print(f"{nome_polpa} adicionada ao estoque com {quantidade} unidades.")


def registrar_venda(estoque, historico, nome_polpa, quantidade):

# Registra uma venda, atualizando o estoque e o histórico de vendas.

    quantidade_estoque = estoque.get(nome_polpa)
    if quantidade_estoque is None:
        print(f"Erro: {nome_polpa} não encontrada no estoque.")
        return
    elif quantidade <= 0: # Adicionado validação para quantidade não positiva
        print("Erro: A quantidade a ser vendida deve ser um número positivo.")
        return
    elif quantidade > quantidade_estoque:
        print(f"Erro: Estoque insuficiente de {nome_polpa}. Disponível: {quantidade_estoque}, solicitado: {quantidade}.")
        return
    else:
        estoque[nome_polpa] -= quantidade
        historico.append({"polpa": nome_polpa, "quantidade": quantidade})
        print(f"{quantidade} unidades de {nome_polpa} vendidas. Estoque restante: {estoque[nome_polpa]}.")


def exibir_estoque(estoque_a_exibir, titulo="Estoque Atual"):
  
# Exibe o estoque formatado.
  
    print(f"\n--- {titulo} ---")
    if not estoque_a_exibir:
        print("O estoque está vazio ou não há itens para exibir.")
    else:
        for polpa, quantidade in estoque_a_exibir:
            print(f"{polpa}: {quantidade} unidades")
    print("----------------------")


def exibir_historico_vendas(historico_a_exibir, titulo="Histórico de Vendas"):
  
# Exibe o histórico de vendas formatado.

    print(f"\n--- {titulo} ---")
    if not historico_a_exibir:
        print("Nenhuma venda registrada ainda para os critérios selecionados.")
    else:
        for venda in historico_a_exibir:
            print(f"Polpa: {venda['polpa']}, Quantidade: {venda['quantidade']}")
    print("---------------------------")


# --- Função auxiliar para leitura de inteiros (melhorada) ---
def ler_inteiro_valido(mensagem):
    '''
    Solicita ao usuário uma entrada de número inteiro e valida.
    Continua pedindo até que uma entrada válida seja fornecida.
    '''
  
    while True:
        try:
            valor = int(input(mensagem))
            # Adicionado validação para garantir que a quantidade não seja zero ou negativa
            if valor <= 0:
                print("A quantidade deve ser um número inteiro positivo. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


# --- Interface de Usuário (Principal) ---

while True:
    print("\n--- Sistema de Controle de Polpas ---")
    print("1. Adicionar Polpa ao Estoque")
    print("2. Registrar Venda")
    print("3. Exibir Estoque")
    print("4. Buscar Polpa no Estoque")
    print("5. Exibir Histórico de Vendas")
    print("6. Buscar Vendas por Polpa (com opção de ordenação dos resultados)")
    print("7. Análise de Estoque Baixo (Busca e Ordenação)")
    print("8. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome da polpa: ")
        # A mensagem de erro de 'quantidade inválida' agora é tratada dentro de ler_inteiro_valido
        quantidade = ler_inteiro_valido("Quantidade a adicionar: ")
        adicionar_polpa(estoque, nome, quantidade)
    elif opcao == '2':
        nome = input("Nome da polpa vendida: ")
        # A mensagem de erro de 'quantidade inválida' agora é tratada dentro de ler_inteiro_valido
        quantidade = ler_inteiro_valido("Quantidade vendida: ")
        registrar_venda(estoque, historico_vendas, nome, quantidade)
    elif opcao == '3':
        while True:
            print("\nComo deseja ordenar o estoque?")
            print("  1. Por Nome")
            print("  2. Por Quantidade")
            criterio_opcao = input("Escolha o critério (1 ou 2): ")
            
            criterio = None
            if criterio_opcao == '1':
                criterio = "nome"
            elif criterio_opcao == '2':
                criterio = "quantidade"
            else:
                print("Opção inválida. Por favor, digite 1 ou 2.")
                continue
            break

        estoque_ordenado = ordenar_estoque(estoque, criterio)
        exibir_estoque(estoque_ordenado, f"Estoque Atual (Ordenado por {criterio.capitalize()})")
    elif opcao == '4':
        nome_busca = input("Nome da polpa a buscar: ")
        quantidade_encontrada = buscar_polpa(estoque, nome_busca)
        if quantidade_encontrada is not None:
            print(f"{nome_busca}: {quantidade_encontrada} unidades em estoque.")
        else:
            print(f"{nome_busca} não encontrada no estoque.")
    elif opcao == '5':
        while True:
            print("\nComo deseja ordenar o histórico de vendas?")
            print("  1. Por Nome da Polpa")
            print("  2. Por Quantidade Vendida")
            criterio_opcao = input("Escolha o critério (1 ou 2): ")

            criterio = None
            if criterio_opcao == '1':
                criterio = "nome"
            elif criterio_opcao == '2':
                criterio = "quantidade"
            else:
                print("Opção inválida. Por favor, digite 1 ou 2.")
                continue
            break
            
        historico_ordenado = ordenar_historico_vendas(historico_vendas, criterio)
        exibir_historico_vendas(historico_ordenado, f"Histórico de Vendas (Ordenado por {criterio.capitalize()})")
    elif opcao == '6':
        nome_busca = input("Nome da polpa para buscar nas vendas: ")
        vendas_encontradas = buscar_vendas_por_polpa(historico_vendas, nome_busca)
        if vendas_encontradas:
            print(f"\n--- Vendas de {nome_busca} ---")
            while True:
                print("\nComo deseja ordenar estas vendas?")
                print("  1. Por Nome da Polpa")
                print("  2. Por Quantidade Vendida")
                criterio_opcao_venda = input("Escolha o critério (1 ou 2, ou Enter para não ordenar): ")

                criterio_ordenacao_venda = None
                if criterio_opcao_venda == '1':
                    criterio_ordenacao_venda = "nome"
                elif criterio_opcao_venda == '2':
                    criterio_ordenacao_venda = "quantidade"
                elif criterio_opcao_venda == '':
                    break
                else:
                    print("Opção inválida. Por favor, digite 1, 2 ou Enter.")
                    continue
                break

            if criterio_ordenacao_venda:
                vendas_ordenadas = ordenar_historico_vendas(vendas_encontradas, criterio_ordenacao_venda)
                exibir_historico_vendas(vendas_ordenadas, f"Vendas de {nome_busca} (Ordenadas por {criterio_ordenacao_venda.capitalize()})")
            else:
                exibir_historico_vendas(vendas_encontradas, f"Vendas de {nome_busca} (Sem Ordenação)")
        else:
            print(f"Não houve vendas registradas de {nome_busca}.")
    elif opcao == '7':
        # A mensagem de erro de 'quantidade inválida' agora é tratada dentro de ler_inteiro_valido
        limite_quantidade = ler_inteiro_valido("Qual o limite mínimo para considerar estoque baixo? ")
        
        polpas_baixas = buscar_polpas_abaixo_quantidade(estoque, limite_quantidade)
        
        if polpas_baixas:
            polpas_baixas_ordenadas = ordenar_estoque(dict(polpas_baixas), "quantidade")
            exibir_estoque(polpas_baixas_ordenadas, f"Polpas com Estoque Abaixo de {limite_quantidade} (Ordenadas por Quantidade)")
        else:
            print(f"Nenhuma polpa com estoque abaixo de {limite_quantidade}.")
    elif opcao == '8':
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")
