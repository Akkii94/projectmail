# projectmail
This Django Project sent event mail
## Functionality

- Log in
    - via email or username & password
- Create an account
- Log out
- Register

## Installing
first provide mail-id and mail app paswsword in setting.py
### follow this steps

```bash
python source/manage.py makemigrations
```
```bash
python source/manage.py migrate
```
```bash
python source/manage.py createsuperuser
```

```bash
python source/manage.py runserver
```
## first add some data to Details and Employee table and then test the app
