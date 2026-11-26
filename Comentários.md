# Devolutiva formativa — Atividade 02 da SA

**Estudante:** Erick  
**Turma:** Rio Negrinho — Tarde  
**UC:** Programação de Aplicativos  
**Projeto:** Sistema escolar — controle de notas  
**Referência de revisão:** 26/11/2026 — commit `459a7521`

**Capacidades avaliadas:**
- CT6 — Aplicar métodos e técnicas de programação.
- CT7 — Empregar comentários para documentação do código-fonte.

## O que você já desenvolveu

- Criou uma interface web com formulário de cadastro de alunos, campos de notas e visualização dos resultados.
- Implementou cálculo de médias, classificação da situação escolar e validação de notas de 0 a 10.
- Desenvolveu filtros por nome e situação, exclusão de registros e exportação CSV.
- Utilizou Python para disponibilizar a aplicação via servidor HTTP e armazenar os registros em um arquivo JSON.
- Separou algumas responsabilidades em funções e implementou tratamento de erros no recebimento e leitura de dados.

## Correções e oportunidades de melhoria

### 1. Organizar a separação entre interface e código Python

O arquivo `codigo/app.py` reúne o servidor e uma grande string com HTML, CSS e JavaScript.

Já o arquivo `interface/index.html` começa com `HTML_PAGE = """`, que é uma atribuição Python, e não uma instrução HTML.

Os arquivos `interface/style.css` e `interface/script.js` estão vazios.

**Como melhorar:**

- Deixar o HTML em `index.html`.
- Deixar o CSS em `style.css`.
- Deixar o JavaScript em `script.js`.
- Ajustar o servidor para entregar esses arquivos ou utilizar Flask.
- Evitar manter duas cópias da mesma página.

### 2. Melhorar as validações e a resposta aos erros

O servidor verifica os nomes e as notas, mas pode descartar registros inválidos silenciosamente.

A interface deve informar ao usuário quando o cadastro ou a comunicação com o servidor falhar.

**Como melhorar:**

- Retornar mensagens claras para entradas inválidas.
- Conferir a resposta do servidor antes de atualizar a interface.
- Testar campos vazios.
- Testar textos no lugar de números.
- Testar notas fora do intervalo permitido.

### 3. Documentar a execução do projeto

O README ainda contém principalmente as orientações gerais da Situação de Aprendizagem.

É necessário acrescentar:

- Objetivo do sistema.
- Requisitos para execução.
- Comando de execução: `python codigo/app.py`.
- No Mac: `python3 codigo/app.py`.
- Endereço de acesso: `http://127.0.0.1:8000`.
- Funcionalidades disponíveis.
- Organização dos arquivos.
- Funcionamento do armazenamento em JSON.

Acrescente comentários ou docstrings nas funções Python quando forem úteis para explicar as regras de negócio.

## Testes recomendados

| Teste | Resultado esperado |
|---|---|
| Cadastrar um aluno com notas 8, 7 e 9 | Média 8,0 e situação de aprovação |
| Informar nota superior a 10 | Cadastro rejeitado com mensagem compreensível |
| Filtrar a lista pelo nome | Apenas registros correspondentes são exibidos |
| Excluir um registro e reiniciar | A exclusão permanece registrada |
| Exportar os registros | Arquivo CSV contém os dados esperados |

## Prioridades para a próxima entrega — B4

- [ ] Separar HTML, CSS e JavaScript do código Python.
- [ ] Integrar o sistema ao banco de dados.
- [ ] Implementar as operações CRUD.
- [ ] Garantir a persistência dos registros.
- [ ] Atualizar o README.
- [ ] Executar e registrar os testes.
- [ ] Publicar as alterações no GitHub.

## Mensagem final

Erick, sua aplicação já apresenta funcionalidades importantes para o controle de notas.

A próxima etapa é melhorar a organização entre as camadas da aplicação, a comunicação de erros e a documentação, de modo que outro desenvolvedor consiga executar e compreender o projeto sem sua ajuda.

Continue evoluindo o sistema e procure compreender como cada funcionalidade foi implementada.

---
