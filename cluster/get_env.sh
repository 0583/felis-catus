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

# kube
sudo groupadd microk8s
sudo usermod -a -G microk8s ubuntu
curl https://raw.githubusercontent.com/ycheng/microk8s-kubeflow-install/master/microk8s-install.bash > microk8s-install.sh
chmod + microk8s-install.sh
./microk8s-install.sh
microk8s.status --wait-ready

# file
curl https://raw.githubusercontent.com/0583/felis-catus/cluster/docker/docker-compose.yml > docker-compose.yml
curl https://raw.githubusercontent.com/0583/felis-catus/cluster/docker/run_docker_compose.sh > run_docker_compose.sh
chmod +x run_docker_compose.sh
./run_docker_compose.sh &
