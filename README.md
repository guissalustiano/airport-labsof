
# Running locally
```bash
# Create enviroment
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migration
python manage.py migrate

# Create super user to acess /admin
python manage.py createsuperuser

# Run server
python manage.py runserver
```

# Run tests
```bash
python manage.py test
```

# Default users
manager@mail.com
operation@mail.com
pilot@mail.com

senha: 1234$qwer
