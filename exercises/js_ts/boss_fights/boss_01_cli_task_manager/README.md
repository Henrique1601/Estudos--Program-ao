# 👹 Boss Fight 1: Gerenciador de Tarefas em Memória (Marco Nível 5)

## Desafio
Construir uma classe de serviço completa que encapsula estado, manipulação de coleções, filtros compostos e buscas case-insensitive.

## Requisitos
1. `adicionar(titulo, prioridade)`: Atribui ID auto-incremental, define `concluida = false` e armazena.
2. `alternarConclusao(id)`: Encontra a tarefa correspondente, inverte seu status (`concluida = !concluida`) e retorna `true`. Se não existir, retorna `false`.
3. `listar(filtro)`:
   - Se `filtro.apenasPendentes === true`, só retorna tarefas com `concluida === false`.
   - Se `filtro.prioridade` for informado, só retorna tarefas dessa prioridade.
4. `buscarPorTermo(termo)`: Retorna tarefas cujo título contenha o termo buscado (case-insensitive).
