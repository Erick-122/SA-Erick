import os  # Importa o módulo 'os' para interagir com o sistema operacional (limpar a tela)

def limpar_tela():
    """
    Função utilitária para limpar a tela do console.
    O módulo 'os' verifica o sistema operacional:
    - Se for Windows ('nt'), executa o comando 'cls'.
    - Se for Linux ou macOS, executa o comando 'clear'.
    Isso garante que o menu fique sempre limpo e organizado para o usuário.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_nota(mensagem):
    """
    Função de validação defensiva para garantir que o usuário digite 
    apenas números válidos entre 0 e 10.
    
    Usa um loop infinito (while True) que só é interrompido (return) 
    quando a entrada atende a todas as regras de negócio.
    """
    while True:  # Loop infinito que continuará rodando até que o usuário digite um valor válido
        try:
            # Exibe a mensagem recebida por parâmetro, captura o texto e tenta convertê-lo para decimal (float)
            nota = float(input(mensagem))
            
            # Verifica se o número convertido está dentro do intervalo escolar permitido (0 a 10)
            if 0 <= nota <= 10:
                return nota  # Retorna a nota válida para quem chamou a função e encerra o loop
            else:
                # Caso o número seja menor que 0 ou maior que 10, avisa o usuário e repete o loop
                print("A nota deve estar entre 0 e 10. Tente novamente.")
                
        except ValueError:
            # Captura erros caso o usuário digite letras, símbolos ou deixe a entrada vazia
            print("Entrada inválida! Digite apenas números.")

def exibir_cabecalho():
    """Exibe o cabeçalho visual padrão do sistema no topo do console."""
    print("=" * 50)  # Imprime uma linha com 50 caracteres de sinal de igual
    print("        SISTEMA ESCOLAR - CONTROLE DE NOTAS")
    print("=" * 50)

def cadastrar_aluno(alunos):
    """
    Gerencia o processo de cadastro de um novo aluno e suas respectivas notas.
    Recebe por parâmetro a lista 'alunos' para adicionar o novo registro.
    """
    print("\n--- NOVO CADASTRO ---")
    
    # Solicita o nome do aluno e remove espaços em branco extras nas pontas usando .strip()
    nome = input("Digite o nome do aluno: ").strip()
    
    # Validação para impedir que o usuário cadastre um nome vazio (pressionando apenas ENTER)
    if not nome:
        print("O nome não pode estar vazio.")
        return  # Encerra a execução desta função prematuramente e volta ao menu

    # Coletando as 3 notas utilizando a função de validação criada anteriormente
    n1 = validar_nota(f"Digite a 1ª nota de {nome}: ")
    n2 = validar_nota(f"Digite a 2ª nota de {nome}: ")
    n3 = validar_nota(f"Digite a 3ª nota de {nome}: ")

    # Calculando a média aritmética das 3 notas somando todas e dividindo por 3
    media = (n1 + n2 + n3) / 3
    
    # Definindo a situação acadêmica com base no valor da média obtida
    if media >= 7.0:
        situacao = "Aprovado(a) "
    elif media >= 5.0:
        situacao = "Em Recuperação "
    else:
        situacao = "Reprovado(a) "

    # Criando um dicionário para estruturar os dados do aluno de forma organizada por chaves e valores
    aluno = {
        "nome": nome.title(),               # .title() padroniza a primeira letra de cada palavra em maiúscula
        "notas": [n1, n2, n3],             # Armazena as 3 notas dentro de uma lista interna
        "media": media,                    # Armazena o valor numérico da média calculada
        "situacao": situacao               # Armazena a string contendo o status final do aluno
    }
    
    # Adiciona o dicionário do aluno recém-criado dentro da lista principal 'alunos'
    alunos.append(aluno)
    print(f"\nAluno(a) '{aluno['nome']}' cadastrado(a) com sucesso!")

def listar_relatorio(alunos):
    """
    Percorre a lista de alunos cadastrados, exibe o boletim individual de cada um
    e calcula estatísticas gerais da turma (média da sala e contadores de status).
    """
    # Verifica se a lista de alunos está vazia antes de tentar gerar qualquer relatório
    if not alunos:
        print("\nNenhum aluno cadastrado até o momento.")
        return  # Sai da função se não houver registros

    print("\n" + "=" * 50)
    print("          RELATÓRIO FINAL DA TURMA")
    print("=" * 50)
    
    # Declarando variáveis acumuladoras e contadoras para gerar as estatísticas da turma
    soma_medias = 0
    aprovados = 0
    recuperacao = 0
    reprovados = 0

    # A função enumerate() percorre a lista extraindo o índice (começando em 1) e o dicionário do aluno
    for i, a in enumerate(alunos, 1):
        print(f"{i}. Aluno(a): {a['nome']}")
        # Formata a exibição das notas utilizando :.1f para mostrar sempre 1 casa decimal
        print(f"   Notas: {a['notas'][0]:.1f} | {a['notas'][1]:.1f} | {a['notas'][2]:.1f}")
        print(f"   Média: {a['media']:.2f}")  # Formata a média para exibir 2 casas decimais
        print(f"   Situação: {a['situacao']}")
        print("-" * 50)
        
        # Acumula o valor da média do aluno atual na variável totalizadora
        soma_medias += a['media']
        
        # Verifica o texto da situação para incrementar o contador correto de desempenho da turma
        if "Aprovado" in a['situacao']:
            aprovados += 1
        elif "Recuperação" in a['situacao']:
            recuperacao += 1
        else:
            reprovados += 1

    # Calcula a média geral da sala dividindo a soma de todas as médias pelo número total de alunos
    media_turma = soma_medias / len(alunos)
    
    # Exibe o resumo estatístico consolidado da turma inteira
    print("\nESTATÍSTICAS DA TURMA:")
    print(f"• Total")