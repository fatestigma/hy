from hy.importer import import_file_to_module


# import_file_to_module


def test_basics():
    "Make sure the basics of the importer work"
    module = import_file_to_module("basic",
                                   "tests/resources/importer/basic.hy")
