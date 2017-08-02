# -*- coding: utf-8 -*-
import re
import scrapy
from pyquery import PyQuery
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import Escuela

COORD = re.compile(r'"lat"\:(?P<lat>\-?\d{2}\.\d+),"lon"\:(?P<lon>\-?\d{2}\.\d+)', flags=re.MULTILINE)

provincias_slugs = '|'.join(['buenos\-aires', 'catamarca', 'chaco', 'chubut', 'ciudad\-de\-buenos\-aires', 'cordoba', 'corrientes', 'entre\-rios', 'formosa', 'jujuy', 'la\-pampa', 'la\-rioja', 'mendoza', 'misiones', 'neuquen', 'rio\-negro', 'salta', 'san\-juan', 'san\-luis', 'santa\-cruz', 'santa\-fe', 'santiago\-del\-estero', 'tierra\-del\-fuego', 'tucuman'])


class EscuelasSpider(CrawlSpider):
    name = 'escuelas'
    allowed_domains = ['escuelasarg.com']
    start_urls = ['http://escuelasarg.com']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=(f'{provincias_slugs}(/[\w-]*)?',))),
        Rule(LinkExtractor(allow=('cue/\d+/.*',)), callback='parse_item'),
    )

    def parse_item(self, response):
        pq = PyQuery(response.text)
        nombre = pq('h1').text()
        info1 = pq('div.info-establ div.columns:first')
        info2 = pq('div.info-establ div.columns:last')
        try:
            lat, lon = re.findall(COORD, response.text)[0]
        except IndexError:
            lat, lon = '', ''
        escuela = Escuela(nombre=nombre, lat=lat, lon=lon)
        for pos, field in enumerate(('jurisdiccion', 'departamento', 'localidad', 'domicilio')):
            escuela[field] = pq(f'p:eq({pos}) label.info', info1).text()
        for pos, field in enumerate(('sector', 'telefono', 'email', 'codigo_postal')):
            escuela[field] = pq(f'p:eq({pos}) label.info', info2).text()
        escuela['tags'] = ', '.join(e.text for e in pq('i.fi-check + h2, i.fi-check + label'))
        yield escuela

