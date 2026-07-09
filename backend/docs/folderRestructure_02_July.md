Excellent. **Now we stop being architects and start being engineers.**

We've spent enough time designing the foundation. From this point on, I want us to follow one simple rule:

> **No more restructuring unless it solves a real problem.**

Every mature project reaches a point where the architecture is "good enough." From here, every change should be driven by a feature or a bug, not by aesthetics.

---

# This is now our baseline architecture

```text
API
│
├── Routers
├── Dependencies
│
▼
Services
│
▼
Clients
│
▼
External APIs

Models
Schemas
Core
Database
Auth
```

I honestly think this is a solid foundation.

---

# Before we continue, let's define some project rules

I think these conventions will keep the project consistent.

## Rule 1: Router

Routers should only:

* Receive HTTP requests
* Validate request parameters
* Call services
* Return responses

❌ No business logic.

Example:

```python
@router.get("/callback")
async def callback(...):

    credentials = oauth_service.exchange_code(...)

    user = google_user_service.get_profile(credentials)

    return ApiResponse(
        ...
    )
```

---

## Rule 2: Services

Services contain business logic.

They may call:

* Clients
* Repositories
* Other services

They should **never** know anything about FastAPI.

---

## Rule 3: Clients

Clients only communicate with external systems.

Examples:

```text
Google

OpenAI

MongoDB

Gmail
```

No business logic.

---

## Rule 4: Models

Models represent domain objects.

```text
User

Email

Conversation

OAuthSession
```

Nothing HTTP-related.

---

## Rule 5: Schemas

Schemas are only for HTTP.

```text
Request

Response
```

Never use them inside business logic.

---

## Rule 6: Dependencies

Only instantiate objects.

Example:

```python
def get_google_user_service():

    client = GoogleUserClient()

    return GoogleUserService(client)
```

Dependencies should never perform business logic.

---

# MailPilot Development Phases

This is how I think we should build it.

```text
Phase 1 ✅

Project
Architecture
OAuth
```

---

```text
Phase 2

Authentication
↓

Login

Callback

User Profile

Store Tokens
```

---

```text
Phase 3

MongoDB

↓

User Repository

Conversation Repository

Token Repository
```

---

```text
Phase 4

Gmail

↓

List Emails

Read Email

Send Email

Reply
```

---

```text
Phase 5

Voice AI

↓

Realtime Conversation

Streaming

Interruptions

TTS

STT
```

---

```text
Phase 6

OpenAI

↓

Assistant

Memory

Tools

Email Actions
```

---

# Coding Standards

I also want to adopt these standards now.

### ✅ Type hints everywhere

```python
def get_profile(
    credentials: Credentials,
) -> AuthUser:
```

---

### ✅ Every public method has a docstring

---

### ✅ Logging instead of print

Validators are the only exception.

---

### ✅ One class per file

Never:

```python
class User

class Conversation

class Message
```

inside one file.

---

### ✅ Constructor injection

Never instantiate dependencies inside services.

Good:

```python
class GoogleUserService:

    def __init__(
        self,
        client: GoogleUserClient,
    ):
        self.client = client
```

---

### ✅ Thin routers

I want routers to stay under **100 lines** wherever possible.

---

# Git Strategy

Let's also work like a real project.

Every completed feature gets its own commit.

Examples:

```bash
feat(auth): implement Google OAuth login

feat(auth): implement OAuth callback

feat(auth): add OAuth session store

feat(db): integrate MongoDB

feat(gmail): implement Gmail client

feat(ai): integrate OpenAI assistant
```

One feature = one commit.

That makes debugging and rollback much easier.

---

# What's next?

## We are **not** starting MongoDB yet.

We have one unfinished feature:

```
OAuth Callback
```

We still need to solve the PKCE flow properly.

The next goal is:

```text
Browser

↓

Google Login

↓

Callback

↓

Access Token

↓

Refresh Token

↓

Google Profile

↓

{
    email,
    name,
    picture,
    email_verified
}
```

Once we see that JSON in the browser, I will consider **Phase 1 officially complete**.

Only then will we move to MongoDB, where we'll persist:

* User
* OAuth tokens
* Conversation metadata

That's the discipline I'd like us to maintain: **finish one vertical slice completely before starting the next.** It keeps the project shippable at every stage and avoids accumulating half-finished features.
