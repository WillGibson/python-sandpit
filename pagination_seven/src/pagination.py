from typing import LiteralString

from typeguard import typechecked


@typechecked
def paginate(total_pages: int, current_page: int):

    before: range = range(1, current_page)
    after: range = range(current_page + 1, total_pages + 1)

    return f"{elide_pages(before, total_pages)} ({current_page}) {elide_pages(after, total_pages)}"


def elide_pages(pages: range, total_pages: int) -> str | LiteralString:
    if len(pages) > 3 and total_pages > 7:
        return f"{pages[0]} … {pages[-1]}"
    else:
        return " ".join(map(str, pages))
