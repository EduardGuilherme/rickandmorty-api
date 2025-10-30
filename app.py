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

@app.route("/characters", methods=["GET"])
def characters_json():
    limit = int(request.args.get("limit", TARGET_COUNT))
    page = int(request.args.get("page", 1))

    characters = fetch_characters(limit=limit, start_page=page)

    return jsonify(characters)

if __name__ == "__main__":
    app.run(debug=True, port=8000)