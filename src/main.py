# project: obsidian-search-link
# author: dev-rafaelmachado
# date: 2024-08-24

from env import env_load
from json import load
from utils.files import FilesTools
from utils.markdown import Markdown


env = env_load()

def handle():
    files = FilesTools.find_files(env['INPUT_PATH'], ".md", env['EXCLUDE_DIRS'])
    file_names = FilesTools.get_all_file_names(env['INPUT_PATH'], ".md", env['EXCLUDE_DIRS'])
    print(f"📂 Found {len(files)} files.")
    count = 0

    for file in files:
        markdown_file = Markdown(file)
        for file_name in file_names:
            match = markdown_file.search_not_wrapped(file_name, "[[", "]]")
            if match:
                if match.group() == file_name:
                    continue
                if markdown_file.search("- class:"):
                    markdown_file.wrap(match, "\"[[", "]]\"") 
                else:
                    markdown_file.wrap(match, "[[", "]]")
                count += 1

    print(f"🔍 Found {count} matches.")


if __name__ == "__main__":
    print("🛠️ Iniciando search project...")

    try:
        handle()
        print("🎉 Search project finished!")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("🚨 Search project failed!")
