from flask import Flask, request, jsonify
import fitz  # PyMuPDF

app = Flask(__name__)

TIPOS_CHAVE = {
    "térreo": "terreo",
    "pavimento térreo": "terreo",
    "pavimento 1": "pavimento1",
    "pavimento superior": "pavimento1",
    "pavimento 2": "pavimento2",
    "situação": "situacao",
    "corte": "corte",
    "cobertura": "cobertura",
    "caixa d'água": "caixa_dagua",
    "barrilete": "barrilete",
    "garagem": "garagem"
}

@app.route("/identificar_plantas", methods=["POST"])
def identificar_plantas():
    if "pdf" not in request.files:
        return jsonify({"erro": "PDF não enviado"}), 400

    file = request.files["pdf"]
    doc = fitz.open(stream=file.read(), filetype="pdf")
    resultado = []

    for i, page in enumerate(doc):
        texto = page.get_text().lower()
        tipo_detectado = None
        for chave, tipo_padrao in TIPOS_CHAVE.items():
            if chave in texto:
                tipo_detectado = tipo_padrao
                break

        resultado.append({
            "pagina": i + 1,
            "tipo_detectado": tipo_detectado or "desconhecido"
        })

    return jsonify(resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

