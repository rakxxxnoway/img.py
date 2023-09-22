from PIL import Image
import platform
import sys
import os

exts = [ "JPG", "PNG", "WEBP", "ICO", "BLP", "BMP", "DDS", "DIB", "EPS", "GIF", "ICNS", "IM", "MSP", "PCX", "PPM", "SGI", "SPIDER", "TGA", "TIFF", "XBM"]

if platform.system().lower() == "windows":
    os.system("cls")
else:
    os.system("clear")

def help_msg() -> None:
    print("[*] Use -> python3 img.py [format] file.ext\n[*] List Formats -> python3 img.py --list\n")

def main(ext:str, img_to_convert:str, width:int=0, height:int=0) -> None:
    if ext.lower() == "jpg":
        ext = "jpeg"
    
    img = Image.open(img_to_convert)

    print(f"[!] Converting from {img.format} to {ext.upper()}...")

    img_sizes = [(width, height)]

    if width == 0 and height == 0:
        match ext.lower():
            case "ico":
                img_sizes = [(32, 32)]
            case _:
                img_sizes = [img.size]
                img.convert("RGB")

    img.save(f"img.{ext.lower()}", ext.lower(), sizes=img_sizes)

    print(f"[!] Done! Saved at -> {os.path.abspath(f'img.{ext.lower()}')}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 7:
        help_msg()

    elif len(sys.argv) == 2:
        if sys.argv[1] in ("--list", "-l"):
            for ext in exts:
                if ext.lower() == "spider":
                    print(f"* {ext} - Convert to {ext.lower()} extention")
                else:
                    print(f"* {ext}\t-  Convert to {ext.lower()} extention")

        elif sys.argv[1] in ("--help", "-h", "?"):
            help_msg()

    elif len(sys.argv) == 3:
        main(*[sys.argv[1], sys.argv[2]])

    elif len(sys.argv) == 7:
        main(*[sys.argv[1], sys.argv[2]], width=int(sys.argv[3]), height=int(sys.argv[5]))
