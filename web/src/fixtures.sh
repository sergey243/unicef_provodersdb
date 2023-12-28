# Apply fixtures
echo "Adding cities"
python manage.py cities_light
echo "Migrating goods"
python manage.py loaddata ./providers/fixtures/goods.json
echo "Mgirgqting services"
python manage.py loaddata ./providers/fixtures/services.json
echo "Migrating works"
python manage.py loaddata ./providers/fixtures/works.json
echo "Migrating providers"
python manage.py loaddata ./providers/fixtures/providers.json