## Run

```
pyenv install 3.9.4
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
pip install --user pipenv
python -m pip install --upgrade pip
# Add export PATH="$HOME/.local/bin:$PATH" to a configuration file of your shell

pyenv local 3.9.4
pyenv virtualenv 3.9.4 movie-clipper
pyenv local movie-clipper
pip install -r requirements.txt

python clip.py your_movie.mp4
```
