# coding:utf-8
# version: python 3.5
import uuid
import hashlib


def common_get_uuid():
    """得到uuid,如:244567b69db240da83229cbd1d9b964f"""
    return str(uuid.uuid4()).replace('-', '')


def common_md5_str(_str):
    """得到字符串MD5值"""
    return hashlib.md5(_str.encode()).hexdigest()


def common_md5_file(path):
    """得到文件MD5值"""
    m = hashlib.md5()
    with open(path, 'br') as f:
        for line in f:
            m.update(line)
    return m.hexdigest()
