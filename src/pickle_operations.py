import pickle
import bz2


def save_pickles(list_name, path) -> None:
    """
    saves input object (here: tuple containing object list and integer list)
    :param list_name: list to be stored
    :param path: where to save + file name
    :return: None
    """
    # open file and save to it
    with open(path, "wb") as f:
        pickle.dump(list_name, f)


def save_compressed_pickles(list_name, path) -> None:
    """
    Saves input object to a compressed (bz2) file to yield a smaller file
    :param list_name: object to be stored
    :param path: where to save the file + its name
    :return: None
    """
    bz2_file = bz2.BZ2File(path, 'w')

    # write the input object to bz2 file
    pickle.dump(list_name, bz2_file)


def load_compressed_pickles(path) -> object:
    """
    loads pickle object from compressed (bz2) file
    :param path: where is the file stored (directory) and what's its name
    :return: decompressed pickle object
    """
    bz2_file = bz2.BZ2File(path, 'rb')
    return pickle.load(bz2_file)


def load_pickles(path) -> object:
    """
    loads stored pickles (here: object lists) from file
    :param path: path to pickle file
    :return: decompressed pickle / object list
    """
    # open file and return obtained content
    with open(path, "rb") as f:
        return pickle.load(f)