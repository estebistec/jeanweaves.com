# jeanweaves.com Project

## Useful commands

```PYTHONPATH=. django-admin.py collectstatic --noinput --ignore=jeanweaves_public/static/img --settings=jeanweaves.settings.heroku_staging```

## Features ToDo

* google analytics
* image management (flickr integration)
* image rollover to detail
* exhibits management or i18n

## Tech ToDo

* remove all font files for now :/
* upgrade to bootstrap 3.0, and use less of it -OR- try a responsive grid component + reset
* only load blog CSS on blog post list
* check all templates for missing i18n
* bring local-dev in line with deployment
  * e.g., env vars and postactivate scripts to set them
* error log emailing

* general django setup: https://devcenter.heroku.com/articles/django
* staticfiles: https://devcenter.heroku.com/articles/django-assets
  * djstatic or s3boto?
  * django-pipeline + django-twitter-bootstrap
* remove bootstrap classes from markup, use mixins to adapt jeanwaves classes
* give jeanweaves classes a good prefixs (smacss/bem?)
* sentry
* statsd
* splunk
