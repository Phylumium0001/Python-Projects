import os

from translate_file import translate_lines
from translate_file import get_lines

def get_files_in_directory():
    # Get all the filename in the directory
    file_names = os.listdir("./")
    md_file_names = []

    # Sort out the md files
    if file_names:
        for file_name in file_names:
            if (file_name.endswith(".md")):
                md_file_names.append(file_name)
        return md_file_names

    return None

if __name__ == "__main__":
    # Will look for markdown files in the current directory
    files = get_files_in_directory()
    if files:
        try:
            os.mkdir("Output")

        except FileExistsError:
            print("Ouput Folder Already Exists")
            
        for file_path in files:
            print(file_path)
            lines = get_lines(file_path)
            translated_lines = translate_lines(lines)
            new_file_path = f"Output/{file_path.split(".")[0]}.html"
            with open(new_file_path,"w") as file:
                file.writelines(translated_lines)


    else:
        print("No Files Found")