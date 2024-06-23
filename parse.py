#!/usr/bin/env python3

import sys
from amazon_page_parser.parsers import DetailParser

def parse_page(page_path):

    with open(page_path, 'r') as f:
        c = f.read()

    parser = DetailParser(c)

    data = dict(
        title = parser.parse_title(),
        authors = parser.parse_author(),
        feature_bullets = parser.parse_feature_bullets(),
        book_description = parser.parse_book_description(),
        product_description = parser.parse_product_description(),
        images = parser.parse_images(),
        rating = parser.parse_star(),
        reviews = parser.parse_reviews(),
        rank = parser.parse_rank(),
        cats = parser.parse_categories(),
        details = parser.parse_details(),
    )

    for key, val in data.items():
        print(f"{key}: {val}")

parse_page(sys.argv[1])
