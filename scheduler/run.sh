# microk8s.add-node

kubectl create -f rbac.yaml
kubectl create -f custom_deployment.yaml
kubectl create -f felisdb-deployment.yaml
kubectl create -f server-deployment.yaml
kubectl apply -f felisdb-service.yaml
kubectl apply -f server-service.yaml
kubectl create -f deployment.yaml