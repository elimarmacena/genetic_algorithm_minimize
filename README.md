# Genetic Algorithm Function Minimize

## O Algoritmo
Os algoritmos geneticos se enquadram no ramo da computação evolucionária (CE), este ramo trabalha na solução de problemas por meio de uma abordagem inspirada em seleção natural, proposta por Darwin.

Algoritmos genéticos (AG) foram expostos John Holland em 1960, inicialmente a ideia foi apresentada para a realização de estudos de adaptação de espceies e seleção natural que ocorre no ambiente, juntamente com a ideia de transpor tais conceitos aos computadores.

Para que seja possivel a implementaçãode um algoritmo génetico é necessario que os sequintes pontos sejam seguidos:
* População inicial com presença de diversidade.
* Método de medição da adaptação de cada indivíduos.
* A presença de um manipulador para que seja possivel combinar indivíduos para a criação de novos indivíduos na população.
* Critério de escolha de permanencia na população e também sua retirada da população.
* A presença de um variante periodico nos indivíduos da população, afim de manter a diversidade e expandir possibilidades.

Aplicando os requisitos expostos, é possivel realizar a construção do algortimo utilizando o fluxo apresentado na imagem a seguir

![Fluxo Algortimo](https://github.com/elimarmacena/genetic_algorithm_minimize/blob/main/resource/Image/fluxo_algoritmo.png)

## Problema Proposto
O algoritmo deve ser capz de minimizar o valor da função a seguir através do parametro X.

### f(x) = cos(x) * x +2

A imagem a seguir atras a representação grafica da função exposta.

![Grafico Funcao](https://github.com/elimarmacena/genetic_algorithm_minimize/blob/main/resource/Image/graph_function.png)
