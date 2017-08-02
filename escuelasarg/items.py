# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Escuela(scrapy.Item):
    # define the fields for your item here like:
    nombre = scrapy.Field()
    jurisdiccion = scrapy.Field()
    departamento = scrapy.Field()
    localidad = scrapy.Field()
    domicilio = scrapy.Field()
    sector = scrapy.Field()
    telefono = scrapy.Field()
    email = scrapy.Field()
    codigo_postal = scrapy.Field()
    lat = scrapy.Field()
    lon = scrapy.Field()
    tags = scrapy.Field()

