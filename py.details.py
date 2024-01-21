from os.path import exists

def make_details_file(file_path):
    name = input("Name : ")
    author_name = input("Author name : ")
    version = input("Version : ")
    language = input("Language : ")
    tlv = input("TLV (Tested Language Version) : ")
    license = input("License : ")
    with open(file_path, "w") as f:
        f.write(f"Name : {name}")
        f.write(f"\nAuthor : {author_name}")
        f.write(f"\nVersion : {version}")
        f.write(f"\nLanguage : {language}")
        f.write(f"\nTLV : {tlv}")
        f.write(f"\nLicense : {license}")

def read_details_file(file_path):
    if not exists(file_path):
        raise FileNotFoundError(f"The file specified ({file_path}) does not exist.")
    else:
        with open(file_path, "r") as f:
            print(f.read())
    

if __name__ == '__main__':
    match input("Mode (read/make) : "):
        case "read":
            read_details_file(input("Enter the filename for .details [with extension] : "))
        case "make":
            make_details_file(input("Enter the filename for .details [with extension] : "))
        case _:
            print("Invalid mode.")