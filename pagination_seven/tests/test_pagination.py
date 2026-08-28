import pytest

from pagination_seven.src.pagination import paginate, CannotPaginateException


class TestThing:

    def test_paginate_raises_cannot_paginate_exception(self):
        with pytest.raises(CannotPaginateException):
            paginate()
