class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, __object):
        if __object > 0:
            super().append(__object)
        else:
            raise NonPositiveError()