FROM jenkins/jenkins:lts

USER root

# Install Docker for DinD
RUN apt-get update && \
    apt-get install -y \
    docker.io \
    curl \
    unzip

# Install AWS CLI for ARM64
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip aws

# Add jenkins user to docker group
RUN usermod -aG docker jenkins

# Start Docker daemon when container starts
CMD ["sh", "-c", "dockerd & /usr/local/bin/jenkins.sh"]

USER jenkins