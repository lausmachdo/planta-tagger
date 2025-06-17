import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import io
import fitz
from main import app


def create_pdf_with_texts(text_list):
    doc = fitz.open()
    for text in text_list:
        page = doc.new_page()
        page.insert_text((72, 72), text)
    pdf_bytes = doc.write()
    doc.close()
    return io.BytesIO(pdf_bytes)


def test_identificar_plantas_detects_keywords():
    client = app.test_client()
    pdf_file = create_pdf_with_texts([
        "Texto generico",
        "Projeto de garagem"
    ])
    data = {"pdf": (pdf_file, "test.pdf")}
    response = client.post(
        "/identificar_plantas",
        data=data,
        content_type="multipart/form-data",
    )
    assert response.status_code == 200
    assert response.get_json() == [
        {"pagina": 1, "tipo_detectado": "desconhecido"},
        {"pagina": 2, "tipo_detectado": "garagem"}
    ]

