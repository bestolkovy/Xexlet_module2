# Ассоциативный массив.
# Решение учителя структурно более правильное. Он выделил в отдельную функцию
# разрешение коллизий и поиск индекса.
import zlib


def set_(map, key, value):
    key_hash = zlib.crc32(key) % 10
    if not map[key_hash] or map[key_hash][0] == key:
        map[key_hash] = (key, value)
        return True
    else:
        return False


def get_(map, key, default=None):
    key_hash = zlib.crc32(key) % 10
    if not map[key_hash]:
        result = default
        return result
    if map[key_hash][0] != key:
        return None
    else:
        result = map[key_hash][1]
        return result
