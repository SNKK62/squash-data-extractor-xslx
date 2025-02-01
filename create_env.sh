#!/bin/bash

pyenv install 3.10.12
pyenv virtualenv 3.10.12 squash

HOME_DIR=$(echo $HOME)

echo '{
  "venvPath": "'$HOME_DIR'/.pyenv/versions",
  "venv": "squash",
}' > pyrightconfig.json
