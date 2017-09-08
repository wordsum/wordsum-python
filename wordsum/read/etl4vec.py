'''
Functions to read a wordsum text model and create data for word2vec.py and begin
to create teh story model.
'''
import logging


'''
groom_string4vec = returns groom str_obj.

Groom the known marks outputted by wordsum-java.

Remove marks until I can reason how to include them into
a version of word2vec. For now, the marks attaching to letters
decrease accuracy as it will prevent the Counting of all the same
words altered with a period or comma.

There's is a better way using a list and iterating over it, or a map
but right now I can move on.
'''
def groom_string4vec(str_obj):
    logging.debug("Grooming :", str_obj)


    str_obj=str_obj.replace("\\n", " ")
    str_obj=str_obj.replace("...", " ")
    str_obj=str_obj.replace("\\u0027", "")
    str_obj=str_obj.replace("\\u003c", "")
    str_obj=str_obj.replace("\\u003e", "")
    str_obj=str_obj.replace("|", "")
    str_obj=str_obj.replace(".", "")
    str_obj=str_obj.replace(",", "")
    str_obj=str_obj.replace(":","")
    str_obj=str_obj.replace(";","")
    str_obj=str_obj.replace("?","")

    str_obj=str_obj.lower()

    return str_obj


'''
Get and check the file state is it has all the data for the word2vec.
'''
def get_file_state(text_model):
    logging.debug("Getting file state :")

    if 'fileState' in text_model:
        file_state = text_model['fileState']
    else:
        file_state = None


    return file_state


'''
Get narrative
'''