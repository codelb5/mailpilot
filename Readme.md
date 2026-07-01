# MailPilot

> AI-Powered Gmail Assistant that controls the UI through natural language.

---

# Project Vision

MailPilot is an AI-powered email assistant built as part of the Processity AI hiring assignment.

Unlike traditional chatbots, MailPilot is designed to **control the application UI**.

Instead of simply answering:

> "Send an email to John"

the assistant should:

- Open the compose window
- Fill the recipient
- Fill the subject
- Fill the body
- Allow the user to review
- Send the email after confirmation

The AI is not just a chatbot.

It is the primary controller of the application.

---

# Technology Stack

## Backend

- Python
- FastAPI
- OpenAI API
- Gmail API
- MongoDB
- WebSockets

## Frontend

- React
- JavaScript
- Vite

---

# High Level Architecture

```
                React Frontend

      Inbox      Compose      Assistant

                    │

             REST + WebSocket

                    │

              FastAPI Backend

                    │

        ┌───────────┼────────────┐

        ▼           ▼            ▼

     OpenAI      Gmail API    MongoDB

                    │

             Gmail Account
```

---

# Project Principles

Throughout the project we will follow these rules.

## 1. Clean Architecture

Every module should have one responsibility.

No file should become a "God Object."

---

## 2. Service Layer

Business logic belongs inside services.

Example

```
Assistant

↓

Tool

↓

Service

↓

Gmail Client

↓

Google API
```

The Assistant never talks directly to Gmail.

---

## 3. Repository Pattern

Database access should never be mixed with business logic.

Repositories handle MongoDB.

Services handle application logic.

---

## 4. Tool Calling

The AI never performs actions directly.

It calls tools.

Example

```
User

↓

"Show unread emails"

↓

OpenAI

↓

search_emails()

↓

EmailService

↓

MongoDB

↓

Results
```

---

## 5. UI Driven by Actions

The frontend never parses natural language.

The backend sends structured UI actions.

Example

```json
{
    "action": "OPEN_COMPOSE"
}
```

```json
{
    "action": "FILTER_EMAILS",
    "filters": {
        "unread": true
    }
}
```

```json
{
    "action": "OPEN_EMAIL",
    "email_id": "123"
}
```

The frontend simply executes these actions.

---

# Final Backend Architecture

```
backend/

src/

    api/

    ai/

    auth/

    gmail/

    database/

    services/

    toolkits/

    models/

    prompts/

    config/

    utils/
```

---

# Development Roadmap

We will build this project incrementally.

Each phase should leave the application in a working state.

---

# Phase 0

## Project Foundation

Goal

Create a clean project structure.

Tasks

- Create folder structure
- Configure virtual environment
- Configure requirements
- Configure logging
- Configure environment variables
- Configure FastAPI
- Add health endpoint

Result

```
GET /health

↓

{
    "status":"healthy"
}
```

---

# Phase 1

## Google Authentication

Goal

Authenticate users with Gmail.

Tasks

- OAuth
- Login
- Refresh Tokens
- Gmail Connection

Result

User successfully connects Gmail.

---

# Phase 2

## Gmail Client

Goal

Create a reusable Gmail wrapper.

Modules

```
gmail/

client.py

reader.py

sender.py

drafts.py

labels.py

threads.py

parser.py
```

Result

Backend can

- Read emails
- Send emails
- Create drafts
- Archive
- Delete
- Labels

---

# Phase 3

## MongoDB

Goal

Persist email data locally.

Collections

```
users

gmail_accounts

emails

threads

assistant_conversations
```

Tasks

- MongoDB connection
- Repository pattern
- Email synchronization

Result

Emails are cached locally.

---

# Phase 4

## OpenAI Integration

Goal

Create the AI assistant.

Tasks

- OpenAI Client
- Prompt Manager
- Tool Registry
- Tool Executor

Result

Assistant can reason about requests.

---

# Phase 5

## Search

Goal

Search emails using MongoDB.

Example

```
Find emails from Sarah
```

↓

MongoDB

↓

Results

↓

Assistant

---

# Phase 6

## AI Controls UI

Goal

Assistant updates the frontend.

Example

User

```
Compose an email to John
```

↓

Assistant

↓

UI Action

↓

Frontend

↓

Compose window opens

---

# Phase 7

## Context Awareness

The assistant understands

- Current page
- Selected email
- Current thread
- Previous request

Example

```
Reply to this.
```

The assistant knows what "this" means.

---

# Phase 8

## Real-time Gmail Sync

Goal

Receive emails without refresh.

Flow

```
Gmail

↓

Watch API

↓

Backend

↓

MongoDB

↓

Frontend Update
```

---

# Phase 9

## Production Improvements

Tasks

- Error Handling
- Logging
- Testing
- Docker
- Environment Validation
- Cleanup

---

# Git Strategy

Every phase should have meaningful commits.

Examples

```
feat: initialize project

feat: configure FastAPI

feat: implement Gmail authentication

feat: create Gmail client

feat: integrate MongoDB

feat: add OpenAI assistant

feat: implement tool calling

feat: synchronize Gmail

feat: add websocket support
```

---

# Future Scope

After the assignment the architecture should allow adding

- Google Calendar
- Google Drive
- Contacts
- Slack
- Outlook

without major architectural changes.

---

# Important Rule

Every phase must leave the project runnable.

We should never break the application while adding features.

If a phase is complete, the application should start successfully before moving to the next phase.

---

# Current Status

- [x] Project planning
- [x] Folder structure
- [ ] FastAPI foundation
- [ ] Gmail Authentication
- [ ] Gmail Client
- [ ] MongoDB
- [ ] OpenAI Integration
- [ ] AI Tool Calling
- [ ] UI Actions
- [ ] React Frontend
- [ ] Real-time Synchronization
- [ ] Production Ready
