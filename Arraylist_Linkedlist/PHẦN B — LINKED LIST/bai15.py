from collections import OrderedDict

cache = OrderedDict()

cache[1]=10

cache[2]=20

print(cache)

cache.move_to_end(1)

print(cache)