echo "Migrating"
python manage.py migrate
echo "Create super user"
python manage.py createsuperuser
echo "Loading fixtures"
python manage.py loaddata ./basedata.json --exclude auth.permission
echo "Translation"
django-admin compilemessages
echo "Collect static files"
manage.py collectstatic