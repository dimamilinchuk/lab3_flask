# ¿¿¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿ 3: ¿¿¿¿¿¿¿¿¿, ORM ¿¿ ¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿

## ¿¿¿¿ ¿¿¿¿¿¿¿

¿¿¿¿¿¿¿ ¿¿¿ ¿¿¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿ ¿ ¿¿¿¿¿¿¿¿¿¿:
- ¿¿¿¿¿¿ ¿¿¿¿¿¿¿ ¿¿ ¿¿¿¿¿¿
- ¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿¿¿¿¿
- ¿¿¿¿¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿ ¿¿¿ ¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿
- ¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿ ¿¿¿¿¿ ¿¿ ¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿
- ¿¿¿¿¿¿ ¿ ¿¿¿¿¿ ¿¿¿¿¿ ¿¿¿¿¿ ORM (SQLAlchemy)

**¿¿¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿¿¿ (¿¿¿¿¿¿¿ 0 - ¿¿¿¿¿ ¿¿¿¿¿¿¿):**
- ¿¿¿¿¿ ¿¿¿¿¿¿¿¿¿¿ ¿¿¿ ¿¿¿¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿
- ¿¿¿¿¿ ¿¿¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿¿¿ ¿ ¿¿¿¿¿¿¿ ¿¿¿ ¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿
- ¿¿¿¿¿¿¿ ¿ ¿¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿ **¿¿¿¿¿¿¿¿¿¿** (¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿)
- ¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿/¿¿¿¿¿¿

## ¿¿¿¿¿¿

- Python 3.10+
- Docker ¿¿ Docker Compose
- ¿¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿ ¿ `requirements.txt`

## ¿¿¿¿¿¿¿ ¿¿¿¿¿

### 1. ¿¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿¿¿¿
```bash
git clone <URL_¿¿¿¿¿¿_¿¿¿¿¿¿¿¿¿¿¿>
cd lab3_project
```

### 2. ¿¿¿¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿
¿¿¿¿¿¿¿¿ `.env` ¿¿¿¿ ¿ ¿¿¿¿¿¿ ¿¿¿¿¿¿¿:
```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=secret
POSTGRES_DB=finance_db
DATABASE_URL=postgresql://admin:secret@db:5432/finance_db
```

### 3. ¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿
```bash
docker-compose up -d db       # ¿¿¿¿¿¿ ¿¿¿¿ ¿¿¿¿¿
docker-compose up app         # ¿¿¿¿¿¿ ¿¿¿¿¿¿¿
```

### 4. ¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿
```bash
flask db upgrade
```

## ¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿
```
¿¿¿ app/
¿   ¿¿¿ __init__.py          # ¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿
¿   ¿¿¿ models.py            # ORM ¿¿¿¿¿¿
¿   ¿¿¿ routes/              # ¿¿¿¿¿¿¿¿¿ API
¿   ¿   ¿¿¿ ... 
¿¿¿ migrations/              # ¿¿¿¿¿¿¿¿ ¿¿¿¿ ¿¿¿¿¿
¿¿¿ config.py                # ¿¿¿¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿
¿¿¿ schemas.py               # Marshmallow ¿¿¿¿¿
¿¿¿ __init__.py 
¿¿¿ docker-compose.yaml
¿¿¿ requirements.txt
```

## API ¿¿¿¿¿¿¿¿¿

### ¿¿¿¿¿¿¿
- `POST /accounts` - ¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿ ¿¿¿¿¿¿¿
- `GET /accounts/{user_id}` - ¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿
- `POST /accounts/{user_id}/deposit` - ¿¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿

### ¿¿¿¿¿¿¿¿¿¿
- `POST /transactions/income` - ¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿
- `POST /transactions/expense` - ¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿
- `GET /transactions/{user_id}` - ¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿

**¿¿¿¿¿¿¿ ¿¿¿¿¿¿:**
```bash
curl -X POST http://localhost:5000/transactions/income \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "amount": 1500, "description": "¿¿¿¿¿¿¿¿"}'
```

## ¿¿¿¿¿¿¿¿¿ ¿¿ ¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿
¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿¿¿¿¿:
- ¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿ ¿¿¿¿¿ Marshmallow
- ¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿
- HTTP ¿¿¿¿¿¿ ¿¿¿¿ ¿¿¿ ¿¿¿¿ ¿¿¿¿¿¿¿¿¿¿

**¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿:**
```json
{
  "error": "Insufficient funds",
  "message": "¿¿ ¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿ ¿¿¿ ¿¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿"
}
```

## ¿¿¿¿¿¿¿¿¿¿
¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿¿¿:
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow
- psycopg2-binary

¿¿¿¿¿¿¿¿¿¿¿¿:
```bash
pip install -r requirements.txt
```

## ¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿
1. ¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿:
```bash
FLASK_APP=app FLASK_ENV=development flask run
```

2. ¿¿¿ ¿¿¿¿¿¿ ¿ ¿¿¿¿¿¿¿¿¿¿:
```bash
flask db init          # ¿¿¿¿¿¿¿¿¿¿¿¿¿ (¿¿¿¿¿¿ ¿¿¿)
flask db migrate       # ¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿ ¿¿¿¿¿¿¿¿
flask db upgrade       # ¿¿¿¿¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿¿¿
```
