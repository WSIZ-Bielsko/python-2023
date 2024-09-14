from loguru import logger


def merge_files(final_filename: str, file_1: str, file_2: str):
    if file_2 == '':
        logger.info(f'merging {file_1} into {final_filename}')

        return

    logger.info(f'merging {file_1} and {file_2} into {final_filename}')


def distributed_merge(files: list[str], level: int):
    logger.info(f'starting merger at {level=}')
    logger.debug(f'files: {files}')
    if len(files) == 1:
        return

    num_files = len(files)
    final_files = []

    for i in range((num_files + 1) // 2):
        final_filename = f'L{level}_partX{i}'
        if 2 * i + 1 >= num_files:
            merge_files(final_filename, files[2 * i], '')
        else:
            merge_files(final_filename, files[2 * i], files[2 * i + 1])
        final_files.append(final_filename)
    logger.info(f'merged files level {level} completed')
    distributed_merge(final_files, level + 1)


if __name__ == '__main__':
    files = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt']
    distributed_merge(files, 1)
