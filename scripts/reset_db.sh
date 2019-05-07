sudo -u postgres psql -a -f ./scripts/drop_db.sql
sudo -u postgres psql -a -f ./scripts/create_db.sql

python manage.py migrate