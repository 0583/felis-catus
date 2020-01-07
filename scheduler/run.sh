kubectl delete deployment nginx-deployment
kubectl delete nginx-service
kubectl create -f default_d.yaml
kubectl create -f custom_d.yaml
kubectl apply -f service.yaml