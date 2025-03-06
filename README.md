# economy_api
economy_api > IMF, World Bank, Yahoo Finance

/economy_project
    ├── economy_api/
    │   ├── main.py            # main FastAPI
    │   ├── models.py          # model of database (PostgreSQL)
    │   ├── services/          # buizness logic (for ex. from API)
    │   ├── routes/            # endpoints FastAPI
    │   ├── database.py        # database connection
    │   ├── cache.py           # logic of caching Redis
    │   └── Dockerfile         # Dockerfile for API of container
    ├── frontend/
    │   ├── app.py             # dashboard (UI)
    │   └── Dockerfile         # Dockerfile for font-end-container
    ├── docker-compose.yml     # Docker Compose main file
    ├── .env                   # enfirovements (optional)

TOOLS:

1. FastAPI
2. PostgresSQL
3. Redis

HOW TO:

1. Build docker images
2. docker compose up -d
2. Get http://127.0.0.1:8000/docs 
4. docker compose down