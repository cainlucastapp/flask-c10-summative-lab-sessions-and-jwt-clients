# ⚔️ Quest Tracker API

A secure Flask REST API backend for a fantasy-themed productivity app. Users create characters, track quests, and earn gold upon completion. Built with session-based authentication and full CRUD functionality.

---

## 📖 Description

Quest Tracker is a user-owned resource API where each adventurer can manage their personal quest log. Users cannot view or modify each other's quests. Authentication is handled via Flask sessions with bcrypt password hashing.

---

## 🛠️ Installation

### Requirements
- Python 3.13
- Pipenv

### Steps

1. **Clone the repository**
```bash
   git clone 
   cd flask-c10-summative-lab-sessions-and-jwt-clients/server
```

2. **Install dependencies**
```bash
   pipenv install
```

3. **Activate the virtual environment**
```bash
   pipenv shell
```

4. **Set environment variables**
```bash
   # Windows
   set FLASK_APP=app.py
   set FLASK_ENV=development

   # Mac/Linux
   export FLASK_APP=app.py
   export FLASK_ENV=development
```

5. **Initialize the database**
```bash
   flask db upgrade
```

6. **Seed the database**
```bash
   python seeds.py
```

7. **Run the server**
```bash
   flask run --port=5555 --debug
```

The API will be running at `http://127.0.0.1:5555`

---

## 🌐 API Endpoints

### Auth

| Method | Route | Description | Auth Required |
|--------|-------|-------------|---------------|
| POST | `/signup` | Register a new user | ❌ |
| POST | `/login` | Log in an existing user | ❌ |
| GET | `/check_session` | Check if a session is active | ❌ |
| DELETE | `/logout` | End the current session | ❌ |

#### Signup Request Body
```json
{
  "username": "Thorin",
  "email": "thorin@ironforge.com",
  "password": "hammertime1",
  "password_confirmation": "hammertime1",
  "character_class": "Fighter"
}
```

#### Login Request Body
```json
{
  "username": "Howl",
  "password": "swordfight1"
}
```

#### Auth Response
```json
{
  "id": 1,
  "username": "Howl",
  "email": "howl@tavernbook.com",
  "character_class": "Fighter",
  "level": 5,
  "gold": 450
}
```

---

### Quests

All quest routes require an active session.

| Method | Route | Description | Auth Required |
|--------|-------|-------------|---------------|
| GET | `/quests` | Get all quests for current user (paginated) | ✅ |
| POST | `/quests` | Create a new quest | ✅ |
| PATCH | `/quests/<id>` | Update quest status | ✅ |
| DELETE | `/quests/<id>` | Delete a quest | ✅ |

#### Pagination Query Params
GET /quests?page=1&per_page=10

#### GET /quests Response
```json
{
  "quests": [
    {
      "id": 1,
      "title": "Slay the Mountain Troll",
      "description": "A massive troll has been terrorizing the mountain pass.",
      "status": "completed",
      "difficulty": "Hard",
      "reward_gold": 200,
      "user_id": 1,
      "created_at": "2026-05-23T19:00:00.000000",
      "updated_at": "2026-05-23T19:00:00.000000"
    }
  ],
  "pagination": {
    "total": 20,
    "pages": 4,
    "current_page": 1,
    "per_page": 5,
    "has_next": true,
    "has_prev": false
  }
}
```

#### POST /quests Request Body
```json
{
  "title": "Defeat the Dark Knight",
  "description": "A mysterious dark knight challenges warriors at the crossroads.",
  "difficulty": "Hard",
  "reward_gold": 300
}
```

#### PATCH /quests/<id> Request Body
```json
{
  "status": "completed"
}
```
> Note: Only `status` can be updated. Quests with status `completed` or `failed` are locked and cannot be modified. Completing a quest automatically adds `reward_gold` to the user's gold total.

#### Quest Response
```json
{
  "id": 1,
  "title": "Slay the Mountain Troll",
  "description": "A massive troll has been terrorizing the mountain pass.",
  "status": "completed",
  "difficulty": "Hard",
  "reward_gold": 200,
  "user_id": 1,
  "created_at": "2026-05-23T19:00:00.000000",
  "updated_at": "2026-05-23T19:00:00.000000"
}
```

---

## 👤 Seeded Characters

| Username | Class | Level | Password |
|----------|-------|-------|----------|
| Howl | Fighter | 5 | swordfight1 |
| Jastor | Mage | 9 | !expelliarmus |
| Alistare | Rogue | 3 | 34n21poirrn!@$#21n4i32n42$#@M$ono32n1l2n4l321n4lnr3#@ |
| Kaiser | Paladin | 4 | forthelord |
| Volstage | Ranger | 1 | ilikesquires |

---

## 🔒 Security Features

- Passwords hashed / salted with bcrypt 
- Session-based authentication via Flask sessions
- Route protection — unauthenticated requests return 401
- Users can only access their own quests — cross-user requests return 404
- Completed and failed quests are locked from further modification
- Input validation on all fields with descriptive error messages

---

## 🧰 Tech Stack

- Python 3.13
- Flask 
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Bcrypt
- Flask-RESTful
- Flask-CORS
- SQLite

---

## 🗺️ Planned Improvements

- Equipment system (weapons, armor, accessories)
- Experience points and automatic leveling
- Quest difficulty scaling based on character level
- NPC quest givers with reputation tracking
- Inventory system with consumable items
- Party system for group quests
- Achievement and title system
- Quest categories and filtering