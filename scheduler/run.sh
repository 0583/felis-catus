kubectl create -f felisdb-deployment.yaml
kubectl create -f server-deployment.yaml
kubectl apply -f felisdb-service.yaml
kubectl apply -f server-service.yaml