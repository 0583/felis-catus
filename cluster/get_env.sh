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

# kube
sudo groupadd microk8s
curl https://raw.githubusercontent.com/ycheng/microk8s-kubeflow-install/master/microk8s-install.bash > microk8s-install.sh
chmod +x microk8s-install.sh
sudo ./microk8s-install.sh
sudo usermod -a -G microk8s ubuntu
microk8s.status --wait-ready

echo "microkube installed"

# files
mkdir yamls
curl https://raw.githubusercontent.com/0583/felis-catus/cluster/scheduler/yamls/felisdb-deployment.yaml > felisdb-deployment.yaml
curl https://raw.githubusercontent.com/0583/felis-catus/cluster/scheduler/yamls/felisdb-service.yaml > felisdb-service.yaml
curl https://raw.githubusercontent.com/0583/felis-catus/cluster/scheduler/yamls/server-deployment.yaml > server-deployment.yaml
curl https://raw.githubusercontent.com/0583/felis-catus/cluster/scheduler/yamls/server-service.yaml > server-service.yaml

sudo kubectl create -f felisdb-deployment.yaml
sudo kubectl create -f server-deployment.yaml
sudo kubectl apply -f felisdb-service.yaml
sudo kubectl apply -f server-service.yaml
