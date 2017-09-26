import re
def words(str):
    def remove_empty_strings(listelems):
        # return list(filter(lambda x: x != '', listelems))
        return [s for s in listelems if s != '']
    res = re.split('\s+',str)
    return remove_empty_strings(res)
