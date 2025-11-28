#!/bin/bash
echo "Setting up Jenkins on ."

# Build Jenkins image
docker build -t jenkins-dind .

# Stop existing
docker stop jenkins-dind 2>/dev/null || true
docker rm jenkins-dind 2>/dev/null || true

echo "Creating network for Jenkins and SonarQube..."
docker network create dind-network
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
  --privileged \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_data:/var/jenkins_home \
  -v $(pwd):/workspace \
  -u root \
  jenkins-dind
echo "Waiting for Jenkins to start..."
sleep 30

echo "Setting up SONARQBUE on .."
docker run -d \
  --name sonarqube \
  --network dind-network \
  -p 9000:9000 \
  -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true \
  -v sonarqube_data:/opt/sonarqube/data \
  -v sonarqube_extensions:/opt/sonarqube/extensions \
  -v sonarqube_logs:/opt/sonarqube/logs \
  sonarqube:latest
# Get access information
MAC_IP=$(ipconfig getifaddr en0)
ADMIN_PASSWORD=$(docker exec jenkins-dind cat /var/jenkins_home/secrets/initialAdminPassword)

echo "=== Jenkins Access Information ==="
echo "Local access: http://localhost:8080"
echo "Network access: http://$MAC_IP:8080"
echo "Admin password: $ADMIN_PASSWORD"
echo "Computer name: $(scutil --get ComputerName)"