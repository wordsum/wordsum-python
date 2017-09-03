# wordsum containers

This is file directory that will contain the container 
creators to host wordsum, its trained models and the data.

While these are now Dockerfiles, rewriting to docker-compose or some other
method of communicatation with environments can wait until
beyond POC.

# List of conatains

## Dockerfile.model (under construction) 

A container with a standard user wordsum that has a root directory call 'models' and contains exiting models that can be stored on the docker container the made into an image, tagged for version and stored for later use.

This should allow for the distribution of the models too.

Automation steps define in these steps (TODO: automate):
	1. https://www.digitalocean.com/community/tutorials/how-to-work-with-docker-data-volumes-on-ubuntu-14-04
	2. https://stackoverflow.com/questions/44480740/how-to-saving-a-docker-container-state

## Dockerfile.worsum (underconstriction)
A container contained the latest release of wordsum with an open point for an endpoint to send the text and return it modelled.



# Model versioning with tags.
(Under construction)





