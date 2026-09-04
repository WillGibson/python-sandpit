from pagination_seven.src.pagination import paginate


class TestPagination:

    def test_paginate_highlights_current_page(self):
        assert paginate(total_pages=5, current_page=2) == "1 (2) 3 4 5"

    def test_paginate_shows_seven_pages(self):
        assert paginate(total_pages=7, current_page=6) == "1 2 3 4 5 (6) 7"

    def test_paginate_elides_pages_before_the_current_page(self):
        assert paginate(total_pages=8, current_page=5) == "1 … 4 (5) 6 7 8"

    def test_paginate_elides_pages_after_the_current_page(self):
        assert paginate(total_pages=8, current_page=4) == "1 2 3 (4) 5 … 8"

    def test_paginate_elides_pages_before_and_after_the_current_page(self):
        assert paginate(total_pages=9, current_page=5) == "1 … 4 (5) 6 … 9"

    # Todo: Next up!
    # def test_paginate_doesnt_elides_pages_before_if_not_needed(self):
    #     assert paginate(total_pages=9, current_page=2) == "1 (2) 3 4 5 … 9"
