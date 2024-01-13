import datetime

from search import File




# def get_size_verbose(size: int) -> str:
#     # zamienić size (w B) na coś w GB, MB, KB ... z 1 miejscem po przecinku
#     # 1234 ---> 1.2 KB
#     # 123456 --> 123.4 kB
#     # 1234567 --> 1.2 MB
#     # zawsze najwyższa niezerowa jednostka, nie więcej niż 1 miejsce po przecinku....
#     # 1 KB = 1000 B
#     #
#     pass

def get_age_in_days(date: datetime) -> int:
    # find out how many days passed between datetime.now() and date

    return (datetime.datetime.now() - date).days


def get_size_verbose(size: int) -> str:
    if len(str(size)) >= 13:
        return str(round(size / 10 ** 12, 2)) + " TB"
    if len(str(size)) >= 10:
        return str(round(size / 10 ** 9, 2)) + " GB"
    if len(str(size)) >= 7:
        return str(round(size / 10 ** 6, 2)) + " MB"
    if len(str(size)) >= 4:
        return str(round(size / 10 ** 3, 2)) + " KB"
    return str(size) + "B"


def file_verbose(f: File) -> str:
    return f'{f.path:>40}\t{get_size_verbose(f.size):>8}\t{get_age_in_days(f.last_modify_time)}d'


if __name__ == '__main__':
    f = File(path='/home/wrong/vmware/gns3_vmware.zip', size=4733877482,
             last_modify_time=datetime.datetime(2021, 4, 10, 0, 21, 34, 746313))
    f2 = File(path='/home/wrong/Downloads/vIOS-L2.zip', size=36275271,
              last_modify_time=datetime.datetime(2021, 2, 1, 19, 49, 51, 930827))

    print(file_verbose(f))
    print(file_verbose(f))
    print(file_verbose(f))
    print(file_verbose(f2))
