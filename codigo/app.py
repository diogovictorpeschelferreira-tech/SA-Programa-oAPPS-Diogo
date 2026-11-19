from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None

    if request.method == "POST":
        try:
            # Captura os nomes
            nomes = [
                request.form.get("nome1"),
                request.form.get("nome2"),
                request.form.get("nome3")
            ]

            # Captura e valida as idades
            idades = [
                int(request.form.get("idade1")),
                int(request.form.get("idade2")),
                int(request.form.get("idade3"))
            ]

            for i, idade in enumerate(idades):
                if not (14 <= idade <= 18):
                    raise ValueError(f"O aluno {nomes[i]} deve ter entre 14 e 18 anos.")

            # Captura e valida as notas (3 notas por aluno)
            notas = []
            for i in range(3):
                n1 = float(request.form.get(f"nota{i+1}_1"))
                n2 = float(request.form.get(f"nota{i+1}_2"))
                n3 = float(request.form.get(f"nota{i+1}_3"))
                
                for n in [n1, n2, n3]:
                    if not (0 <= n <= 10):
                        raise ValueError(f"As notas do aluno {nomes[i]} devem estar entre 0 e 10.")
                
                notas.append([n1, n2, n3])

            # Cálculo das médias e situações
            alunos_resultado = []
            for i in range(3):
                media = sum(notas[i]) / 3
                if media >= 7:
                    situacao = "FOI APROVADO"
                    status_class = "aprovado"
                elif media >= 5:
                    situacao = "FICOU EM RECUPERAÇÃO"
                    status_class = "recuperacao"
                else:
                    situacao = "FOI REPROVADO"
                    status_class = "reprovado"

                alunos_resultado.append({
                    "nome": nomes[i],
                    "idade": idades[i],
                    "media": round(media, 2),
                    "situacao": situacao,
                    "status_class": status_class
                })

            resultado = alunos_resultado

        except ValueError as e:
            erro = str(e)

    return render_template("index.html", resultado=resultado, erro=erro)

if __name__ == "__main__":
    app.run(debug=True)