import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


# BEGIN (write your solution here)
def downcase_file_names(node):
    name = get_name(node)
    new_meta = copy.deepcopy(get_meta(node))
    if is_file(node):
        return mkfile(name.lower(), new_meta)
    children = get_children(node)
    new_children = list(map(downcase_file_names, children))
    tree = mkdir(name, new_children, new_meta)
    return tree


# END
tree = mkdir('/', [
    mkdir('eTc', [
        mkdir('NgiNx', [], {'size': 4000}),
        mkdir(
            'CONSUL',
            [mkfile('config.JSON', {'uid': 0})],
        ),
    ]),
    mkfile('HOSTS'),
])
new_tree = downcase_file_names(tree)
print (tree)
print(new_tree)
new_file = get_children(new_tree)[1]
get_name(new_file)  # hosts