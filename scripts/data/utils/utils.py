import os

def search_walk(info):
    searched_list = []
    root_path = info.get('path')
    extension = info.get('extension')
    for (path, dir, files) in os.walk(root_path):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == extension:
                list_file = ('%s/%s' % (path, filename))
                searched_list.append(list_file)

    if searched_list:
        return searched_list
    else:
        return False