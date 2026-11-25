# EduPortal - Gestão de Notas

## Sobre o projeto

O EduPortal é um sistema escolar desenvolvido em Python com Flask e HTML. Seu objetivo é cadastrar informações de estudantes, registrar notas, calcular médias finais e apresentar a situação acadêmica de cada aluno.

O projeto foi desenvolvido para a Situação de Aprendizagem nº 1, na Unidade Curricular Programação de Aplicativos.

## Funcionalidades

- Cadastro de 3 estudantes.
- Registro de nome e idade.
- Registro de 3 notas por estudante.
- Validação das idades entre 14 e 18 anos.
- Validação das notas entre 0 e 10.
- Cálculo automático da média final.
- Classificação de aprovação, recuperação ou reprovação.
- Mensagens de erro para entradas inválidas.

## Regras de classificação

O sistema calcula a média das três notas de cada estudante.

- **Aprovado:** média igual ou superior a 7,0.
- **Recuperação:** média igual ou superior a 5,0 e inferior a 7,0.
- **Reprovado:** média inferior a 5,0.

As notas devem estar entre 0 e 10, e as idades aceitas pelo sistema estão entre 14 e 18 anos.

## Tecnologias utilizadas

- Python
- Flask
- HTML
- CSS

## Organização dos arquivos

```text
codigo/
├── app.py
└── templates/
    └── index.html
```

- `app.py`: responsável pelo processamento dos dados, validações, cálculo das médias e classificação.
- `templates/index.html`: responsável pela interface do sistema, formulário de cadastro e apresentação dos resultados.

## Como executar o projeto

### 1. Instalar o Flask

No terminal do VS Code, execute:

```bash
pip install flask
```

### 2. Acessar a pasta do código

```bash
cd codigo
```

### 3. Executar a aplicação

```bash
python app.py
```

### 4. Abrir no navegador

Acesse o endereço:

```text
http://127.0.0.1:5000
```

## Testes

Foram definidos testes para verificar o funcionamento das validações e classificações do sistema.

| Teste | Entrada | Resultado esperado |
|---|---|---|
| Nota mínima | 0 | Aceita |
| Nota máxima | 10 | Aceita |
| Nota negativa | -1 | Rejeitada |
| Nota acima do limite | 11 | Rejeitada |
| Entrada não numérica | Letras | Mensagem de erro |
| Campo vazio | Sem preenchimento | Mensagem de erro |
| Média 4,99 | 4,99 | Reprovado |
| Média 5,00 | 5,00 | Recuperação |
| Média 6,99 | 6,99 | Recuperação |
| Média 7,00 | 7,00 | Aprovado |

## Desenvolvedor

**Nome:** Diogo Victor Peschel Ferreira  
**Turma:** Desenvolvimento de Sistemas  
**Unidade Curricular:** Programação de Aplicativos  
**Projeto:** EduPortal - Gestão de Notas