help:		## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'


build:		## Builds the stack
	docker-compose build

stop:		## Stops the stack
	docker-compose stop

propagate:	## Fetch exchange by hand
	docker run -it web python manage.py fetch

run:		## Runs application on port 8000
	docker-compose up -d
