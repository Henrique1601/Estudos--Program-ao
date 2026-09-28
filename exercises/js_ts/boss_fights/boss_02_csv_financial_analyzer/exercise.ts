// Boss Fight 2 (Marco Nível 10): Analisador de Extrato Financeiro CSV
// Uso intensivo de reduce, Map, destructuring e manipulação de strings.

export interface ResumoFinanceiro {
    totalReceitas: number;
    totalDespesas: number;
    saldoFinal: number;
    maiorDespesaCategoria: string;
    contagemPorCategoria: Record<string, number>;
}

/**
 * Recebe o conteúdo bruto de um arquivo CSV de transações no formato:
 * data,descricao,categoria,valor,tipo
 * (onde tipo é 'receita' ou 'despesa')
 * 
 * Exemplo de linha:
 * 2026-09-01,Salario,trabalho,5000,receita
 * 2026-09-02,Supermercado,alimentacao,450,despesa
 */
export function analisarExtratoCsv(conteudoCsv: string): ResumoFinanceiro {
    // ESCREVA SEU CÓDIGO AQUI
    return {
        totalReceitas: 0,
        totalDespesas: 0,
        saldoFinal: 0,
        maiorDespesaCategoria: "",
        contagemPorCategoria: {},
    };
}
