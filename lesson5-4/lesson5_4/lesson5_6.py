from hexlet.fs import get_children, get_name, is_file


# BEGIN (write your solution here)
def get_hidden_files_count(node):
    name = get_name(node)
    if is_file(node):
        if name.startswith('.'):
            return 1
        else:
            return 0
    children = get_children(node)
    dis_counts = list(map(get_hidden_files_count, children))
    return sum(dis_counts)
# END
