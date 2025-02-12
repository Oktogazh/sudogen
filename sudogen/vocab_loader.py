import argparse


def load_dictionary() -> tuple[list[str], list[str]]:
    """
    Ask for a Hunspell dictionary and extract its content in two arrays
    the first array represents the lemma,
    the second the possible derived word types
    """
    parser = argparse.ArgumentParser(
        description="Load a file containing a list of words or a hunspell .dic file."
    )
    parser.add_argument("file_path", type=str, help="Path of the file:")

    args = parser.parse_args()
    file_path = args.file_path
    words = []
    derived_words = []
    if file_path.endswith(".dic"):
        words = load_hunspell_dic(file_path)
    else:
        with open(file_path, "r") as file:
            words = file.read().splitlines()

    print(
        f"loaded {len(words)} words and {len(derived_words)} derived words from {file_path}"
    )
    return words, derived_words


def load_hunspell_dic():
    pass
