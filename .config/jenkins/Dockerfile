# Use the official Jenkins LTS image as the base image
FROM jenkins/jenkins:2.414.2-jdk17

# Switch to root user to perform system-level installations
USER root

# Install lsb-release for distribution info
RUN apt-get update && apt-get install -y lsb-release

# Add Docker GPG key and repository to the system
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg && \
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list

# Update package repository and install Docker CLI
RUN apt-get update && apt-get install -y docker-ce-cli

# Switch back to the jenkins user
USER jenkins

# Install Jenkins plugins "blueocean" and "docker-workflow"
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"
