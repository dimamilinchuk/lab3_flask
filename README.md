# 真真真真真� 真真真 3: 真真真真�, ORM 真 真真真� 真真真�

## 真真 真真真�

真真真� 真� 真真真真真� 真真真 � 真真真真真:
- 真真真 真真真� 真 真真真
- 真真真真� 真真真真� 真真真真真真
- 真真真真真真� 真真真真 真真真 真� 真真真真� 真真真
- 真真真真� 真真真� 真真� 真 真真真� 真真真�
- 真真真 � 真真� 真真� 真真� ORM (SQLAlchemy)

**真真真真真� 真真真真真 (真真真� 0 - 真真� 真真真�):**
- 真真� 真真真真真 真� 真真真真真真 真真真�
- 真真� 真真真真真� 真真真真真 � 真真真� 真� 真真真真� 真真真
- 真真真� � 真真真真真 真真真 **真真真真真** (真真真真 真真真�)
- 真真真� 真真真真� 真真真真 真真真真 真真真�/真真真

## 真真真

- Python 3.10+
- Docker 真 Docker Compose
- 真真真真真 真真真� � `requirements.txt`

## 真真真� 真真�

### 1. 真真真真真 真真真真真�
```bash
git clone <URL_真真真_真真真真真�>
cd lab3_project
```

### 2. 真真真真真真 真真真真
真真真真 `.env` 真真 � 真真真 真真真�:
```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=secret
POSTGRES_DB=finance_db
DATABASE_URL=postgresql://admin:secret@db:5432/finance_db
```

### 3. 真真真 真真真真
```bash
docker-compose up -d db       # 真真真 真真 真真�
docker-compose up app         # 真真真 真真真�
```

### 4. 真真真真� 真真真真
```bash
flask db upgrade
```

## 真真真真� 真真真�
```
真� app/
�   真� __init__.py          # 真真真� 真真真�
�   真� models.py            # ORM 真真真
�   真� routes/              # 真真真真� API
�   �   真� ... 
真� migrations/              # 真真真真 真真 真真�
真� config.py                # 真真真真真真 真真真�
真� schemas.py               # Marshmallow 真真�
真� __init__.py 
真� docker-compose.yaml
真� requirements.txt
```

## API 真真真真�

### 真真真�
- `POST /accounts` - 真真真真� 真真真 真真真�
- `GET /accounts/{user_id}` - 真真真真� 真真真�
- `POST /accounts/{user_id}/deposit` - 真真真真真 真真真�

### 真真真真真
- `POST /transactions/income` - 真真真真� 真真真
- `POST /transactions/expense` - 真真真真� 真真真�
- `GET /transactions/{user_id}` - 真真真� 真真真真

**真真真� 真真真:**
```bash
curl -X POST http://localhost:5000/transactions/income \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "amount": 1500, "description": "真真真真"}'
```

## 真真真真� 真 真真真� 真真真�
真真真� 真真真真真真:
- 真真真真� 真真� 真真� Marshmallow
- 真真真真� 真真真� 真真真�
- HTTP 真真真 真真 真� 真真 真真真真真

**真真真� 真真真�:**
```json
{
  "error": "Insufficient funds",
  "message": "真 真真真� 真真真真真� 真真真 真� 真真真真真 真真真真"
}
```

## 真真真真真
真真真� 真真真真真:
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow
- psycopg2-binary

真真真真真真:
```bash
pip install -r requirements.txt
```

## 真真真真 真真真真
1. 真真真真� 真真真真真真 真真真:
```bash
FLASK_APP=app FLASK_ENV=development flask run
```

2. 真� 真真真 � 真真真真真:
```bash
flask db init          # 真真真真真真� (真真真 真�)
flask db migrate       # 真真真真� 真真� 真真真真
flask db upgrade       # 真真真真真真 真真真真
```
