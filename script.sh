#!/bin/bash
echo "Setting up Jenkins on macOS..."

# Build Jenkins image
docker build -t jenkins-dind .

# Stop existing
docker stop jenkins-dind 2>/dev/null || true
docker rm jenkins-dind 2>/dev/null || true

# Run Jenkins
# docker run -d \
#   --name jenkins-dind \
#   -p 0.0.0.0:8080:8080 \
#   -p 0.0.0.0:50000:50000 \
#   -v jenkins_data:/var/jenkins_home \
#   -v /var/run/docker.sock:/var/run/docker.sock \
#   -u root \
#   jenkins-dind
docker run -d \
  --name jenkins-dind \
  --network dind-network \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_data:/var/jenkins_home \
  --privileged \
  -u root \
  jenkins-dind
echo "Waiting for Jenkins to start..."
sleep 30

# Get access information
MAC_IP=$(ipconfig getifaddr en0)
ADMIN_PASSWORD=$(docker exec jenkins-dind cat /var/jenkins_home/secrets/initialAdminPassword)

echo "=== Jenkins Access Information ==="
echo "Local access: http://localhost:8080"
echo "Network access: http://$MAC_IP:8080"
echo "Admin password: $ADMIN_PASSWORD"
echo "Computer name: $(scutil --get ComputerName)"