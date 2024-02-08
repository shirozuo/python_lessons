def deep_first_search(my_dict, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(my_dict[vertex]) - set(visited))
    return visited


def get_dict():
    exception_dict = dict()
    for _ in range(int(input())):
        exception_input = input().strip().replace(":", "").split()
        exception, parents = exception_input[0], set(exception_input[1:])
        exception_dict[exception] = parents
    return get_full_parent_dict(exception_dict)


def get_full_parent_dict(_dict):
    full_exception_dict = dict()
    for parent in _dict:
        full_exception_dict[parent] = deep_first_search(_dict, parent)[1:]
    return full_exception_dict


def find_redundant_exceptions(exceptions_dict):
    exceptions = []
    redundant_exceptions = []
    for _ in range(int(input())):
        exception = input()
        if exception in exceptions and exception not in redundant_exceptions:
            redundant_exceptions.append(exception)
        else:
            exceptions.append(exception)
            for previous in exceptions:
                if previous in exceptions_dict[exception] and exception not in redundant_exceptions:
                    redundant_exceptions.append(exception)
                    break
    return redundant_exceptions


print("\n".join(find_redundant_exceptions(get_dict())))
