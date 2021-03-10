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

![Fluxo Algortimo](/resource/Image/fluxo_algoritmo.png)

## Problema Proposto
O algoritmo deve ser capz de minimizar o valor da função a seguir através do parametro X.

![Função](/resource/Image/eq_problem.png)

A imagem a seguir atras a representação grafica da função exposta.

![Grafico Funcao](/resource/Image/graph_function.png)

## Solução

### Linguagem Utilizada

Para a solução do problema proposto foi utilizada a linguagem Python, versão 3.8.7.

### Execução Codigo

O codigo foi criado utilizando suas informações de ambiente (tamanho de população, metricas e etc) utilizando um arquivo de constantes ```src/utils/constants.py```, desse modo a execução do codigo ocorre de maneira simplicada, necessario estar apenas na pasta raiz, fora da pasta src, e executar o comando na imagem abaixo

![Execução Codigo](/resource/Image/code_execute.png)

#### Alteração de Parametros

Os parametros utilizados em cada uma das funções requisito para o algortimo genetico ([requisitos](https://github.com/elimarmacena/genetic_algorithm_minimize#o-algoritmo)) pode ser alteradas no arquivo ```src\utils\constants.py```, alem desses parametros, tambem é possivel alterar o tamanho da população e tambem o seed utilizado para os numeros randomicos.

### Saida Esperada

A execução do presente codigo resulta em 2 tipos de saidas, ambos os tipos estaram disponibilizadas na pasta ```output```. Primeiro teremos um arquivo do tipo csv com a medida das dez execuções de cada intervalo de geração solicitada, depois teremos a saida para cada execução realiazada em uma geração, exemplo: ```10gen_it1_gen1.csv```. 

### Implementação

#### Indivíduo (Subject)

Cada indivíduo presente na população é representado por um objeto do tipo **Subject**, como é mostrado na imagem a seguir, esse objeto possui 4 atributos, todos eles calculados no momento de sua criação.

![Indivíduo da População](/resource/Image/subject_class.png)

O atributo **bit_list** é a representação binaria de tal indivíuo, em nossa aplicação esse atributo é criado de maneira aleatoria, é feito o uso de uma função para a tal criação, tendo o resultado esse valor é informado no momento da criação do objeto **Subject**. Conhecendo o atributo **bit_list** é realizado a atribuição dos demais atributos, **value** é determinado através de uma conversão simples de valores binarios para valor decimal, já **x_value** é obtido utilizando o resultado de **value** atrelado à uma expressão matematica, tal expressão sera exposta a seguir. Já o valor de **fitness** é obtido através da substituição do x na função apresentada no problema pelo o valor presente em **x_value**.

![Expressão X](/resource/Image/eq_x.png)

Onde β representa o numero de bits presentes no atributo **bit_list**.

#### Geração (Lab)

A representação da população no presente codigo vem através da classe Lab, alem de trazer o conceito de população para o codigo, a classe também contem os manipuladores necessarios para o desenvolvimento de um algoritmo genetico, sendo assim a classe nucleo da solução.

A classe apresenta 6 atributos, mas muitos desses atributos são gerados através de uma cadeia de execução. Primeiro temos **population_size**, esse atributo guarda o tamanho da população, ou seja, o numero de indivíduos que fazem parte de uma população.

Ao instanciarmos a classe, automaticamente é atribuido um valor para o atributo **init_population**, população inicial, essa população é gerada por meio de valores randomicos no array binario de representação do individuo (classe Subject). Temos também o atributo **current_population**, esse atributo irá manter as gerações correntes a cada passo dado na criação de uma nova população.

Os demais atributos mostrados na imagem a seguir são gerados por meio de chamada de metodos da propria classe, que seraão explicados melhor mais a frente.

![População e Operadores](/resource/Image/lab_class.png)

##### Seleção

O problema proposto foi resolvido através de uma abordagem de seleção chamada campeonato, a sua ideia é bem simples, o numero de "rounds" é equivalente ao tamanho da população, neses rounds são selecionados um numero N de individuos que irão "batalhar" entre si, o individuo que melhor se sair nessa batalha irá permanecer na população.

O conceito de melhor individuo pode variar por round, nem sempre o melhor valor significa o mais apto para população, as vezes o pior resultado pode ser mais interessante. Essa abordagem também nos auxilia evitar uma construção de população com os melhores resultados e assim acarretando um cenario de maximos globais e diminuindo a variedade da população.

A implementação desse metodo no presente codigo pode ser visto a seguir.

![Seleção de Indivíduos](/resource/Image/selection_method.png)

##### Crossover

Apos selecionados os individuos, partimos para a etapa de crossover, nessa etapa os inidividuos passam por um "novo processo de seleção" para estabelecer se sera misturada as informações de dois indivíduos ou não.

Essa mistura pode ocorrer a partir de diferentes pontos do array de bits de um indivíduo, na solução desenvolvida foi utilizado a partição de 1 ponto, dessa maneira nós temos 50% de informação de cada individuo que foi selecionado para a mistura de informação. Essa mistura ocorre a partir de um determinada porcentagem estipulada, ou seja existe N% de dois individuos se misturares e gerar um novo.

A implementação dessa fusão de informações é apresentada na figura a seguir e como pode ser visto, é utilizado os valores presentes no atributo **selected_population**, que é o atributo que mantei a seleção realizada na [etapa de selação](https://github.com/elimarmacena/genetic_algorithm_minimize#sele%C3%A7%C3%A3o) dos indivíduos.

![Crossover de Indivíduos](/resource/Image/crossover_method.png)

##### Mutação

Visando manter o estado de variedade em uma população, os algoritmos geneticos fazem uso de mutação. Essa mutação nada mais é do que a alteração de valores presentes no array de representação de um indivíduo, assim como o crossover, essa abordagem precisa de uma determinada porcentagem para perfomar a mutação.

Em nosso codigo, como trabalhamos com valores binarios no array de representação do individuo, a mutação trata apenas de uma inversão de bit. A implementação desse metodo é apresentado na imagem a seguir, cada bit do individuo deve ser analisado em uma porcentagem X de alteração, sendo assim possivel haver apenas um bit alterado em todo o array do individuo.

![Mutação de Indivíduos](/resource/Image/mutation_method.png)

##### Nova Geração
Apos todos os processamentos em cima de uma população, o algoritmo genetico deve dar origem a uma nova população, essa nova população pode ser composta de difrentes maneiras, mas na solução proposta foi feito o uso de elitismo.

A abordagem de elitismo corre quando uma parcela X dos melhores individuos geração base, antes dos processamentos, é mantida para a nova geração e então afeita a agregação dos resultados de processamento juntamente com os dados "limpos".

No presente codigo é trabalhado uma população de tamanho 10, para o nosso elitismo foi estipulado 10% da população base deve ser mantida na proxima geração, ou seja 1 individo, e os outros 9 individuos devem ser selecionados após o processamento da população base, no codigo optou-se por pegar os 9 melhores fitness da população. A implementação pode ser vista na imagem a seguir.
![Nova Geração](/resource/Image/newgen_method.png)

#### Arquivo da Aplicação(Main)

O arquivo de execução do codigo, main, possui uma construção simples, onde é seguido apenas a ordem dos requisitos estabelecidos para o funcionamento de um algoritmo genetico.

A imagem abaixo traz a função de execução, nesse codigo podemos destacar o variavel **generation_life_list**, onde temos uma lista contendo o tempo de vida (total maximo gerações) que uma população deve ter. Após isso trazemos o destaque para o loop baseado em **const.EXECUTIONS**, valor utiliado para estabelecer a quantidade de vezes que um mesmo ciclo de vida deve ser executado, esse valor tambem pode ser alterado no arquivo de constantes, juntamente com os demais valores presentes no arquivo.

![Arquivo da Aplicação](resource/Image/main_method.png)

Levantado os ponto iniciais, a ordem de execução é bem simples, tarefas basicas de algoritmo genetico ocorrem e suas saidas sao salvas em arquivos. Vale salientar que gerações escritas no arquivo com o valor -1 representam a geração inicial.


## Resultados

Apesar de toda teoria por traz do funcionamento dos algoritmos geneticos, as saidas encontradas no problema proposto foram relativamente simples e faceis de levantar uma analise breve.

O pico de melhores fitness foram encontrados nas gerações 9 e 10, utilizando os ciclos de vida de 10 e 20 gerações. Os melhores resultados de cada interação de cada ciclo de vida pode ser encontrado em [Ciclo 10](/outputs/lifetime10_best_entities.txt) e [Ciclo 20](/outputs/lifetime20_best_entities.txt). Vale lembrar que os valores alcançados podem variar com o uso de seed para os numeros randomicos.
