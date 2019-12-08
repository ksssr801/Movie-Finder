#!/bin/sh

INSTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo $INSTDIR
SOURCEDIR="$(dirname "$INSTDIR")"
echo $SOURCEDIR

cd $SOURCEDIR
python3 -m venv MovieFinderEnv
source MovieFinderEnv/bin/activate
cd $INSTDIR
echo "Virtual environment (MovieFinderEnv) has been created."
echo ""
echo "Installing the Python dependencies"
pip3 install --upgrade pip
chmod +x requirement.sh
./requirement.sh
python3 manage.py makemigrations
python3 manage.py migrate
echo ""
echo "All Python dependencies has been installed"
chmod +x moviefinder.sh

