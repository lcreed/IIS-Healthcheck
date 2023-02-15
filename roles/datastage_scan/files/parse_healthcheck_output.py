#!/usr/bin/env python

import argparse
import json

from lxml.html import soupparser  # implicitly requires BeautifulSoup4
from lxml import etree

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'infile',
        type=argparse.FileType('r')
    )
    return parser.parse_args()

def main():
    args = get_args()
    tree = soupparser.parse(args.infile)
    td_cells = tree.xpath('//td[position() = 2]')
    results = list()
    for cell in td_cells:
        if cell.text and cell.text.startswith('CDIHC'):
            finding = dict()
            finding['id'] = cell.text.split(' ', 1)[0]
            finding['description'] = cell.text.split(' ', 1)[1]
            finding['severity'] = cell.getprevious().text_content().strip()
            results.append(finding)
    print(json.dumps(results))


if __name__ == "__main__":
    main()
