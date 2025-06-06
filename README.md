# buscaOrdenacao
🍹 Sistema de controle de polpas de frutas

Projeto acadêmico desenvolvido para demonstrar a aplicação de estruturas de dados (listas e dicionários) e algoritmos fundamentais (busca e ordenação) em Python. Ele simula um sistema de controle de estoque e vendas de polpas via console, destacando a sinergia entre esses conceitos. Pemsamos em ajudar em um problema de um dos integrantes do grupo que tem um pequeno negócio https://www.instagram.com/nat.polpas?igsh=bnZ0ejU1djJ0ZG1i

Objetivo

Criar um sistema de gerenciamento administrativo em Python, baseado no uso de estruturas de dados nativas (listas e dicionários). Este sistema permitirá o cadastro e controle de polpas e seu histórico de vendas. O projeto visa realizar a implementação prática de funcionalidades como adição, remoção, ordenação e busca, demonstrando a sinergia entre esses algoritmos para uma gestão eficiente.

Funcionalidades do Sistema

Cadastro
Cadastro de Polpas: Permite registrar novas polpas no estoque com seu nome e quantidade inicial.

Gerenciamento
Adição/Atualização de Estoque: Funcionalidade para aumentar a quantidade de polpas existentes ou adicionar novas polpas ao estoque.

Registro de Vendas: Permite registrar a venda de polpas, diminuindo a quantidade em estoque e atualizando o histórico de vendas.

Consulta e Visualização

Listagem de Estoque: Exibe todas as polpas em estoque, com opções de ordenação por nome ou por quantidade.

Histórico de Vendas: Apresenta todas as vendas registradas, com opções de ordenação por nome da polpa ou por quantidade vendida.

Busca de Polpa Específica: Permite verificar a quantidade de uma polpa específica no estoque.

Busca de Vendas por Polpa: Consulta todas as vendas de uma polpa específica, com a possibilidade de ordenar os resultados.

Análise de Estoque Baixo: Identifica e lista polpas com quantidade abaixo de um limite definido, exibindo-as ordenadas por quantidade.

Ordenação

Ordenação Dinâmica: Tanto o estoque quanto o histórico de vendas e os resultados de buscas podem ser ordenados dinamicamente por nome da polpa ou quantidade, conforme a escolha do usuário.

Estruturas Utilizadas
estoque (Dicionário): Armazena as polpas como chaves (strings) e suas respectivas quantidades em estoque como valores (inteiros). Embora seja um dicionário, ele é fundamental para gerenciar os itens de forma individual.
historico_vendas (Lista): Contém uma coleção linear de dicionários, onde cada dicionário representa uma venda e guarda informações como o nome da polpa e a quantidade vendida.

Tecnologias Utilizadas

Linguagem: Python (console)
Paradigma: Programação Estruturada (com elementos de Modularização por Funções)
Restrições: Foco no uso de estruturas de dados nativas (listas e dicionários), sem a necessidade de reimplementar lógicas complexas de baixo nível como redimensionamento manual

Justificativa Pedagógica

O uso de listas e dicionários nativos do Python neste projeto tem fins didáticos e reforça o entendimento de:

Armazenamento e Organização de Dados: Como dados relacionados (polpas, quantidades, histórico de vendas) são eficientemente armazenados e acessados.

Algoritmos de Ordenação e Busca: A aplicação prática de diferentes métodos para organizar (por nome, por quantidade) e localizar informações dentro das estruturas de dados.

Sinergia de Algoritmos: Como a combinação de busca e ordenação aprimora a análise e visualização dos dados, tornando o sistema mais funcional e intuitivo para o usuário.
\nRobustez de Entrada: A importância da validação de entrada de dados para garantir a integridade do sistema e proporcionar uma melhor experiência ao usuário.



