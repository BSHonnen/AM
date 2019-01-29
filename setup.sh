#!/bin/bash
if [[ "$(uname -s)" == "Darwin" ]]; then
  echo "is a mac"
  set -ex
  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
else
  echo "is a windows"
  python -m venv venv
  source venv/Scripts/activate
  pip install -r requirements.txt
fi

