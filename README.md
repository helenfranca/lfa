# Conversão Mealy e Moore
Trabalho desenvolvido como uma atividade na disciplina de Linguagens Formais e Autômatos do curso de Sistemas de Informações ofertado pelo IFES - Campus Serra foi implementado pela aluna Helen França e o aluno Jadson Pereira. A atividade consiste em converter uma máquina de Mealy para uma máquina de Moore ou vice-versa.

# Máquina de Mealy
A máquina de mealy foi criada por George H. Mealy. <br>
"Em ciências da computação, uma máquina de Mealy é uma máquina de estado finito que produz um resultado (saída de dados) baseando-se no estado em que se encontra e na entrada de dados. Isto significa que o diagrama de estados irá incluir tanto o sinal de entrada como o de saída para cada vértice de transição. Em contraste, a saída de uma máquina de Moore depende apenas do estado actual da máquina, sendo que as transições não possuem qualquer sinal em anexo. Mesmo assim, por cada máquina de Mealy existe uma máquina de Moore equivalente cujos estados consistem na união dos estados da máquina de Mealy e o produto cartesiano dos estados da máquina de Mealy com o alfabeto de entrada de sinais" Fonte:[https://pt.wikipedia.org/wiki/M%C3%A1quina_de_Mealy.] A máquina de mealy é aplicada em leitor de códigos de barra, Semáforos, máquinas de vendas e relógio com temporizador.<br>

<br>Exemplo de máquina de mealy: <br>
![Alt text](https://github.com/jadsonpp/lfa/blob/master/prints/maqMealy.png)
<br>Represetado em arquivo como: <br> 
![Alt text](https://github.com/jadsonpp/lfa/blob/master/prints/ExMealy.png)

# Máquina de Moore
"Na teoria da computação, uma máquina de Moore é um autômato de estado finito onde as saídas são determinadas pelo estado corrente apenas (e não pela entrada). O diagrama de estado para uma máquina de Moore inclui um sinal de saída para cada estado." Fonte: [https://pt.wikipedia.org/wiki/M%C3%A1quina_de_Moore]<br>
Exemplo de máquina de Moore:
![Alt text](https://github.com/jadsonpp/lfa/blob/master/prints/maqMoore.png)
<br>Represetado em arquivo como: <br>
![Alt text](https://github.com/jadsonpp/lfa/blob/master/prints/exMoore.png)

# Estrutura do código

Biblioteca com as principais funções para a conversão das máquinas, entre elas estão a função de tratar S-Expressions e fazer a conversão das máquinas de Mealy pra Moore e de Moore pra Mealy.
``` 
    conversorBib.py
```
 Arquivo principal que realiza a chamada da função de conversão.

```
    conversor.py
```
 

  ```Nome e modo de uso do programa desenvolvido; ```

# Procedimento para compilação

