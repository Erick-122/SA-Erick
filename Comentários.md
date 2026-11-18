
# Devolutiva formativa — Atividade 01 da SA

**Estudante:** Erick  
**Turma:** Rio Negrinho — Tarde  
**Unidade Curricular:** Programação de Aplicativos  
**Projeto escolhido:** Escola — Sistema de Controle de Notas  
**Código analisado:** `codigo/app.py`  
**Referência:** Situação de Aprendizagem nº 1 — *Da Ideia ao Código*

## O que você já conseguiu desenvolver

Erick, você construiu uma boa base para um sistema escolar. O código está dividido em funções com responsabilidades definidas e mostra atenção à validação de dados e à clareza das explicações.

Pontos positivos identificados:

- Organizou o programa em funções como `limpar_tela()`, `validar_nota()`, `exibir_cabecalho()`, `cadastrar_aluno()` e `listar_relatorio()`.
- Utilizou **parâmetros e retorno de valores**, permitindo reaproveitar a função `validar_nota()` para as três notas de cada estudante.
- Aplicou **`try/except` e estruturas de repetição** para solicitar novamente uma nota quando a entrada não for numérica ou estiver fora do intervalo de 0 a 10.
- Utilizou **listas e dicionários** para representar alunos, notas, médias e situações escolares.
- Implementou o cálculo da média e a classificação em aprovado, recuperação ou reprovado, conforme as faixas definidas no próprio programa.
- Incluiu **docstrings e comentários** que facilitam a compreensão das funções.

## O que precisa ser corrigido

### 1. Concluir a função de relatório

O arquivo disponibilizado termina durante a construção do relatório, logo após a linha `print(f"• Total")`. A função `listar_relatorio()` ainda não apresenta um resumo final completo com a quantidade de estudantes por situação e a média da turma, embora já calcule esses valores.

**Como melhorar:** finalizar o relatório usando `len(alunos)`, `media_turma`, `aprovados`, `recuperacao` e `reprovados`. Depois, testar o relatório com estudantes de diferentes situações e também com a lista vazia.

### 2. Criar um fluxo principal para executar o programa

Atualmente, o arquivo define as funções, mas não chama `cadastrar_aluno()` nem `listar_relatorio()`. Ao executar `python codigo/app.py`, o usuário não recebe um menu ou uma sequência de ações para utilizar o sistema.

**Como melhorar:** criar uma função `menu()` com opções para cadastrar estudantes, listar o relatório e sair. Manter a lista de alunos durante a execução e iniciar o programa por um bloco `if __name__ == "__main__":`.

## Oportunidades de melhoria

### 3. Tornar os comentários mais objetivos

A documentação é um ponto forte, mas algumas linhas explicam operações muito simples, como incrementar um contador ou imprimir uma linha de texto. Isso aumenta o tamanho do arquivo sem acrescentar informação relevante.

**Como melhorar:** preservar as docstrings e priorizar comentários que expliquem **por que uma regra existe**, especialmente os limites das notas e as faixas de classificação.

### 4. Evitar dados duplicados quando possível

O dicionário de cada aluno guarda as três notas e também a média e a situação. Essa organização é válida para o exercício, mas exige cuidado: se uma nota for alterada futuramente, a média e a situação precisarão ser recalculadas.

**Como melhorar:** centralizar o cálculo da média e da situação em uma função reutilizável antes de implementar a edição de notas.

### 5. Comprovar o comportamento do sistema

Não identifiquei testes automatizados específicos da aplicação no código analisado. Para a entrega, é importante demonstrar que o sistema se comporta corretamente diante de diferentes entradas.

**Como melhorar:** verificar estes cenários:

1. Cadastro de aluno com três notas válidas.
2. Digitação de uma nota negativa, acima de 10 ou com letras.
3. Cadastro com nome vazio.
4. Relatório com alunos aprovados, em recuperação e reprovados.
5. Relatório quando não houver nenhum aluno cadastrado.

## Prioridades para a próxima versão

1. **Concluir a função `listar_relatorio()` e exibir as estatísticas calculadas.**
2. **Implementar o menu e a chamada inicial do programa para que o sistema seja utilizável.**
3. **Executar os cenários de teste e registrar os resultados.**
4. **Revisar comentários redundantes, mantendo a documentação das regras importantes.**

## Mensagem final

Erick, seu trabalho demonstra compreensão de funções, parâmetros, estruturas de controle, listas, dicionários e tratamento de entradas inválidas. A organização e a documentação são bons pontos de partida. Agora, concentre-se em **concluir o fluxo do sistema e demonstrar seu funcionamento de ponta a ponta**. Um programa menor, completo e testado vale mais do que funcionalidades que ainda não podem ser utilizadas. Continue registrando a evolução do projeto no GitHub.
