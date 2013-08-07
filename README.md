# jeanweaves.com Project

## Features ToDo

* tumblr integration
* google analytics
* image management (flickr integration)
* image rollover to detail
* exhibits management or i18n

## Tech ToDo

* cache pages to keep them static-like
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
