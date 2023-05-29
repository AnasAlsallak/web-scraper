import requests
from bs4 import BeautifulSoup
import json


def get_citations_needed_count(url):
    """
    This function takes in a url and returns the number of citations needed

    Args:
        url (str): url of the page

    Returns:
        int: number of citations needed
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_needed_citations = soup.find_all('a', title='Wikipedia:Citation needed')
    counter = 0

    for citation in all_needed_citations:
        counter = counter + 1

    return counter

# print(get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico'))

def get_citations_needed_report(url):
    """
    This function takes in a url and returns a report of the citations needed

    Args:
        url (str): url of the page

    Returns:
        str: report of citations needed
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    p_elements = soup.find_all('p')
    report = ""
    
    for p in p_elements:
        if p.find('a', title='Wikipedia:Citation needed'):
            text= p.text                                         
            # using ANSI escape sequences for color formatting to ease locating needed citation
            highlighted_text = text.replace('[citation needed]', '\033[93m[citation needed]\033[0m')
            report += highlighted_text + '\n'

    return report


def write_report(url):
    """
    This function takes in a url and writes the report of the citations needed in to a file

    Args:
        url (str): url of the page
    """
    report = "Report of citations needed:\n" + get_citations_needed_report(url)

    with open('report.txt', 'w') as f:
        f.write(report)


if __name__ == "__main__":
    write_report("https://en.wikipedia.org/wiki/History_of_Mexico")

    print("Number of citations needed:")
    print(get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico"))

    print("Report of citations needed:")
    print(get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico"))

