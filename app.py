from flask import Flask,jsonify, Response, request
import requests
import csv
import io

app = Flask(__name__)
RICK_API_BASE = "https://rickandmortyapi.com/api/character"
TARGET_COUNT = 50

def fetch_characters(limit=TARGET_COUNT, start_page=1):
  
    resultados = []
    current_page = start_page
    #url = RICK_API_BASE
    url = f"{RICK_API_BASE}?page={current_page}"

    while len(resultados) < limit and url:
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Erro ao buscar dados: {response.status_code}")
            break

        data = response.json()
        personagens = data.get("results", [])

        for p in personagens:
            resultados.append({
                "id": p.get("id"),
                "name": p.get("name"),
                "status": p.get("status"),
                "species": p.get("species"),
                "type": p.get("type", ""), 
                "gender": p.get("gender")
            })
            
            if len(resultados) >= limit:
                break

        url = data.get("info", {}).get("next")
        current_page += 1

    return resultados[:limit]

def generate_csv(personagens):
    buffer = io.StringIO()
    writer = csv.writer(buffer, delimiter=';')
    writer.writerow(["id","name","status","species","type","gender"])
    for p in personagens:
        writer.writerow([p.get("id"), p.get("name"), p.get("status"), p.get("species"), p.get("type"), p.get("gender")])
    return buffer.getvalue()


@app.route("/characters", methods=["GET"])
def characters_json():
    limit = int(request.args.get("limit", TARGET_COUNT))
    page = int(request.args.get("page", 1))

    characters = fetch_characters(limit=limit, start_page=page)

    return jsonify(characters)

@app.route("/characters/csv")
def characters_csv():
    csv_text = generate_csv(fetch_characters())
    return Response(csv_text, mimetype="text/csv", headers={"Content-Disposition":"attachment;filename=personagens.csv"})


if __name__ == "__main__":
    app.run(debug=True, port=8000)