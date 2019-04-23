from lxml import html
from lxml import etree
import requests

page_html = requests.get("http://localhost:8082/planets.html").text

tree = html.fromstring(page_html)

a = [tr for tr in tree.xpath("/html/body/div/table/tr")]

"XPath [1] is the first element. It doesn't use 0!"
print([etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div[1]/table/tr[@class='planet']")])
print([etree.tostring(tr) for tr in tree.xpath("/html/body/div/table/tr[@name='Venus']/td[5]")])
print([etree.tostring(tr) for tr in tree.xpath("/html/body/div/table/tr/parent::*")])

venus_diameter = tree.xpath("/html/body/div/table/tr[@name='Venus']/td[4]/text()[1]")[0].strip()
print(venus_diameter)