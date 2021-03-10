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

PLACE HOLDER --- COLOCAR INFORMAÇÃO DE EXECUCAO

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

![Seleção de Indivíduos](/resource/Image/selection_method.png)

##### Crossover

![Crossover de Indivíduos](/resource/Image/crossover_method.png)

##### Mutação

![Mutação de Indivíduos](/resource/Image/mutation_method.png)

##### Nova Geração

![Nova Geração](/resource/Image/newgen_method.png)

#### Arquivo da Aplicação(Main)