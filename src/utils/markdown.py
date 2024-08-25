import re
from pathlib import Path


class Markdown:
    def __init__(self, path: Path | str, encoding: str = "utf-8") -> None:
        self.path: Path = Path(path)
        self.encoding: str = encoding
        self.text: str = ""
        with open(path, "r", encoding=encoding) as file:
            self.text = file.read()

    def get_text(self) -> str:
        return self.text

    def search(self, word: str) -> re.Match | None:
        return re.search(word, self.text)

    def search_not_wrapped(
        self, word: str, wrap_word_start: str, wrap_word_end: str
    ) -> re.Match | None:
        wrap_word_start_escaped = re.escape(wrap_word_start)
        wrap_word_end_escaped = re.escape(wrap_word_end)
        word_escaped = re.escape(word)

        pattern = (
            f"(?<!{wrap_word_start_escaped}){word_escaped}(?!{wrap_word_end_escaped})"
        )

        return re.search(pattern, self.text)

    def replace(self, word: str, new_word: str, save: bool = True) -> str:
        self.text = re.sub(re.escape(word), new_word, self.text)

        if save:
            self.save()

        return self.text

    def wrap(
        self,
        match: re.Match,
        wrap_word_start: str,
        wrap_word_end: str,
        save: bool = True,
    ) -> str:
        self.text = self.text.replace(
            match.group(), f"{wrap_word_start}{match.group()}{wrap_word_end}"
        )

        if save:
            self.save()

        return self.text

    def save(self) -> None:
        with open(self.path, "w", encoding=self.encoding) as file:
            file.write(self.text)
