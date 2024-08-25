from pathlib import Path
from typing import List, Union


class FilesTools:
    @staticmethod
    def find_files(
        root_path: str, extension: str, exclude_dirs: Union[List[str], None] = None
    ) -> List[Path]:
        root = Path(root_path)
        if not root.is_dir():
            raise ValueError(f"{root_path} não é um diretório válido.")

        if exclude_dirs is None:
            exclude_dirs = []

        files: List[Path] = []
        for file in root.iterdir():
            if file.is_file() and file.suffix == extension:
                files.append(file)
            elif file.is_dir() and file.name not in exclude_dirs:
                files.extend(FilesTools.find_files(str(file), extension, exclude_dirs))
        return files

    @staticmethod
    def get_all_file_names(
        path: str, extension: str, exclude_dirs: Union[List[str], None] = None
    ) -> List[str]:
        names: List[str] = []
        for file in FilesTools.find_files(path, extension, exclude_dirs):
            names.append(file.name.replace(extension, ""))
        return names
