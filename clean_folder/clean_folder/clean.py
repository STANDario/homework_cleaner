from pathlib import Path
import os
import shutil
import re
import sys


expansion = {
    "images": [".JPEG", ".PNG", ".JPG", ".SVG"],
    "video": [".AVI", ".MP4", ".MOV", ".MKV"],
    "documents": [".DOC", ".DOCX", ".TXT", ".PDF", ".XLSX", ".PPTX"],
    "audio": [".MP3", ".OGG", ".WAV", ".AMR"],
    "archives": [".ZIP", ".GZ", ".TAR"]
}

spisok = []

p = Path(sys.argv[1])


# Роблю список усіх файлів в усіх папках
def processing_files(path):

    for i in path.iterdir():

        if i.is_dir():
            processing_files(i)
        else:
            spisok.append(i)
    return spisok


# Додаю до папок "images, video, documents, audio, archives, unknown" файли, які відповідають їм по розширенню та міняю їх назву
def add_to_folder(spisok):

    for file in spisok:

        old_name = file.name.replace(file.suffix, "")
        new_name = normalize(old_name) + file.suffix

        suf = file.suffix.upper()

        if suf in expansion.get("images"):
            images = p / "images"
            if images.exists():
                os.rename(file, images / new_name)
            else:
                os.mkdir(images)
                os.rename(file, images / new_name)

        elif suf in expansion.get("video"):
            video = p / "video"
            if video.exists():
                os.rename(file, video / new_name)
            else:
                os.mkdir(video)
                os.rename(file, video / new_name)

        elif suf in expansion.get("documents"):
            doc = p / "documents"
            if doc.exists():
                os.rename(file, doc / new_name)
            else:
                os.mkdir(doc)
                os.rename(file, doc / new_name)

        elif suf in expansion.get("audio"):
            audio = p / "audio"
            if audio.exists():
                os.rename(file, audio / new_name)
            else:
                os.mkdir(audio)
                os.rename(file, audio / new_name)

        elif suf in expansion.get("archives"):
            arch = p / "archives"
            if arch.exists():
                shutil.unpack_archive(
                    file, arch / new_name.replace(file.suffix, ""))
                file.unlink()
            else:
                os.mkdir(arch)
                shutil.unpack_archive(
                    file, arch / new_name.replace(file.suffix, ""))
                file.unlink()

        else:
            unknown = p / "unknown"
            if unknown.exists():
                os.rename(file, unknown / file.name)
            else:
                os.mkdir(unknown)
                os.rename(file, unknown / file.name)


# Видаляю пусті папки
def del_folder(path):

    for i in path.iterdir():

        if i.name == "archives" or i.name == "unknown" or i.name == "audio" \
                or i.name == "documents" or i.name == "video" or i.name == "images":
            continue

        del_folder(i)
        os.rmdir(i)


# Нормалізую текст
def normalize(text):

    x = re.sub(r"[^a-zA-Z0-9]", "_", text)
    return x


def main():

    spisok = processing_files(p)

    add_to_folder(spisok)

    del_folder(p)


if __name__ == "__main__":
    main()
