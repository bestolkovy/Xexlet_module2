def diff_keys(dic_old, dic_new):
    set_old = set(dic_old)
    set_new = set(dic_new)
    set_kept = set_old & set_new
    set_added = set_new - set_old
    set_removed = set_old - set_new
    result_dic = {'kept': set_kept,
                  'added': set_added,
                  'removed': set_removed}
    return result_dic
