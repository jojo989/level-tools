import base64
import gzip
import zlib
import tkinter as tk
from tkinter import filedialog

def encode_level(level_string: str, is_official_level: bool) -> str:
    gzipped = gzip.compress(level_string.encode())
    base64_encoded = base64.urlsafe_b64encode(gzipped)
    if is_official_level:
        base64_encoded = base64_encoded[13:]
    return base64_encoded.decode()


def decode_level(level_data: str, is_official_level: bool) -> str:
    if is_official_level:
        level_data = 'H4sIAAAAAAAAA' + level_data
    base64_decoded = base64.urlsafe_b64decode(level_data.encode())
    # window_bits = 15 | 32 will autodetect gzip or not
    decompressed = zlib.decompress(base64_decoded, 15 | 32)
    return decompressed.decode()
        
##these 2 functions are from gddocs
        
def save_file(content, extension=".txt"):

    root = tk.Tk()
    root.withdraw()
    file = filedialog.asksaveasfilename(defaultextension=extension, 
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    if file:
        with open(file, "w") as f:
            f.write(content)
        print(f"file saved in  en: {file}")
    else:
        print("dumb lel.")
        
def open_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    if file_path:
        with open(file_path, "r") as f:
            content = f.read()
        print(f"File opened: {file_path}")
        return content
    else:
        print("No file selected.")
        return None

def main():
    while True:
        try:
            user_input = int(input("Select 1 for encode level, 2 for decode level, and 3 for concatenate two strings\nInput: "))
        except ValueError:
            print("Invalid input! Please enter a number.\n")
            continue

        match user_input:
            case 1:
                level_input = open_file()
                if level_input:
                    save_file(encode_level(level_input, False), extension=".txt")
            case 2:
                level_input = open_file()
                if level_input:
                    save_file(decode_level(level_input, False), extension=".txt")
            case 3:
                print("Select your two levels:")
                file1 = open_file()
                file2 = open_file()
                if file1 and file2:
                    output_string = file1 + file2
                    save_file(output_string)
            case _:
                print("Invalid choice! Please select 1, 2, or 3.\n")
                
if __name__ == "__main__":
    main()
        

