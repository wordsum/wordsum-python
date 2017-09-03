# wordsum-python

## Purpose:
The purpose of this tool is to train a machine to read, write, edit and publish fiction stories.

It is also to be the python implementation of wordsum-java

## Use Cases Being Developed:
1. Using a CNN to classify dialog of a character modelled by wordsum.

2. Using word2vec to plot story plot.


## Tools:
Python3 3.5
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

data/test/ is a dictory of wordsum modelled test data. The file hierarchy may get
        deeper as more test are had.

doc/ is a directory for documents.

containers/ is a directory containing the Dockerfiles.

## Local Setup:

### Local Setup on MacOS with Python3 and virtualenv:

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


### Local Setup on Ubuntu with Python3 and virtualenv:

1. git clone <source>

2. cd <source>

3. (if pip and virtualenv not installed) sudo apt-get install python3-pip python3-dev python-virtualenv

4. virtualenv --system-site-packages -p python3 .

5. source ./bin/activate

6. pip3 install --upgrade tensorflow

7. python tensor_install_test.py

8. wait for TensorFlow to say 'Hi'. If it doesn't then something is wrong.


## Testing:
There is not testing right now because there is not much to test right now.

## ToDo:
1. Test requirements.txt

2. Test everything...



