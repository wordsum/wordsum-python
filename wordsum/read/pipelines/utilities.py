import os
import logging

def get_file_basename(path_file):
    logging.debug("get_file_basename")

    if path_file is not None:
        file = os.path.splitext(path_file)[0]
        file_base = os.path.basename(file)
    else:
        file_base = None

    return file_base




