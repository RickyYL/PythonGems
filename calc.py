#!/usr/local/bin/python3

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import sys

def genURL(query, appid='X5R2R6-WRUUGRU6RU'):
	url = "http://api.wolframalpha.com/v2/query?input=" + query + "&appid=" + appid
	return url

def printResult(query):
	url = genURL(query)
	xml = urllib.request.urlopen(url)
	xml_tree = ET.parse(urllib.request.urlopen(url))
	xml_root = xml_tree.getroot()
	for child in xml_root:
		if child.tag == 'pod' and child[0][0].text:
			print('[' + child.get('title') + ']')
			print('\t' + child[0][0].text.replace('\n', '\n\t'))

if __name__ == '__main__':
	if len(sys.argv) > 1:
		printResult(urllib.parse.quote(sys.argv[1]))