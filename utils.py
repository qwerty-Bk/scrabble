
def find_owner(name, method, it):
    try:
        return next(
            i for i in it.__class__.__mro__ if i.__dict__.get(name, None) is method)
    except StopIteration:
        raise KeyError

_ERR_MSG = "{0}::{1} is not implemented in {2}"
def virtual(method):
    def _f(self, *args, **kwargs):
        raise NotImplementedError(
            _ERR_MSG.format(
                find_owner(
                    method.__name__,
                    _f, self
                ).__name__,
                method.__name__,
                self.__class__
                    .__name__
            )
        )
    return _f
