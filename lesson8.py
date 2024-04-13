def apply_diff(target, diff):
    target.update(diff.get['add'])
    target.difference_update(diff.get['remove'])

