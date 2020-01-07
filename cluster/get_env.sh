# docker
curl -fsSL https://get.docker.com -o get-docker.sh
chmod +x get-docker.sh
./get-docker.sh

# pip3
sudo apt-get install python3-pip

# docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

# file
curl https://github.com/0583/felis-catus/blob/cluster/docker/docker-compose.yml >> docker-compose.yml
curl https://github.com/0583/felis-catus/blob/cluster/docker/run_docker_compose.sh >> run_docker_compose.sh
chmod +x run_docker_compose.sh
./run_docker_compose.sh
