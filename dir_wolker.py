from collections import namedtuple
import os

from logger import common_log

FSObject = namedtuple('FSObject', 'name ext is_dir parent', defaults=['', '', False,
                                                                      ''])  # (имя файла, расширение, директория или нет, родительская директория) - кортеж


def walk_dir(path_string: str):
    fs_objects = []
    if not path_string:
        path_string = os.getcwd()
        common_log.warning(f'Путь установлен по умолчанию {path_string}')
    path_string = os.path.abspath(path_string)
    parent = path_string.rstrip('\\').rsplit('\\', 1)[1]  # получаем абсолютный путь
    try:
        for item in os.listdir(path_string):
            obj_name, obj_ext = None, None
            is_dir = False
            if os.path.isdir(path_string + '\\' + item):
                obj_name = item
                is_dir = True
            else:
                obj_name, obj_ext = item.rsplit('.', 1)
            fs_objects.append(FSObject(name=obj_name, ext=obj_ext, parent=parent, is_dir=is_dir))
        common_log.info(msg=str(fs_objects))
    except Exception as exc:
        common_log.error(msg=f'{exc.__class__}: {exc}, = {item}')
    return fs_objects  # список наименованных кортежей


if __name__ == '__main__':
    print('Not for separate use')
