# pedalingrelief
Pedaling Relief Project logistics: https://pedalingrelief.herokuapp.com/

This project is currently a prototype. Anything can change at any time.

## Development

This project uses the Python framework [Django](https://www.djangoproject.com/) and the [PostgreSQL](https://www.postgresql.org/) database.

The production environment runs on [Heroku](https://www.heroku.com/), which is owned by Salesforce.

### Setup Process
On MacOS, install system dependencies:
* install [Homebrew](https://docs.brew.sh/Installation)
* run `brew bundle`
* `pyenv install 3.10.3`

Download and use the Python dependencies:
* `pipenv shell`

Get your database going:
* `createdb pedalingrelief`
* `./manage.py migrate`

You might consider using the [PyCharm](https://www.jetbrains.com/pycharm/) IDE for development. There is a free ("Community") version and a subscription ("Professional") version.