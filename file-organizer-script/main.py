import logging.config
import shutil, os, re,logging
logging.basicConfig(filename="logs.log",
                              filemode="w",
                              level=logging.INFO,
                              format='[%(asctime)s] : %(levelname)s - %(message)s',
                                datefmt='%H:%M:%S')


def create_folders():
    folders = ["Images", "Documents", "Compressed_files", "Videos","Programs","Code"]
    for foldername in folders:
            try:
                os.makedirs(foldername)
            except FileExistsError:
                print(f"{foldername} exists")

def remove_folders():
    "If you want to delete the folders -\_(-_-)_/-"
    folders = ["Images", "Documents", "Compressed_files", "Videos","Programs","Code"]

    for foldername in folders:
        try:
            os.removedirs(foldername)
        except FileNotFoundError:
            pass

def organise_file(filepath):
    formats = {
        "Images":[".jpeg",".jpg",".png"],
        "Documents":[".pdf",".doc",".docx"],
        "Compressed_files":[".zip",".rar"],
        "Videos":['.mp4',".mp"],
        "Programs":[".exe"],
        "Code":[".py"]
        }
    ending = re.compile(r".\w+$").findall(filepath)[0]
    
    for file_type in formats:
        for extension in formats[file_type]:
            print(f"{extension}")
            if ending in extension:
                logging.info(f"Moving {filepath} to {file_type}")
                shutil.move(filepath,file_type)

if __name__ == "__main__":
    print("Initiating File Organization (-_-)")
    logging.info("Creating Folders")

    logging.info("Finding Files\n")
    files = os.listdir("./")
    
    for file in files:

        create_folders()
        organise_file(file)
