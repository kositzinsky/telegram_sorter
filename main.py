from pathlib import Path
import loguru
# TODO: make logs

TELEGAM_DIR = r"C:\Users\user\Downloads\Telegram Desktop"

TYPES = {
    "documents": (".txt", ".pdf", ".doc", ".docx"),
    "images": (
        ".apng",
        ".png",
        ".avif",
        ".gif",
        ".jpg",
        ".jpeg",
        ".jfif",
        ".pjpeg",
        ".pjp",
        ".png",
        ".svg",
        ".webp",
        ".bmp",
        ".ico",
        ".cur",
        ".tif",
        ".tiff",
    ),
    "tables": (
        ".xlsx",
        ".xlsm",
        ".xlsb",
        ".xls",
        ".xltx",
        ".xltm",
        ".csv",
        ".xml",
        ".dbf",
    ),
    "executable": (".exe", ".dll", ".bat"),
    "archives": (".zip", ".rar", ".7z", ".tar", ".apk", ".jar", ".zipx", ".cbr"),
    "videos": (
        ".webm",
        ".mkv",
        ".flv",
        ".vob",
        ".ogv",
        ".ogg",
        ".rrc",
        ".gifv",
        ".mng",
        ".mov",
        ".avi",
        ".qt",
        ".wmv",
        ".yuv",
        ".rm",
        ".asf",
        ".amv",
        ".mp4",
        ".m4p",
        ".m4v",
        ".mpg",
        ".mp2",
        ".mpeg",
        ".mpe",
        ".mpv",
        ".m4v",
        ".svi",
        ".3gp",
        ".3g2",
        ".mxf",
        ".roq",
        ".nsv",
        ".flv",
        ".f4v",
        ".f4p",
        ".f4a",
        ".f4b",
        ".mod",
    ),
    "others": (),
}

FOLDERS = {t: f"\\{t.capitalize()}\\" for t in TYPES.keys()}

files = [f for f in Path(TELEGAM_DIR).iterdir() if f.is_file()]


def sort_files(files: list):
    files_sorted_by_types = {t: [] for t in TYPES.keys()}
    for type in TYPES.keys():
        for file in files:
            if Path(file).suffix in TYPES[type]:
                files_sorted_by_types[type].append(file)
                files.remove(file)
                loguru.logger.debug(f"{file}")

    if files:
        for file in files:
            files_sorted_by_types["others"].append(file)
            loguru.logger.warning(f"{file}")
            
    return files_sorted_by_types


def create_folders():
    for type in TYPES.keys():
        folder = TELEGAM_DIR + FOLDERS[type]
        try:
            Path(folder).mkdir()
        except Exception as e:
            print(e)


def move_files(files: dict):
    files = sort_files(files)
    for type in TYPES.keys():
        for file in files[type]:
            source = Path(file)
            destination = Path(TELEGAM_DIR + FOLDERS[type] + source.name)
            source.rename(destination)


if __name__ == "__main__":
    create_folders()
    move_files(files)
