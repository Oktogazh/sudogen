import argparse
from spylls.hunspell import Dictionary


def load_dictionary() -> tuple[list[str], list[str]]:
    """
    Ask for a Hunspell dictionary and extract its content in two arrays
    the first array represents the lemma,
    the second the possible derived word types
    """
    parser = argparse.ArgumentParser(description="Load a hunspell folder.")
    parser.add_argument(
        "dictionary_path",
        nargs="?",
        type=str,
        help="Name of the directory, without the extentions .dic or .aff",
        default="en_US",
    )

    args = parser.parse_args()
    dictionary_path = args.dictionary_path
    dictionary = Dictionary.from_files(dictionary_path)
    return dictionary


def load_hunspell_dic():
    pass
