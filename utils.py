import os

def create_filepath(filename: str, new_filename: str) -> str:
    dirname = os.path.dirname(filename)

    return f"{dirname}/{new_filename}"