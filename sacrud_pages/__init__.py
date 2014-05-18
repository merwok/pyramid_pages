#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.
__version__ = "0.0.1a"


def includeme(config):
    config.include('pyramid_jinja2')
    config.add_jinja2_search_path("sacrud_pages:templates")
    config.add_static_view('/static_sacrud_pages', 'sacrud_pages:static/sacrud_pages/')

    config.include('sacrud_pages.routes')
    config.scan()
