import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


def compress_images(tree):
    children = get_children(tree)

    def reducicate(node):
        name = get_name(node)
        if name.endswith('.jpg') and is_file(node):
            meta = get_meta(node)
            new_meta = copy.deepcopy(meta)
            new_meta['size'] //= 2
            return mkfile(name, new_meta)
        else:
            return node

    kids = map(reducicate, children)
    new_meta = copy.deepcopy(get_meta(tree))
    return mkdir(get_name(tree), list(kids), new_meta)

 

tree = mkdir(
        'my documents',
        [
            mkdir('documents.jpg'),
            mkfile('avatar.jpg', {'size': 100}),
            mkfile('passport.jpg', {'size': 200}),
            mkfile('family.jpg', {'size': 150}),
            mkfile('addresses', {'size': 125}),
            mkdir('assets'),
        ],
        {'test': 'haha'},
    )

compress_images(tree)
#print(tree)
# END
