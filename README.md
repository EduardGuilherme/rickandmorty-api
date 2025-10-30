
Tecnologias Utilizadas

Python 3.10+

Flask

Requests

CSV

Virtualenv


Clone o repositório
git clone https://github.com/EduardGuilherme/rickandmorty-api.git
cd rickandmorty-api

Criar e ativar o ambiente virtual

python -m venv .venv

No Windows:

.venv\Scripts\activate

No Linux/Mac:

source .venv/bin/activate

Instalar as dependências

pip install flask requests

Rodar o servidor Flask

python app.py


O servidor será iniciado em:

http://localhost:8000

para ver a lista completa 

http://localhost:8000/characters

para ver a lista por paginas 

http://localhost:8000/characters?limit=1&page=1

5️⃣ Gerar o arquivo CSV

Para gerar o arquivo, acesse no navegador:

Cole esse endpoint http://localhost:8000/characters/csv para gerar o arquivo csv

O sistema gera automaticamente um arquivo CSV, conforme demonstrado abaixo:

<img width="751" height="70" alt="Arquivo CSV Gerado" src="https://github.com/user-attachments/assets/e5041dc5-c68d-4f9f-bda4-20caddf40877" />






Resultado do Arquivo CSV

Visualização do conteúdo processado no arquivo CSV:

<img width="700" height="512" alt="Resultado CSV" src="https://github.com/user-attachments/assets/9c016c6c-8ac2-49dd-a5c6-4a4d98ab454c" />

Resultado da Listagem com Paginação

A aplicação também exibe os dados com paginação para melhor navegação e organização dos resultados:

<img width="1294" height="779" alt="Listagem com Paginação" src="https://github.com/user-attachments/assets/1112b206-7bdb-43fe-a17d-6ae1aae441e0" />

Demonstração do funcoionamento da Api no Postman


https://github.com/user-attachments/assets/a8d0126f-0586-4173-b503-88b1dfa57fb1

