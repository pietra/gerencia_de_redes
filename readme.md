To run this application simply run in a terminal:

`$ ./run`

The application will:
- Start a docker swarm (the user will be prompted to add worker nodes mannually);
- Show a list of nodes sucefully added to the swarm;
- Deploy the application;
- Promt the user to choose from listed IPs to generate traffic statistics.

Make sure to do this before deploying:

- first, the swarm must have two nodes ('replicas' are hardcoded in docker-compose, modify for a bigger swarm);
- the hosts can't have the same hostname (since we are running several instances of the same vm, all of them were named "gerencia-VirtualBox");
- before deploying, create folders "/docker/appdata/firefox" in the host which will be used as a worker node;

We'll be working in fixing these :)
