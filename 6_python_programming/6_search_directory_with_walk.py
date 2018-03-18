import os


def search_directory(dirname, search_ext):
    try:
        for (path, dir, files) in os.walk("c:/"):
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if search_ext:
                    if ext == ("." + search_ext):
                        print("%s/%s" % (path, filename))
                else:
                    print("%s/%s" % (path, filename))
    except PermissionError:
        pass


search_directory("c:/", "py")
