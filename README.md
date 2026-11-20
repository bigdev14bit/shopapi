# Shop API

## PostgreSQL

Install the Python dependencies with `python3 -m pip install -r requirements.txt`.
Copy `.env.example` to `.env`, set `DB_PASSWORD` to the password for your PostgreSQL
user, and load the variables into your shell before running Django:

```sh
set -a
. ./.env
set +a
python3 manage.py migrate
python3 manage.py runserver
```

The database name defaults to `shopapi_db`; the connection user, password, host,
and port are read from `DB_USER`, `DB_PASSWORD`, `DB_HOST`, and `DB_PORT`.
If the database and user do not already exist, create them with PostgreSQL's
interactive tools so the password is not embedded in a command:

```sh
sudo -u postgres createuser --pwprompt shopapi
sudo -u postgres createdb --owner=shopapi shopapi_db
```

For an existing database, ensure the login role exists and grant it permission
to create tables in the public schema:

```sql
GRANT CONNECT ON DATABASE shopapi_db TO shopapi;
GRANT USAGE, CREATE ON SCHEMA public TO shopapi;
```

Run these statements as the database owner or a PostgreSQL administrator.
Do not commit `.env` or put database passwords in source control.

The `catalog` app provides categories and products, including descriptions,
non-negative two-decimal prices, and Django admin management.
