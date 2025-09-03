# SeminarBase

## 仮想環境作成

```bash
python -m  venv .venv
```

## 仮想環境に入る

```bash
source .venv/Scripts/activate
```

## ライブラリのインストール

```bash
pip install -r requirements.txt 
```

## サーバー起動

### Python

```bash
python manage.py runserver
```

### Docker

```bash
# ビルド
docker compose build
# 起動
docker compose up
```

## データベース

db.sqlite3
