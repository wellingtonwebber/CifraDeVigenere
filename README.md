<h1 align="center">Cifra de Vigenère</h1>

<p align="center">Trabalho realizado para cadeira de segurança de sistemas do curso de análise e desenvolvimentos de sistemas do IFRS campus Canoas.</p>

<p>A <strong>Cifra de Vigenère</strong> é um método de criptografia que utiliza uma série de diferentes cifras de César com base nas letras de uma palavra-chave. Inventada pelo matemático francês Blaise de Vigenère no século XVI, esta técnica oferece uma forma mais avançada de criptografia do que a cifra de César tradicional.</p>

<h2>Funcionamento</h2>

<p>Na cifra de Vigenère, cada letra da mensagem é substituída por outra letra, dependendo da letra correspondente na palavra-chave. Para cifrar uma mensagem:</p>
    <ol>
        <li>A chave é repetida até ter o mesmo comprimento da mensagem.</li>
        <li>Cada letra da mensagem é deslocada de acordo com a letra correspondente na chave.</li>
    </ol>
<p>Para decifrar, o processo é revertido.</p>
    
<h2>Exemplo</h2>

<p>Suponha que queremos cifrar a mensagem "HELLO" usando a chave "KEY". Repetindo a chave, obtemos:</p>
    <ul>
        <li>Mensagem: <strong>HELLO</strong></li>
        <li>Chave: <strong>KEYKEY</strong></li>
    </ul>
<p>Ao cifrar cada letra, obtemos "OFXOR" como mensagem cifrada.</p>

<h2>Fórmula da Cifra de Vigenère</h2>

<p>A fórmula algébrica para cifrar uma letra <em>P</em> (da mensagem) usando uma letra <em>K</em> da chave é dada por:</p>

<p>C = (P + K) mod 26</p>

<p>Onde:</p>
    <ul>
        <li><em>C</em> é o número correspondente à letra cifrada na tabela de letras do alfabeto (de 0 a 25)</li>
        <li><em>P</em> é o número correspondente à letra da mensagem original na tabela de letras do alfabeto (de 0 a 25)</li>
        <li><em>K</em> é o número correspondente à letra da chave na tabela de letras do alfabeto (de 0 a 25)</li>
        <li><em>mod</em> representa a operação de módulo, ou seja, o resto da divisão.</li>
    </ul>

<p>Para decifrar, a fórmula é:</p>

<p>P = (C - K) mod 26</p>

<h1 align="center">Implementação em Python</h1>

<p>A linguagem escolhida para implementação foi Python. Uma melhoria possível de implementar é que o algoritmo pode realizar a cifra de letras maiusculas e minúsculas, números e alguns caracteres especiais</p>

<p>A string utilizada como alfabeto é "ABCDEFGHIJKLMNOPQRSTUVWYZÁÉÍÓÚÃÂÊÔabcdefghijklmnopqrstuvwxyzáéíóúãâêô:.@#%&*()-à;,?!_-0123456789 "</p>

<p>Certifique-se de que o texto de entrada não possua algum caractere não suportado pelo algoritmo antes de executá-lo. Fique a vontade para adicionar algum caractere que a string não contenha</p>

<h1 align="center">Executando o script</h1>

<p>Para criptografar o arquivo, abra o terminal no local programa e execute o comando a seguir:</p>

```
$ python "vigenere.py" "teste.txt" "chave" "criptografar"
```

<p>Para decriptografar o arquivo, abra o terminal no local programa e execute o comando a seguir:</p>

```
$ python "vigenere.py" "teste_cripto.txt" "chave" "decriptografar"
```

<p>Certifique-se da existência do arquivo .txt no local do script e de usar a mesma chave para criptografar e decriptografar</p>

