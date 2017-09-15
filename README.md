# wordsum-python

## Purpose:
The purpose of this tool is to train a machine to read, write, edit and publish fiction stories.

It is also to be the python implementation of wordsum-java

## Models Being Developed:
1. Using word2vec to model plot.

2. Using a CNN to classify dialog of a character modeled by wordsum.

3. Using an LSTM to model syntax (so one could train and create the regex to parse text for wordsum text model).

## Tools:
Python3 3.6.1

TensorFlow 1.3


## Source Structure:

wordsum/ is root level of the source. It is intended that the source structure will
        loosely mirror wordsum-java, it will for now be shallow and allow to
        see where the code writes.

tests/ is root level of the tests for the wordsum python code.

data/ is a directory to contain any test data or output data before it is put
        into a container image for archive.

data/model/ is a directory to output model checkout points before they are put in to
        containers.

data/test/ is a directory of wordsum modeled test data. The file hierarchy may get
        deeper as more test are had.

doc/ is a directory for documents.

containers/ is a directory containing the Dockerfiles.

## Local Setup:

### Local Setup on MacOS with Python3 and virtualenv:
TODO: TEST MAC STEPS AGAIN!
1. git clone <source>

2. cd <source>

3. (if not installed) sudo easy_install pip

4. (if virtualenv not installed) sudo pip install --upgrade virtualenv

5. (if brew and python3 not installed) ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

6. (if python3 not installed) brew install python3 --with-tcl-tk

7. virtualenv --system-site-packages -p python3 .

8. source ./bin/activate

9. export PYTHONHASHSEED=0

10. pip3 install -r requirements.txt

11. python3 test/test_tensor_install.py

12. wait for Tensorflow to say 'Hi'. If it doesn't then something is wrong.


### Local Setup on Ubuntu with Python3 and virtualenv:

1. git clone <source>

2. cd <source>

3. (if pip and virtualenv not installed) sudo apt-get install python3-pip python3-dev python-virtualenv python3.6-tk

4. virtualenv --system-site-packages -p python3 .

5. source ./bin/activate

6. export PYTHONHASHSEED=0

7. pip3 install -r requirements.txt

8. python3 -m spacy.en.download all

9. python3 test/test_tensor_install.py

10. wait for TensorFlow to say 'Hi'. If it doesn't then something is wrong.


## Testing:
1  cd <source>
2. pytest test/test_etl4vec.py

## ToDo:
1. Test everything...
