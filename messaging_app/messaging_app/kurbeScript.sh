#!/bin/bash
# kurbeScript.sh
# Script to start Kubernetes cluster locally using Minikube (Docker driver)

set -e

echo "=== Checking dependencies ==="

# Check minikube
if ! command -v minikube &> /dev/null; then
	    echo "Minikube not found. Installing..."
	        curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
		    sudo install minikube-linux-amd64 /usr/local/bin/minikube
fi

# Check kubectl
if ! command -v kubectl &> /dev/null; then
	    echo "kubectl not found. Installing..."
	        sudo apt-get update -y
		    sudo apt-get install -y apt-transport-https ca-certificates curl
		        sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
			    echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
			        sudo apt-get update -y
				    sudo apt-get install -y kubectl
fi

# Check crictl
if ! command -v crictl &> /dev/null; then
	    echo "crictl not found. Installing..."
	        VERSION="v1.30.0"
		    wget https://github.com/kubernetes-sigs/cri-tools/releases/download/$VERSION/crictl-$VERSION-linux-amd64.tar.gz
		        sudo tar zxvf crictl-$VERSION-linux-amd64.tar.gz -C /usr/local/bin
			    rm crictl-$VERSION-linux-amd64.tar.gz
fi

echo "=== Starting Minikube cluster with Docker driver ==="
minikube start --driver=docker

echo "=== Verifying cluster status ==="
kubectl cluster-info

echo "=== Retrieving pods in all namespaces ==="
kubectl get pods -A

echo "=== Kubernetes setup complete! ==="

