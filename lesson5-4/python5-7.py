from hexlet.fs import get_children, get_meta, get_name, is_file, mkfile, mkdir


def du(tree):
    node = get_children(tree)
    name = get_name(node)
    print(name)
    if is_file(node):
        return (name, get_meta(node)['size'])
    kids = get_children(node[0])
    meta_sum = list(map(lambda q: du(q), kids))
    print(meta_sum)
               







tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])
du(tree)


