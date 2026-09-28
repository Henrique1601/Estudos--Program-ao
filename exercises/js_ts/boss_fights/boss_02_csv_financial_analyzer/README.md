# 👹 Boss Fight 2: Analisador de Extrato Financeiro CSV (Marco Nível 10)

## Desafio
Processar um relatório CSV de fluxo de caixa em texto puro, ignorar cabeçalhos, tratar linhas em branco, converter tipos e gerar um resumo analítico completo usando agregadores funcionais.

## Requisitos
1. Divida o texto por quebras de linha (`\n` ou `\r\n`).
2. Ignore o cabeçalho (`data,descricao...`) e linhas vazias.
3. Para cada linha, use `.split(",")` e desestruture `[data, descricao, categoria, valorStr, tipo]`.
4. Converta o valor com `Number(valorStr)`.
5. Acumule `totalReceitas` e `totalDespesas`.
6. Calcule `saldoFinal = totalReceitas - totalDespesas`.
7. Descubra a categoria com a maior despesa somada.
8. Mapeie a quantidade de transações em cada categoria.
