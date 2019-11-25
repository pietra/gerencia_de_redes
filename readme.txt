Make sure to do this before deploying:

*** first, the swarm must have two nodes ('replicas' are hardcoded in docker-compose, modify for a bigger swarm);
*** the hosts can't have the same hostname (since we are running several instances of the same vm, all of them were named "gerencia-VirtualBox");
*** before deploying, create folders "/docker/appdata/firefox" in the host which will be used as a worker node;

WE'll be working in fixing these :)
