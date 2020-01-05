
# forkbot
This telegram bot returns the number of forks that each repository of fedora-infra organisation has

## Installing

Start a new virtual environment using `python -m venv evn` and activate it using `source env/bin/activate`.
Install the dependencies using `pip install -r requirements.txt`.
Get a telegram token from @BotFather on telegram.
Run `export TELEGRAM_TOKEN=<token>` where you replace `<token>` with your own token

## Usage

Send a message of the form `/q <repo1> <repo2> <repo3>` to query for specific repositories, or `/q` to return all repositories.