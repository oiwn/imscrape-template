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

and open http://localhost:8000


# TODO

- [ ] database post/update via. internal eve (+ validate data)
- [ ] add honcho
- [ ] init settings.py constants from environment
- [ ] add celery
