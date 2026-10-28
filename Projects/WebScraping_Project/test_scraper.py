import os
import sys

sys.path.append(os.path.dirname(__file__))
from Books_Scraper import parse_books


SAMPLE_HTML = """
<html>
<body>
    <article class="product_pod">
        <h3><a href="catalogue/a-light-in-the-attic_1000/index.html"
               title="A Light in the Attic">A Light in the ...</a></h3>
        <p class="star-rating Three">
            <i class="icon-star"></i>
        </p>
        <p class="price_color">£51.77</p>
        <p class="instock availability">
            <i class="icon-ok"></i>
            In stock
        </p>
    </article>
    <article class="product_pod">
        <h3><a href="catalogue/tipping-the-velvet_999/index.html"
               title="Tipping the Velvet">Tipping the ...</a></h3>
        <p class="star-rating One">
            <i class="icon-star"></i>
        </p>
        <p class="price_color">Â£53.74</p>
        <p class="instock availability">
            <i class="icon-ok"></i>
            In stock
        </p>
    </article>
</body>
</html>
"""


def test_parse_books_valid():
    books = parse_books(SAMPLE_HTML)
    assert len(books) == 2

    first = books[0]
    assert first["Title"] == "A Light in the Attic"
    assert first["Price_GBP"] == 51.77
    assert first["Rating"] == "Three"
    assert "In stock" in first["Availability"]

    second = books[1]
    assert second["Title"] == "Tipping the Velvet"
    assert second["Price_GBP"] == 53.74
    assert second["Rating"] == "One"


def test_parse_books_empty_or_none():
    assert parse_books("") == []
    assert parse_books(None) == []


def test_parse_books_no_matching_elements():
    html = "<div><p>No products on this page</p></div>"
    assert parse_books(html) == []

