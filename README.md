# What is it?

Default template for my scraping project. Usually it's few scrapers + REST API on top for JavaScript/Mobile frontend
or another service to consume.

# Featured by

+ Grab Framework
+ Python EVE (based on Flask framework)

# How to use

clone repo

```bash
git clone https://github.com/istinspring/imscrape-template
cd imscrape-template
```

install project dependencies

```bash
pip install -r requirements.txt
```

run test scraper

```bash
python cli.py -T github
```

run REST api

```bash
python api.py
```

and open http://localhost:8000 (both json and xml supported via content-type header)

```xml
<resource href="github_favorites" title="github_favorites">
    <link rel="last" href="github_favorites?page=3" title="last page"/>
    <link rel="next" href="github_favorites?page=2" title="next page"/>
    <link rel="parent" href="/" title="home"/>
    <_meta>
        <max_results>10</max_results>
        <page>1</page>
        <total>25</total>
    </_meta>

    <resource href="github_favorites/555179e74dc7822d62abc2b5" title="Github_favorite">
        <_created>Tue, 12 May 2015 03:56:23 GMT</_created>
        <_etag>83dc8829ef61dfeb52111e04cb04a6e534b36810</_etag>
        <_id>555179e74dc7822d62abc2b5</_id>
        <_updated>Tue, 12 May 2015 03:56:23 GMT</_updated>
        <author>https://github.com/square</author>
        <commits>29</commits>
        <forks>120</forks>
        <repo_name>leakcanary</repo_name>
        <source_url>https://github.com/square/leakcanary</source_url>
        <stars>2116</stars>
        <watchers>155</watchers>
    </resource>

    ...
</resource>
```


# TODO

- [ ] database post/update via. internal eve (+ validate data)
- [ ] add honcho
- [ ] init settings.py constants from environment
- [ ] add celery
