# Nível 18: Node.js Core - EventEmitter e Pub/Sub

## Objetivo
Implementar arquiteturas orientadas a eventos utilizando `node:events`.

## Requisitos
1. Criar classe `CentralAlertas extends EventEmitter`:
   - `emitirAlerta(nivel: "info" | "aviso" | "critico", mensagem: string): void`
   - Deve disparar o evento correspondente ao `nivel` e também um evento genérico `"qualquer"`.
   - `obterTotalDisparos(): number`

## Documentação oficial:
https://nodejs.org/docs/latest/api/events.html
