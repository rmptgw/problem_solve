from xml.etree import ElementTree
from urllib.request import urlopen

def get_distributions(simple_index='https://pypi.org/simple/'):
    with urlopen(simple_index) as f:
        tree = ElementTree.parse(f)
    return [a.text for a in tree.iter('a')]

def scrape_links(dist, simple_index='https://pypi.org/simple/'):
    with urlopen(simple_index + dist + '/') as f:
        tree = ElementTree.parse(f)
    return [a.attrib['href'] for a in tree.iter('a')]

b = get_distributions()
print(b)
