import os
from dataclasses import dataclass, field
from datetime import datetime, timedelta


@dataclass
class Selector:
    min_size: int = -1
    older_than_days: int = -1
    extensions: list[str] = field(default_factory=[])


@dataclass
class File:
    path: str
    size: int
    last_modify_time: datetime

    def is_older_than(self, days: int) -> bool:
        return datetime.now() - self.last_modify_time > timedelta(days=days)

    @staticmethod
    def get_file(path: str) -> 'File':
        return File(path, os.path.getsize(path), datetime.fromtimestamp(os.path.getmtime(path)))


class SearchEngine:
    def traverse_path(self, start_path: str, depth: int, selector: Selector) -> list[File]:
        matching_files = []
        try:
          for f in os.listdir(start_path):
            full_f = os.path.join(start_path, f)
            if os.path.isfile(full_f):
                file = File.get_file(full_f)
                if not file.is_older_than(selector.older_than_days):
                    continue
                if not file.size >= selector.min_size:
                    continue
                if len(selector.extensions) > 0:
                    ok = False
                    name = file.path.upper()
                    for ext in selector.extensions:
                        if name.endswith(ext.upper()):
                            ok = True
                            break
                    if not ok:
                        continue
                matching_files.append(file)

            if os.path.isdir(full_f):
                if depth > 0:
                    extra = self.traverse_path(start_path=full_f, depth=depth - 1, selector=selector)
                    matching_files.extend(extra)
        except PermissionError:
            return []
        return matching_files


if __name__ == '__main__':
    # f = File('', 10, last_modify_time=datetime.now() - timedelta(days=10))
    # print(f.is_older_than(15))
    # print(File.get_file('aparser.py'))
    selector = Selector(extensions=['zip'])
    engine = SearchEngine()
    files = engine.traverse_path('/home/wrong', depth=4, selector=selector)
    files = sorted(files, key=lambda f: -f.size)
    files = files[:20]
    for f in files:
        print(f)