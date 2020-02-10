help:		## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

build:		## Builds the container
	docker-compose build --no-cache

init:		## Initialize application
	docker-compose run web python manage.py migrate --noinput
	docker-compose run web python manage.py fetch

stop:		## Stops the stack
	docker-compose stop

run:		## Runs application on port 8000
	docker-compose up -d --build

fetch:	## Fetch exchange by hand
	docker-compose run web python manage.py fetch
