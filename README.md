# Encontrando a Árvore Geradora Mínima (AGM) usando Exclusão Reversa

Este README descreve um código Python que encontra a Árvore Geradora Mínima (AGM) de um grafo não direcionado usando o algoritmo de exclusão reversa. A AGM é uma árvore que conecta todos os vértices do grafo com o menor peso possível. O algoritmo de exclusão reversa é uma abordagem eficiente para encontrar a AGM.

## Descrição do Código

O código fornece uma implementação Python do algoritmo de exclusão reversa para encontrar a AGM de um grafo. Ele é dividido em três partes principais:

1. **Classe Graph:** A classe Graph é usada para representar o grafo e inclui métodos para adicionar arestas, verificar a conectividade do grafo e encontrar a AGM usando exclusão reversa.
2. **Métodos da Classe Graph:**

**__init__(self, v):** Inicializa o objeto grafo com um número específico de vértices **(v)** e cria a estrutura de dados necessária para representar o grafo.

**addEdge(self, u, v, w):** Adiciona uma aresta ao grafo com peso **w** entre os vértices **u** e **v**, considerando que o grafo é não direcionado.

**dfs(self, v, visited):** Implementa uma busca em profundidade (DFS) para verificar se o grafo é conectado a partir do vértice **v**.

**connected(self):** Verifica se o grafo é conectado, ou seja, se todos os vértices são alcançáveis a partir de um vértice de partida. Utiliza o método **dfs**.

**reverseDeleteMST(self):** Implementa o algoritmo de exclusão reversa para encontrar a AGM. Ordena as arestas em ordem crescente de peso e, em seguida, itera sobre elas na ordem inversa. Para cada aresta, verifica se sua remoção deixaria o grafo desconectado. Se não, a aresta é removida, caso contrário, é mantida.

3. **Código do Motorista:** No código do motorista, um grafo específico é criado com 9 vértices e todas as arestas são adicionadas com seus respectivos pesos. Em seguida, o método **reverseDeleteMST** é chamado para encontrar a AGM usando o algoritmo de exclusão reversa. As arestas que compõem a AGM e o peso total da AGM são impressos como resultado.


## Como Usar o Código

1. Certifique-se de ter o Python 3 instalado no seu sistema.

2. Copie o código Python fornecido para um arquivo com a extensão .py ou use um ambiente Python, como Jupyter Notebook, para executar o código.

3. Execute o código. As arestas que compõem a Árvore Geradora Mínima (AGM) e o peso total da AGM serão impressos na saída.

4. Você pode personalizar o grafo editando o código do motorista para adicionar ou modificar vértices e arestas, conforme necessário.

## Exemplo de Execução

Suponha que você execute o código do motorista conforme fornecido no README. O resultado da execução pode ser semelhante ao seguinte:

``` bash
Edges in MST
( 6, 7 )
( 2, 8 )
( 5, 6 )
( 4, 5 )
( 9, 4 )
( 10, 3 )
( 11, 1 )
O peso total da MST é 47
```
Isso mostra as arestas que compõem a AGM e o peso total da AGM.

## Contribuições
Este código é uma implementação eficiente para encontrar a Árvore Geradora Mínima usando o algoritmo de exclusão reversa. Se você encontrar problemas, erros ou desejar contribuir com melhorias, sinta-se à vontade para abrir uma issue ou um pull request neste repositório.
