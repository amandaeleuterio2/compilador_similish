# Compilador Simlish
Compilador Simlish usado para programação de controladores de ambiente, que são dispositivos eletrônicos responsáveis pelo controle de sistemas de ar-condicionado, aquecimento, ventilação e refrigeração em edifícios comerciais e residenciais.

## Qual a  ligação entre um compilador e um controlador de ambiente?
Um controlador de ambiente é um dispositivo eletrônico que é programado para coletar dados ambientais, processá-los e controlar equipamentos para manter as condições ambientais ideais.
Um compilador é um software que é usado para traduzir o código-fonte de um programa em uma linguagem de programação de alto nível para uma linguagem de máquina que o computador possa entender e executar.
**A ligação está entre utilizar o compilador para escrever e compilar um programa que será carregado em um microcontrolador.**

## Análise Léxica
Análise léxica é a primeira etapa do processo de compilação e seu objetivo é dividir o código fonte em símbolos léxicos em que se verifica se os nomes das entidades estão corretos, preparando-o para a análise sintática.

* Ler o arquivo com o programa fonte
* Extração e classificação dos símbolos léxicos que compõem o programa fonte
* Recuperação de erros léxicos, gerados por sequências de caracteres que não formam símbolos léxicos
* Eliminação de caracteres brancos, como espaços em branco, tabulação e mudanças de linha, e comentários

Itens:
* Identificadores: palavras utilizadas para nomear entidades do programa, como variáveis, funções, métodos, classes, módulos, etc.
* Literais: sequência de caracteres que representa uma constante, como um número inteiro, ponto flutuante, um caracter, uma string, um valor verdade (verdadeiro ou falso), etc.
* Sinais de pontuação: sequências de caracteres que auxiliam na construção das estruturas do programa.
* Palavras chaves: palavras usadas para expressar estruturas da linguagem. Geralmente são reservadas.

## Análise Sintática
Analisa-se se os comandos estão corretos. Chama a verificação da frase. Aqui, não basta escrever as palavras corretamente, importando também a ordem em que elas aparecem. 
O analisador sintático, ao verificar uma “frase”, aciona o analisador léxico, que retorna o tipo de token, ou uma lista de tokens, e, a partir do fluxo recebido, inicia a análise da produção
