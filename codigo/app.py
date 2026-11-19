from flask import Flask, render_template, request

app = Flask(__name__)

NUM_ALUNOS = 3
NUM_NOTAS = 3


def ler_numero(campo, tipo, rotulo):
    """Lê um campo do formulário e converte para int/float.
    Aceita vírgula decimal (7,5) e gera mensagens de erro amigáveis."""
    valor = (request.form.get(campo) or "").strip().replace(",", ".")
    if not valor:
        raise ValueError(f"Preencha {rotulo}.")
    try:
        return tipo(valor)
    except ValueError:
        raise ValueError(f"Valor inválido em {rotulo}: '{valor}'.")


def classificar(media):
    if media >= 7:
        return "FOI APROVADO", "aprovado"
    if media >= 5:
        return "FICOU EM RECUPERAÇÃO", "recuperacao"
    return "FOI REPROVADO", "reprovado"


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None

    if request.method == "POST":
        try:
            alunos = []

            for i in range(1, NUM_ALUNOS + 1):
                nome = (request.form.get(f"nome{i}") or "").strip()
                if not nome:
                    raise ValueError(f"Informe o nome do aluno {i}.")

                idade = ler_numero(f"idade{i}", int, f"a idade de {nome}")
                if not (14 <= idade <= 18):
                    raise ValueError(f"O aluno {nome} deve ter entre 14 e 18 anos.")

                notas = []
                for n in range(1, NUM_NOTAS + 1):
                    nota = ler_numero(f"nota{i}_{n}", float, f"a nota {n} de {nome}")
                    if not (0 <= nota <= 10):
                        raise ValueError(f"As notas do aluno {nome} devem estar entre 0 e 10.")
                    notas.append(nota)

                # Arredonda ANTES de classificar: evita que erros de ponto
                # flutuante (ex.: 6.999999999) mostrem 7.0 mas reprovem na recuperação
                media = round(sum(notas) / NUM_NOTAS, 2)
                situacao, status_class = classificar(media)

                alunos.append({
                    "nome": nome,
                    "idade": idade,
                    "media": media,
                    "situacao": situacao,
                    "status_class": status_class,
                })

            resultado = alunos

        except ValueError as e:
            erro = str(e)

    return render_template("index.html", resultado=resultado, erro=erro)


if __name__ == "__main__":
    # debug=True só em desenvolvimento
    app.run(debug=True)