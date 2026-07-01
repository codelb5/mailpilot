```
mailpilot/
│
├── backend/
│   │
│   ├── src/
│   │   │
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── dependencies.py
│   │   │   ├── middleware.py
│   │   │   └── routers/
│   │   │       ├── __init__.py
│   │   │       ├── health.py
│   │   │       ├── auth.py
│   │   │       ├── gmail.py
│   │   │       └── assistant.py
│   │   │
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── config.py
│   │   │   ├── logging.py
│   │   │   ├── constants.py
│   │   │   └── security.py
│   │   │
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   ├── google_oauth.py
│   │   │   ├── token_manager.py
│   │   │   └── credentials.py
│   │   │
│   │   ├── ai/
│   │   │   ├── __init__.py
│   │   │   ├── assistant.py
│   │   │   ├── prompt_manager.py
│   │   │   ├── memory.py
│   │   │   ├── tool_registry.py
│   │   │   ├── tool_executor.py
│   │   │   └── ui_actions.py
│   │   │
│   │   ├── gmail/
│   │   │   ├── __init__.py
│   │   │   ├── client.py
│   │   │   ├── parser.py
│   │   │   ├── reader.py
│   │   │   ├── sender.py
│   │   │   ├── drafts.py
│   │   │   ├── labels.py
│   │   │   ├── threads.py
│   │   │   └── watcher.py
│   │   │
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   ├── mongodb.py
│   │   │   ├── indexes.py
│   │   │   └── repositories/
│   │   │       ├── __init__.py
│   │   │       ├── user_repository.py
│   │   │       ├── gmail_account_repository.py
│   │   │       ├── email_repository.py
│   │   │       ├── thread_repository.py
│   │   │       └── conversation_repository.py
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── email_service.py
│   │   │   ├── conversation_service.py
│   │   │   ├── search_service.py
│   │   │   ├── sync_service.py
│   │   │   └── assistant_service.py
│   │   │
│   │   ├── toolkits/
│   │   │   ├── __init__.py
│   │   │   ├── gmail_tools.py
│   │   │   ├── search_tools.py
│   │   │   ├── ui_tools.py
│   │   │   └── database_tools.py
│   │   │
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── email.py
│   │   │   ├── thread.py
│   │   │   ├── user.py
│   │   │   ├── gmail_account.py
│   │   │   ├── conversation.py
│   │   │   └── ui_action.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── assistant.py
│   │   │   ├── gmail.py
│   │   │   └── common.py
│   │   │
│   │   ├── prompts/
│   │   │   ├── assistant.md
│   │   │   ├── search.md
│   │   │   ├── summarize.md
│   │   │   ├── compose.md
│   │   │   └── reply.md
│   │   │
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── helpers.py
│   │   │   ├── validators.py
│   │   │   ├── exceptions.py
│   │   │   └── enums.py
│   │   │
│   │   └── __init__.py
│   │
│   ├── tests/
│   │   ├── test_auth.py
│   │   ├── test_gmail.py
│   │   └── test_ai.py
│   │
│   ├── docs/
│   │
│   ├── scripts/
│   │
│   ├── logs/
│   │
│   ├── .env
│   ├── .env.example
│   ├── .gitignore
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── README.md
│   └── main.py
│
├── frontend/
│   │
│   ├── public/
│   │
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   │   ├── Assistant/
│   │   │   ├── Compose/
│   │   │   ├── Email/
│   │   │   ├── Inbox/
│   │   │   ├── Layout/
│   │   │   ├── Sidebar/
│   │   │   └── Common/
│   │   │
│   │   ├── context/
│   │   ├── hooks/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── websocket/
│   │   ├── utils/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
│
└── .gitignore
```