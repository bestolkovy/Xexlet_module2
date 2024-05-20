def make_module(step=1):
    return {'inc': lambda x: x+step, 'dec': lambda x: x-step}


a = make_module(4)
print(a['dec'](10))