# Exercícios de ROS - PS Nautilus

Esse README foi criado no intuito concentrar em um único arquivo, as explicações do que foi desenvolvido usando ROS


## Enunciado:
Um robô possui um sensor de velocidade que fornece os vetores de velocidade linear e angular com suas
componentes x, y e z.
Crie um pacote contendo um publisher que publica esses dados e um subscriber que escuta esse tópico,
calcula o módulo dos vetores e publica os resultados em tópicos separados.

## Observações:
Para poder subir essa atividade, tive que retirar o arquivo CMakeList, talvez isso possa afetar de alguma forma o funcionamento.
Particularmente, tive bastante dificuldade em fazer essa atividade. Por conta disso, optei por aproveitar os arquivos talker_ex e 
listener_ex desenvolvidos pelo Wagner no decorrer da aula de ROS básico. Não ficou exatamente da forma que eu queria, mas optei
por entregar da forma que foi possível. 