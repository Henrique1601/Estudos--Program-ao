// Nível 07: TypeScript - Interfaces e Modelagem

export interface ItemVenda {
    id: string;
    nome: string;
    precoUnitario: number;
    quantidade: number;
}

export interface Recibo {
    totalBruto: number;
    desconto: number;
    totalLiquido: number;
}

export function gerarRecibo(itens: ItemVenda[], percentualDesconto: number): Recibo {
    // ESCREVA SEU CÓDIGO AQUI
    return { totalBruto: 0, desconto: 0, totalLiquido: 0 };
}
