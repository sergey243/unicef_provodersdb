echo "Migrating"
python manage.py migrate
echo "Loading fixtures"
python manage.py loaddata ./basedata.json --exclude auth.permission
echo "Translation"
django-admin compilemessages
echo "Collect static files"
python manage.py collectstatic --noinput