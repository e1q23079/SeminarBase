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

## メモ

`Waitress`は静的ファイルを自動配信しない．
`docker compose`で起動時は，`Waitress`で動作するようにしており，`static`フォルダーのデータは読み込まれない．
`python app.py`も同様となっている．
