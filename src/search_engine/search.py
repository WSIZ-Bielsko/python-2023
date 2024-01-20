from model import *
from gg.easy import play


def get_size_verbose(size: int) -> str:
    n_digits = len(str(size))
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    group = min(n_digits // 3, 4)

    unit = units[group]
    unit_size = (10 ** 3) ** group

    return str(round(size / unit_size, 1)) + ' ' + unit


def get_age_in_days(date: datetime) -> int:
    # find out how many days passed between datetime.now() and date

    return (datetime.now() - date).days


def file_verbose(f: File) -> str:
    return f'{f.path:<70}\t{get_size_verbose(f.size):>8}\t{get_age_in_days(f.last_modify_time)}d'


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
    selector = Selector(extensions=[])
    engine = SearchEngine()
    files = engine.traverse_path('/home/wrong', depth=3, selector=selector)
    files = sorted(files, key=lambda f: -f.size)
    files = [f for f in files if '.wine' not in f.path]
    files = files[:20]
    for f in files:
        print(file_verbose(f))

    print('-----')
    play()