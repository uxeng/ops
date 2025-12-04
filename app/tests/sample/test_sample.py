import pytest
from app import App   

def test_initialization():
    book = App("1984", "George Orwell", 328)
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.pages == 328
    assert book.tags == []

def test_add_tag():
    book = App("Dune", 412)
    book.add_tag("sci-fi")
    book.add_tag("classic")
    assert "sci-fi" in book.tags
    assert "classic" in book.tags
    assert len(book.tags) == 2

def test_has_tag():
    book = App("ABC", 310, tags=["CDF"])
    assert book.has_tag("fantasy") is True
    assert book.has_tag("adventure") is False

def test_summary():
    book = App("The Catcher in the Rye", "J.D. Salinger", 214)
    expected = "'The Catcher in the Rye' by J.D. Salinger, 214 pages."
    assert book.summary() == expected
