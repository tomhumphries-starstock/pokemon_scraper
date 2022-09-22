# Pokemon Crawler

Project started from https://docs.docker.com/compose/django/

Some useful commands:

* `docker-compose up`
* `docker-compose exec web bash`
* `docker-compose exec web python -m pip install -r requirements.txt`

Access list of pokemon from http://0.0.0.0:8000/

Web scraper is currently configured very badly so refresh of page is slow while it scrapes data for next 5 available pokemon. Once db is full, it'd be faster but this needs fixing. 
Similarly, TDD approach was abandoned in exploratory phase of getting scraper working. This would also need rectifying.
