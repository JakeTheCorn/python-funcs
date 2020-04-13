import copy

FALLBACK_FLAG = '____FALLBACK_FLAG'

def omit(obj, paths):
  if not isinstance(obj, dict):
    return obj
  collector = copy.deepcopy(obj)
  for path in paths:
    if '.' not in path:
      if collector.get(path):
        del collector[path]
      continue
    sub_paths = path.split('.')

    if len(sub_paths) < 2:
      continue

    first, rest = sub_paths[0], sub_paths[1:]
    val = collector.get(first, FALLBACK_FLAG)
    if val == FALLBACK_FLAG:
      continue
    collector[first] = omit(val, rest)

  return collector
