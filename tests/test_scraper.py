import pytest
from web_scraper.scraper import get_citations_needed_report, get_citations_needed_count

# Happy path test 1: Valid URL with citations needed
def test_get_citations_needed_report():
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    report = get_citations_needed_report(url)
    assert isinstance(report, str)
    assert len(report) > 0

# Happy path test 2: Valid URL with citations needed
def test_get_citations_needed_count():
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    count = get_citations_needed_count(url)
    assert isinstance(count, int)
    assert count > 0

# Expected failure test 1: Invalid URL
def test_get_citations_needed_report_invalid_url():
    url = "https://en.wikipedia.org/nonexistent"
    report = get_citations_needed_report(url)
    assert report == ""

# Edge case test 1: URL without citations needed
def test_get_citations_needed_report_no_citations():
    # note that this wikipedia page don't have citation needed <p>
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    report = get_citations_needed_report(url)
    assert report == ""

# Edge case test 2: Empty URL
def test_get_citations_needed_report_empty_url():
    url = ""
    report = get_citations_needed_report(url)
    assert report == ""

# Edge case test 3: URL with no internet connection
def test_get_citations_needed_report_no_connection():
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    # Simulate no internet connection by disconnecting the internet manually
    with pytest.raises(ConnectionError):
        get_citations_needed_report(url)
