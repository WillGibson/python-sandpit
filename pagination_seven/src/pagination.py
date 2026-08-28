from typeguard import typechecked


@typechecked
def paginate():
    raise CannotPaginateException


@typechecked
class CannotPaginateException(Exception):
    pass
