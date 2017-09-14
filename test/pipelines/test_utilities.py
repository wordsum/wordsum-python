import  wordsum.read.pipelines.utilities as utilities


def test_get_file_basename():

    file_basename = utilities.get_file_basename("/home/tester/path/file.txt")

    assert file_basename == "file"
