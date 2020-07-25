export DATABASE_URL=postgresql://megaindexof%40ritudb:chow020890@ritudb.postgres.database.azure.com:5432/megaindexof
python manage.py migrate
unset DATABASE_URL