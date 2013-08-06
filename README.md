# jeanweaves.com Project

## Features ToDo

* tumblr integration
* image management (flickr integration)
* image rollover to detail
* exhibits management or i18n

## Tech ToDo

* Put heroku Procfile/requirements on a long-running branch
  * deployments/heroku_staging
  * deployments/heroku_prod
* Make navigation less redundant
* check all templates for missing i18n
* cache pages to keep them static-like
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
