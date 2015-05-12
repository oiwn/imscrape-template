github_data_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'source_url': {
        'type': 'string',
        'required': True,
        'unique': True,
    },

    # github favorites
    'commits': {
        'type': 'number',
    },
    'watchers': {
        'type': 'number',
    },
    'forks': {
        'type': 'number',
    },
    'stars': {
        'type': 'number',
    },
    'author': {
        'type': 'string',
        'default': 'undefined',
    },
    'repo_name': {
        'type': 'string',
        'default': 'undefined',
    },
}
