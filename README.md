# Binobot

Python bot for Binomo trading. This will open your browser and do auto trading without you doing anything.

## Installation

Clone this repo and install all requirements.
Please use [virtualenv](https://virtualenv.pypa.io/en/latest/) or [pyenv](https://github.com/pyenv/pyenv) for an isolated python environment. 

```bash
git@github.com:maztohir/binobot.git

#creating env
pyenv virtualenv 3.7 binobot

#activating virtual env
pyenv shell binobot

#installing all requirements
pip3 install requirements.txt
```

## Usage
Go to the binobot folder and run this

```bash
#####################
#     Step 1.       #
#####################
#Required
python3 start_browser.py
#This will opening your browser, after the browser up, please do login to binomo page

#####################
#     Step 2.       #
#####################
#after you login successfully, then run:
binobot$ python3 start_trading.py
#done. see the bot will automatically run your account to trade :)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)