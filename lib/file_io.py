from pathlib import Path

def write_file(file_name, file_content):
    file_path = Path(file_name).resolve()  # Convert the Path object to a string
    with open(file_path.with_suffix(".txt"), "w") as file:
        file.write(file_content)


def append_file(file_name, append_content):
    file_path = Path(file_name).resolve()  # Convert the Path object to a string
    with open(file_path.with_suffix(".txt"), "a") as file:
        file.write(append_content)

def read_file(file_name):
    file_path = Path(file_name).resolve()  # Convert the Path object to a string
    with open(file_path.with_suffix(".txt"), "r") as file:
        content = file.read()
    return content
