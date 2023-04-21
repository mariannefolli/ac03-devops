from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    qtdTotal = 100
    primos = "1,2,"
    candPrimo = 3
    qtdEncontrados = 2
    ehPrimo = 1

    while qtdEncontrados < qtdTotal:
        for i in range (2, candPrimo):
            if candPrimo % i == 0:
                ehPrimo = 0
                break
        if ehPrimo == 1:
            primos = primos + str(candPrimo)+","
            qtdEncontrados += 1
            if qtdEncontrados % 10 == 0:
                primos += "<br>"
        ehPrimo = 1
        candPrimo += 1

    return primos

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)