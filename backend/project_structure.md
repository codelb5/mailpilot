```text
backend/
├── credentials
│   ├── google_credentials.json
│   └── google_web_credentials.json
├── docs
├── logs
├── scripts
│   ├── validate
│   │   ├── validators
│   │   │   ├── __init__.py
│   │   │   ├── base_validator.py
│   │   │   ├── gmail_validator.py
│   │   │   ├── google_oauth_validator.py
│   │   │   ├── mongodb_validator.py
│   │   │   └── openai_valildator.py
│   │   ├── __init__.py
│   │   ├── validate_config.py
│   │   ├── validate_gmail.py
│   │   ├── validate_google_oauth.py
│   │   ├── validate_mongodb.py
│   │   └── validate_openai.py
│   └── __init__.py
├── src
│   ├── ai
│   │   └── __init__.py
│   ├── api
│   │   ├── dependencies
│   │   │   ├── __init__.py
│   │   │   ├── ai.py
│   │   │   ├── auth.py
│   │   │   ├── gmail.py
│   │   │   ├── google.py
│   │   │   └── oauth_session.py
│   │   ├── routers
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── gmail.py
│   │   │   └── health.py
│   │   ├── __init__.py
│   │   ├── app.py
│   │   └── middleware.py
│   ├── auth
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── authorization_request.py
│   │   │   └── oauth_session.py
│   │   ├── services
│   │   │   ├── __init__.py
│   │   │   ├── google_oauth.py
│   │   │   └── oauth_session_service.py
│   │   └── __init__.py
│   ├── clients
│   │   ├── __init__.py
│   │   ├── gmail_client.py
│   │   ├── google_user_client.py
│   │   └── openai_client.py
│   ├── config
│   │   └── __init__.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── constants.py
│   │   └── logging.py
│   ├── database
│   │   ├── repositories
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── gmail
│   │   └── __init__.py
│   ├── llm
│   │   └── __init__.py
│   ├── models
│   │   └── __init__.py
│   ├── prompts
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── common.py
│   ├── services
│   │   ├── __init__.py
│   │   └── google_user_service.py
│   ├── tools
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── gmail.py
│   │   └── ui.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── validator.py
│   └── __init__.py
├── tests
├── .env
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── main.py
├── project_structure.md
├── README.md
├── requirements.txt
└── test.py
```