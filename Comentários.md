
# Devolutiva formativa — Atividade 01 da SA

**Estudante:** Diogo  
**Turma:** Rio Negrinho — Tarde  
**Unidade Curricular:** Programação de Aplicativos  
**Projeto escolhido:** Escola — Boletim e cálculo de médias  
**Referência:** Situação de Aprendizagem nº 1 — *Da Ideia ao Código*

## O que você já conseguiu desenvolver

Diogo, você construiu uma primeira solução para um sistema escolar que recebe informações de três estudantes, trabalha com três notas por estudante, calcula médias e apresenta situações acadêmicas. O código demonstra a utilização de entradas, condições, cálculos e funções para validar informações.

Pontos positivos identificados:

- Criou uma função **`pedir_nota()`**, utilizada para trabalhar com notas dentro do intervalo de **0 a 10**.
- Criou uma função **`pedir_idade()`**, que verifica a idade dentro da faixa de **14 a 18 anos** definida no seu programa.
- Aplicou **entrada de dados e conversões numéricas** para processar informações escolares.
- Implementou o **cálculo de médias** a partir de três notas por estudante.
- Utilizou **condicionais** para determinar as situações de aprovação, recuperação ou reprovação.
- Conseguiu representar o processamento de informações de **três estudantes** em uma mesma execução.

## O que precisa ser corrigido

### 1. Corrigir o nome exibido para o terceiro estudante

Na apresentação dos resultados do terceiro estudante, o programa utiliza a variável do nome do segundo estudante (`nome2`). Isso faz com que o boletim apresente um nome incorreto, mesmo quando o cálculo das notas corresponde ao terceiro cadastro.

**Como melhorar:** utilizar a variável associada ao estudante correto em cada resultado. Depois, testar com três nomes bem diferentes para identificar facilmente qualquer troca de informações.

### 2. Tratar erros nas conversões para inteiro

Em trechos do programa, a conversão por `int()` ocorre sem um `try/except`. Se o usuário digitar letras ou um campo vazio nesses pontos, a execução pode ser interrompida com `ValueError`.

**Como melhorar:** realizar as conversões em funções de leitura que tratem entradas inválidas, informem o problema e solicitem um novo valor. Verificar também se o valor recebido respeita o intervalo definido.

### 3. Reduzir a repetição do cadastro e do cálculo

O fluxo de leitura e processamento das informações dos três estudantes repete instruções semelhantes. Isso aumenta o tamanho do programa e contribui para erros de cópia, como a utilização de `nome2` na apresentação do terceiro estudante.

**Como melhorar:** criar uma função reutilizável para cadastrar e calcular os resultados de **um estudante**. Depois, utilizar um `for` para repetir esse processo três vezes e armazenar cada registro em uma lista.

## Oportunidades de melhoria

### 4. Organizar os dados com listas e dicionários

Variáveis separadas para cada estudante tornam mais difícil aumentar o número de cadastros e consultar resultados posteriormente.

**Como melhorar:** representar cada estudante por um dicionário com campos como `nome`, `idade`, `notas`, `media` e `situacao`, armazenando os registros em uma lista. Isso permitirá percorrer e apresentar os boletins sem repetir o mesmo bloco de código.

### 5. Centralizar as regras de média e situação

O cálculo da média e a definição da situação escolar devem seguir as mesmas regras para todos os estudantes.

**Como melhorar:** criar funções como `calcular_media(notas)` e `definir_situacao(media)`. Assim, uma alteração na regra será realizada em um único lugar.

### 6. Revisar os limites das validações

As funções de nota e idade apresentam uma preocupação importante com a consistência dos dados. Entretanto, a faixa de 14 a 18 anos precisa estar claramente relacionada aos requisitos do sistema escolar proposto.

**Como melhorar:** documentar por que essa faixa foi escolhida e verificar se ela atende ao público previsto. Testar especialmente os valores limites: 0 e 10 para notas, 14 e 18 para idades, além dos valores imediatamente fora dessas faixas.

### 7. Melhorar a documentação e a apresentação dos resultados

A separação de tarefas em funções é um bom começo, mas as regras e a forma de executar o programa precisam ficar claras.

**Como melhorar:** adicionar docstrings curtas às funções, padronizar os textos dos boletins e atualizar o README com as funcionalidades e os passos de execução.

## Testes recomendados

1. Informar três estudantes com nomes diferentes e conferir cada boletim.
2. Verificar se o terceiro estudante aparece com o nome correto.
3. Testar notas nos limites 0 e 10.
4. Tentar informar notas menores que 0, maiores que 10 e entradas não numéricas.
5. Testar idades 14 e 18 e valores fora do intervalo definido.
6. Digitar letras ou deixar em branco os campos convertidos para inteiro.
7. Conferir as médias com valores cujo resultado seja decimal.
8. Verificar cada situação acadêmica nas fronteiras entre as faixas definidas no programa.
9. Refazer o cadastro após a modularização, confirmando que os três estudantes ainda são processados corretamente.

## Prioridades para a próxima versão

1. **Corrigir a troca de nome no boletim do terceiro estudante.**
2. **Tratar conversões numéricas inválidas com `try/except`.**
3. **Substituir os blocos repetidos por funções e um laço de repetição.**
4. **Organizar os registros em uma lista de dicionários.**
5. **Centralizar os cálculos e registrar testes dos valores limites.**

## Mensagem final

Diogo, você já demonstrou compreensão de **entrada de dados, funções, validação por intervalos, condicionais e cálculo de médias**. Esses conhecimentos são importantes para construir um sistema escolar mais completo.

Seu próximo desafio é reduzir a repetição, evitar trocas de variáveis e impedir que entradas inválidas interrompam a aplicação. **Comece corrigindo o resultado do terceiro estudante e, depois, transforme o cadastro repetido em uma função reutilizável.** Essa evolução deixará o código mais claro, mais fácil de testar e preparado para receber novos estudantes.
