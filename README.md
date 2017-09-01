# wordsum-python


se:
The purpose of this tool is to train a machine to read, write, edit and publish fiction stories.


Tools:
Python3 3.5
TensorFlow 1.3


Source Structure:

README.md
LICENCE
setup.py
requirements.txt
wordsum/
tests/
data
data/test
doc/README.md
containers/README.md





# Local Setup

## Local Setup on MacOS with Python3 and virtualenv:

1. git clone <source>

2. cd <source>

3. (if not installed) sudo easy_install pip

4. (if virtualenv not installed) sudo pip install --upgrade virtualenv

5. (if brew and python3 not installed) ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

6. (if python3 not installed) brew install python3

7. virtualenv --system-site-packages -p python3 .

8. source ./bin/activate

9. pip3 install --upgrade tensorflow

10. python tensor_install_test.py

11. wait for Tensorflow to say 'Hi'. If it doesn't then something is wrong.


## Local Setup on Ubuntu with Python3 and virtualenv:

1. git clone <source>

2. cd <source>

3. (if pip and virtualenv not installed) sudo apt-get install python3-pip python3-dev python-virtualenv

4. virtualenv --system-site-packages -p python3 .

5. source ./bin/activate

6. pip3 install --upgrade tensorflow

7. python tensor_install_test.py

8. wait for TensorFlow to say 'Hi'. If it doesn't then something is wrong.






Testing:
