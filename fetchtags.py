from lxml import etree
import resource

def parse(fp):
    context = etree.iterparse(fp, events=('end',))

    tags = []

    for action, elem in context:
        if elem.tag not in tags:
            tags.append(elem.tag)
        # if elem.tag=='label':
        #     print elem

        # cleanup
        elem.clear()
        while elem.getprevious() is not None:
            del elem.getparent()[0]

    print tags

parse("data/releases.xml")
