


def debug(f):
    def new_f(*args, **kargs):
        print("antes de f")
        ret = f(*args, **kargs)
        print("depois de f (ret ->", ret, ")")
        return ret
    return new_f


def soma(a, b):
    return a + b

