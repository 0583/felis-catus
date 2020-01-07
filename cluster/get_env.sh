# transfer
sudo apt-get update
sudo apt-get install lrzsz

# docker
curl -fsSL https://get.docker.com -o get-docker.sh
chmod +x get-docker.sh
./get-docker.sh

echo "docker installed"

# pip3
sudo apt-get install python3-pip

echo "pip3 installed"

# docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

echo "docker-compose installed"

# kube
sudo groupadd microk8s
curl https://raw.githubusercontent.com/ycheng/microk8s-kubeflow-install/master/microk8s-install.bash > microk8s-install.sh
chmod +x microk8s-install.sh
sudo ./microk8s-install.sh
sudo usermod -a -G microk8s ubuntu
microk8s.status --wait-ready

echo "microkube installed"

# file
curl https://raw.githubusercontent.com/0583/felis-catus/cluster/docker/docker-compose.yml > docker-compose.yml
curl https://raw.githubusercontent.com/0583/felis-catus/cluster/docker/run_docker_compose.sh > run_docker_compose.sh
chmod +x run_docker_compose.sh
sudo ./run_docker_compose.sh &

echo "app running"
