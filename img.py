import platform
from PIL import Image
import sys
import os

exts = ["JPG", "PNG", "WEBP"]

if platform.system().lower() == "windows":
    os.system("cls")
else:
    os.system("clear")

def help_msg() -> None:
    print("[*] Use -> python3 img.py [extention_to_convert] file.ext\n[*] List Formats -> python3 img.py --list\n")

def main(img_to_convert:str, ext:str) -> None:
    if ext.lower() == "jpg":
        ext = "jpeg"
    img = Image.open(img_to_convert).convert("RGB")
    img.save(f"img.{ext.lower()}", ext.lower())

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        help_msg()

    elif len(sys.argv) == 2:
        if sys.argv[1] in ("--list", "-l"):
            for ext in exts:
                print(f"* {ext}\t-  Convert to {ext.lower()} extention")

        elif sys.argv[1] in ("--help", "-h", "?"):
            help_msg()

    elif len(sys.argv) == 3:
        main(sys.argv[2], sys.argv[1])
