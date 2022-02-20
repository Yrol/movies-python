# Building the project
build:
	docker-compose build

# Wake up docker containers
up:
	docker-compose up -d

# Shut down docker containers
down:
	docker-compose down

# Show a status of each container
status:
	docker-compose ps	

#-----------------------------------------------------------
# Clearing containers
#-----------------------------------------------------------

# Shut down and remove all volumes
remove-volumes:
	docker-compose down --volumes

# Remove all existing networks (useful if network already exists with the same attributes)
prune-networks:
	docker network prune

# Clear cache
prune-a:
	docker system prune -a

#force prune
prune-f:
	docker system prune -af

#-----------------------------------------------------------
# Create superusers
#-----------------------------------------------------------
createsuperuser:
	docker-compose run app sh -c "python manage.py createsuperuser"

createapp:
ifdef name
	docker-compose run app sh -c 'python manage.py startapp $(name)'
else
	@echo 'You must specify the app name'
endif

#-----------------------------------------------------------
# Make migrations
#-----------------------------------------------------------
makemigrations:
	docker-compose run app sh -c "python manage.py makemigrations"

#-----------------------------------------------------------
# Make migrations
#-----------------------------------------------------------
migrate:
	docker-compose run app sh -c "python manage.py migrate"
