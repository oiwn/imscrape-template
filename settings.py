"""
Config file for REST API and Scraperss
"""
import os
import sys
import logging

from pymongo import MongoClient
from schemas.github import github_data_schema


DEBUG = True
LOG_LEVEL = logging.DEBUG

DB_NAME = 'imscrape'

# http://docs.mongodb.org/manual/reference/connection-string/
DB_URI = 'mongodb://localhost:27017/{}'.format(DB_NAME)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

TASKS = {
    'github': 'scrapers.github.GithubFavoritesScraper',
}

EVE_CONFIG = {
    'MONGO_URI': DB_URI,
    'PAGINATION_DEFAULT': 10,
    'DOMAIN': {
        'github_favorites': {
            'schema': github_data_schema,
            'resource_methods': ['GET'],
        }
    }
}

SCRAPER_CONFIG = {
    'thread_number': 3,
    'network_try_limit': 3,
    'task_try_limit': 3,
    'max_task_generator_chunk': 3,
    'priority_mode': 'const',
}


def db_connection():
    client = MongoClient('mongodb://localhost:27017/')
    return client[DB_NAME]
