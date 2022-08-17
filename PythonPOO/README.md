# Exercícios de Python POO - PS Nautilus

Esse README foi criado no intuito concentrar em um único arquivo, as explicações dos programas utilizando Python Básico
(Obs: Todos os códigos foram comentados e as explicações aqui presentes foram retiradas deles)

### Implemente um modelo que descreva os AUVs da UFRJ Nautilus

Requerimentos 

Deve conter os atributos: número de thursters, lista com sensores,
ano de construção, nome do veículo, e no mínimo, mais 1 atributo de
livre escolha 
Deve conter métodos para:
Exibir todos os AUVs em tabela
Exibir os robôs individulmente
Rankear os robôs do mais novo para o mais antigo
Deve conter outro método de livre escolha

EXPLICAÇÃO:
Criei a classe AUV e fiz sua respectiva instanciação quatro vezes.

Feito isso, peguei os objetos criados e armazenei em uma lista. Assim,
dei início ao chamamento das funções criadas.

A função exibeEmTabela() foi bem simples de ser desenvolvida, bastou
criar um laço for e printar com as devidas formatações.
Para exibir individualmente, foi basicamente a mesma lógica, porém com
a diferença que retirei as vírgulas e colchetes da lista que armazenava
os sensores de cada AUV.

Agora, para o rankeamento por idade, pensei em usar o método __gt__, mas
acabei optando por usar o método sort por achar mais simples. Para evitar
repetição de código,

Sobre a função livre, fiz a rankearPorVelocidade, e usei a mesma lógica da
função anterior.