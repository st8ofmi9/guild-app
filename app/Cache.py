import requests

def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            print("Retrieving from Cache")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func

@memoize
def get_content(url):
    r = requests.get(url)
    return r