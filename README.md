# Planta Tagger

This is a small Flask service that inspects PDF architectural plans and
attempts to identify the type of each page (e.g. floor levels, cuts,
situational plans). The service is intended to be deployed using
[Render](https://render.com) as defined in `render.yaml`.

## Running locally

Install the requirements and run `main.py`:

```bash
pip install -r requirements.txt
python main.py
```

The API will be available on port `5000` by default.

## Endpoint: `/identificar_plantas`

Send a `POST` request with the PDF file in the `pdf` form field. The
endpoint returns a JSON array where each element describes a page and the
detected type.

Example using `curl`:

```bash
curl -X POST -F pdf=@example.pdf http://localhost:5000/identificar_plantas
```

A successful response looks like:

```json
[
  {"pagina": 1, "tipo_detectado": "terreo"},
  {"pagina": 2, "tipo_detectado": "cobertura"}
]
```
