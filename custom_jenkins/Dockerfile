FROM jenkins/jenkins:lts

# Set environment to non-interactive
ENV DEBIAN_FRONTEND=noninteractive
ENV TERM=xterm

USER root

# Install Docker client without interactive prompts
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    docker.io \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add Jenkins user to docker group
RUN usermod -aG docker jenkins

USER jenkins