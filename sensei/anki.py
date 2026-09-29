"""Exportador de Flashcards para Anki: Modelos mentais e pegadinhas dos 20 níveis."""
import csv
from pathlib import Path
from sensei.colors import bold, cyan, green, yellow, dim, magenta

FLASHCARDS = [
    {
        "front": "Em JavaScript, qual a diferença fundamental entre atribuição de primitivos (number, string) e objetos/arrays?",
        "back": "Primitivos são copiados por VALOR (uma nova cópia independente é criada na pilha). Objetos e arrays são copiados por REFERÊNCIA (ambas as variáveis passam a apontar para o mesmo endereço de memória no Heap). Modificar um altera o outro.",
        "tags": "javascript memoria fundamentos"
    },
    {
        "front": "Por que 'const arr = [1, 2]; arr.push(3);' funciona sem erro se a variável foi declarada com const?",
        "back": "Porque 'const' protege apenas o PONTEIRO (o endereço de memória atribuído à variável arr). Ela impede reatribuição ('arr = [1, 2, 3]'), mas não impede a mutação das propriedades internas do objeto existente na memória.",
        "tags": "javascript const memoria"
    },
    {
        "front": "Qual é a pegadinha clássica do método 'arr.sort()' em JavaScript quando chamado sem função comparadora?",
        "back": "Por padrão, o JavaScript converte todos os elementos em STRINGS e os ordena pela tabela Unicode lexicográfica. Logo, [10, 5, 20].sort() vira [10, 20, 5], pois '1' vem antes de '2' e '5'. Para ordenar números corretamente, passe: (a, b) => a - b.",
        "tags": "javascript pegadinhas arrays"
    },
    {
        "front": "O que causa o erro 'TypeError: Cannot read properties of undefined (reading 'xyz')'?",
        "back": "A tentativa de acessar a propriedade '.xyz' em uma variável cujo valor atual é estritamente 'undefined' (ou 'null'). Causa comum: chamada assíncrona sem 'await', retorno vazio de um '.find()' ou objeto aninhado inexistente.",
        "tags": "javascript erros debugging"
    },
    {
        "front": "Qual a diferença entre '==' (igualdade abstrata) e '===' (igualdade estrita)?",
        "back": "'==' realiza coerção implícita de tipo antes de comparar (ex: '0' == 0 é true, null == undefined é true). '===' compara valor e tipo sem conversão (ex: '0' === 0 é false). Sempre prefira '===' para evitar bugs sutis.",
        "tags": "javascript tipos fundamentos"
    },
    {
        "front": "O que é uma Closure (fechamento léxico) e onde ela é útil?",
        "back": "É a capacidade de uma função interna 'lembrar' e acessar variáveis do seu escopo léxico pai mesmo após a função externa já ter terminado sua execução. Essencial para encapsulamento de estado privado, factories e funções de debounce/throttle.",
        "tags": "javascript escopo funcoes"
    },
    {
        "front": "O que causa o erro 'RangeError: Maximum call stack size exceeded' e como inspecioná-lo?",
        "back": "Ocorre quando a pilha de execução (Call Stack) atinge o limite do motor V8 (~10.000 chamadas). Quase sempre indica uma função recursiva sem 'caso base' ou um loop de chamadas mútuas infinitas. Inspecione se o argumento converge para a parada.",
        "tags": "javascript stack recursao"
    },
    {
        "front": "Qual a diferença entre a Macrotask Queue e a Microtask Queue no Event Loop do Node.js?",
        "back": "Microtasks (Promises '.then()', 'queueMicrotask', 'process.nextTick') têm prioridade absoluta e são esvaziadas inteiramente antes de qualquer Macrotask (setTimeout, setInterval, setImmediate, I/O).",
        "tags": "nodejs event-loop async"
    },
    {
        "front": "No TypeScript, qual a diferença entre 'unknown' e 'any'?",
        "back": "'any' desliga completamente a checagem de tipos (perigoso). 'unknown' é o tipo 'seguro para qualquer valor': o compilador exige que você faça narrowing (com 'typeof', 'instanceof' ou checagem de propriedade) antes de acessar qualquer método dele.",
        "tags": "typescript tipos seguranca"
    },
    {
        "front": "O que acontece com os tipos do TypeScript em tempo de execução (runtime)?",
        "back": "Eles são completamente apagados (type erasure). Interfaces, type aliases e generics NÃO existem na memória do Node.js/navegador. Validações de dados externos (APIs, formulários) precisam ser feitas com código JS real (ou bibliotecas como Zod).",
        "tags": "typescript compilacao runtime"
    },
    {
        "front": "Por que usar loops tradicionais (ou 'for...of') pode ser mais vantajoso que 'arr.map().filter().reduce()' em código de alto desempenho?",
        "back": "Encadear .map().filter() aloca novos arrays intermediários na memória Heap a cada chamada, aumentando pressão sobre o Garbage Collector. Um único 'for' ou 'reduce' processa os dados em uma única passagem (O(N) tempo e O(1) espaço extra).",
        "tags": "performance algoritmos memoria"
    },
    {
        "front": "O que é a técnica de Debounce e qual problema ela resolve?",
        "back": "Debounce adia a execução de uma função cara até que um determinado intervalo de tempo tenha se passado sem nenhum novo disparo. Exemplo: campo de busca digitado pelo usuário — dispara a pesquisa só 300ms após a última tecla digitada.",
        "tags": "padroes funcoes async"
    },
    {
        "front": "O que é Memoização e qual o seu compromisso (trade-off)?",
        "back": "Técnica de caching do resultado de funções puras baseado nos argumentos recebidos. Trade-off: gasta mais memória RAM (espaço) para economizar tempo de CPU em chamadas repetidas.",
        "tags": "otimizacao algoritmos funcoes"
    },
    {
        "front": "O que é e como funciona a técnica de Dois Ponteiros (Two Pointers) em vetores ordenados?",
        "back": "Posiciona-se um ponteiro no início (left = 0) e outro no fim (right = length - 1), movendo-os em direção ao centro com base em uma condição. Transforma buscas de pares de O(N²) para O(N) com complexidade de espaço O(1).",
        "tags": "algoritmos estruturas-dados ponteiros"
    },
    {
        "front": "Qual é a principal diferença entre 'fs.readFileSync' e 'fs.promises.readFile' no Node.js?",
        "back": "'readFileSync' bloqueia a thread única do Event Loop do Node.js, impedindo que qualquer outra requisição ou temporizador seja atendido até o arquivo ser lido do disco. 'fs.promises.readFile' delega a leitura para a libuv em background e não bloqueia a thread.",
        "tags": "nodejs io async"
    },
    {
        "front": "O que é uma Função Pura (Pure Function) e por que ela é fácil de testar?",
        "back": "1) Dado o mesmo input, ela SEMPRE retorna o mesmo output. 2) Ela NÃO produz efeitos colaterais (side-effects) — não altera variáveis externas, não faz requisições de rede e não altera o DOM. Testá-la não requer mocks nem preparação de estado.",
        "tags": "programacao-funcional testes arquitetura"
    },
    {
        "front": "Como clonar um objeto aninhado de forma profunda em JavaScript moderno sem usar bibliotecas externas?",
        "back": "Use a função nativa 'structuredClone(obj)'. Ela suporta arrays aninhados, Maps, Sets e referências circulares nativamente, ao contrário de 'JSON.parse(JSON.stringify(obj))' que perde datas, undefined e funções.",
        "tags": "javascript memoria modernos"
    },
    {
        "front": "Por que o código 'for (var i = 0; i < 3; i++) { setTimeout(() => console.log(i), 100); }' imprime '3 3 3' em vez de '0 1 2'?",
        "back": "Porque 'var' possui escopo de função, não de bloco. Apenas UMA única variável 'i' existe na memória, e quando os timeouts rodam 100ms depois, o loop já terminou e 'i' vale 3. Trocar 'var' por 'let' cria uma nova ligação léxica a cada iteração.",
        "tags": "javascript escopo pegadinhas"
    },
    {
        "front": "O que significa o conceito de Imutabilidade e como ele previne 'efeitos colaterais fantasma'?",
        "back": "Imutabilidade significa nunca alterar o estado ou objeto original após sua criação. Sempre que precisar de alteração, cria-se uma nova cópia com a alteração desejada. Isso garante que outras partes do sistema que dependem daquele objeto não tenham surpresas.",
        "tags": "arquitetura principios qualidade"
    },
    {
        "front": "Ao fazer testes automatizados no Node.js moderno, por que o runner nativo ('node --test') é uma boa escolha?",
        "back": "Zero dependências (não precisa de Jest, Vitest ou compilações pesadas no package.json), inicialização quase instantânea e suporte nativo ao TypeScript a partir do Node.js 22.6+ via '--experimental-strip-types'.",
        "tags": "testes nodejs ferramentas"
    }
]


def export_anki_csv(output_dir: Path | None = None) -> Path:
    if output_dir is None:
        output_dir = Path("flashcards")
    output_dir.mkdir(parents=True, exist_ok=True)
    target_file = output_dir / "code_sensei_anki.csv"

    with open(target_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        # Cabeçalho para Anki
        writer.writerow(["#separator:Comma", "", ""])
        writer.writerow(["#html:false", "", ""])
        writer.writerow(["#tags column:3", "", ""])
        writer.writerow(["Frente", "Verso", "Tags"])

        for card in FLASHCARDS:
            writer.writerow([card["front"], card["back"], card["tags"]])

    return target_file


def start_anki_export():
    print("\n" + bold(magenta("==========================================================")))
    print(bold(magenta("    📇 EXPORTADOR DE FLASHCARDS DO SENSEI PARA ANKI 📇    ")))
    print(bold(magenta("==========================================================")))
    print(dim("Gera baralho de repetição espaçada com 20 modelos mentais fundamentais.\n"))

    arquivo = export_anki_csv()
    print(f" {bold(green('✓'))} Arquivo gerado com sucesso em: {bold(cyan(str(arquivo)))}")
    print(f" {bold(green('✓'))} Total de cartões exportados: {bold(yellow(str(len(FLASHCARDS))))}")

    print("\n" + bold(cyan("Como importar no seu Anki (Desktop ou AnkiDroid / AnkiMobile):")))
    print(f" 1. Abra o Anki e clique em {bold('Arquivo -> Importar')}.")
    print(f" 2. Selecione o arquivo: {bold(str(arquivo))}")
    print(f" 3. Tipo de arquivo: {yellow('Texto separado por vírgula (.csv)')}")
    print(f" 4. Mapeamento de campos:")
    print(f"    • Campo 1 -> {cyan('Frente (Front)')}")
    print(f"    • Campo 2 -> {cyan('Verso (Back)')}")
    print(f"    • Campo 3 -> {cyan('Etiquetas (Tags)')}")
    print(f" 5. Clique em {bold('Importar')} e revise 5 a 10 cartões por dia!\n")
