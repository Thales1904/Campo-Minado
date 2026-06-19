# Campo Minado em Python

Projeto de um jogo de Campo Minado desenvolvido em Python para execução diretamente no terminal.

## Descrição

O programa gera um campo com dimensões definidas pelo jogador e distribui uma quantidade de bombas também escolhida pelo usuário. O objetivo é revelar todas as posições seguras sem selecionar nenhuma bomba.

O jogo foi desenvolvido utilizando matrizes, estruturas de repetição, condicionais e algoritmos de busca para revelar automaticamente áreas livres do tabuleiro.

## Como funciona

Ao iniciar o jogo, o jogador informa:

* O nome;
* Quantidade de linhas do campo;
* Quantidade de bombas.

Inicialmente, todas as posições do tabuleiro permanecem ocultas, representadas por quadrados. As bombas e os espaços livres não são exibidos ao jogador.

Existe um modo de trapaça que permite visualizar o gabarito completo do campo, incluindo a localização das bombas.

## Regras

As jogadas são realizadas informando a linha e a coluna desejadas em uma mesma linha, separados por espaço.

### Se a posição escolhida contiver uma bomba:

* O jogador perde imediatamente.

### Se a posição escolhida estiver livre:

* Será exibida a quantidade de bombas presentes nas oito posições adjacentes.

### Caso não existam bombas adjacentes:

* As oito posições vizinhas serão reveladas automaticamente.
* Se alguma dessas posições também não possuir bombas ao redor, o processo continuará recursivamente até que toda a região segura seja revelada.

## Condição de Vitória

O jogador vence quando todas as posições livres forem reveladas, restando ocultas apenas as casas que contêm bombas.

## Ferramentas utilizadas

* Python 3
* Matrizes
* Listas
* Funções
* Estruturas de repetição
* Estruturas condicionais

## Execução

```bash
python Campo_Minado.py
```

## Objetivos do Projeto

Este projeto foi desenvolvido para praticar:

* Manipulação de matrizes;
* Lógica de programação;
* Recursão e propagação de áreas vazias;
* Organização de código em funções;
* Desenvolvimento de jogos em terminal.
