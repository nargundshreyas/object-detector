# A general purpose utility script consisting number of useful methods.
# author: shreyasn

from six.moves.urllib.parse import urlparse

def is_url(path):
    try:
        result = urlparse(path)
        return result.scheme and result.netloc and result.path
    except:
        return False


def generate_colors(n, max_value=255):
    colors = []
    h = 0.1
    s = 0.5
    v = 0.95
    for i in range(n):
        h = 1 / (h + GOLDEN_RATIO)
        colors.append([c * max_value for c in colorsys.hsv_to_rgb(h, s, v)])

    return colors


def find_class_by_name(name, modules):
    modules = [getattr(module, name, None) for module in modules]
    return next(a for a in modules if a)
