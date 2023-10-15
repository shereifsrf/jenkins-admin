# Use the official Alpine Linux as a parent image
FROM alpine:latest

# Install required dependencies
RUN apk --update add \
    curl \
    git \
    bash \
    build-base \
    zlib-dev \
    openssl-dev \
    ncurses-dev \
    readline-dev \
    bzip2-dev \
    sqlite-dev \
    python3-dev

# Install pyenv and initialize it
RUN curl https://pyenv.run | sh
RUN echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.profile
RUN echo 'eval "$(pyenv init --path)"' >> ~/.profile

# Set up pyenv environment variables for the shell session
RUN echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# Reload the shell to activate Pyenv
SHELL ["/bin/bash", "--login", "-c"]

# Install a specific version of Python
RUN pyenv install 3.12.0

# Set the installed Python version as global
RUN pyenv global 3.12.0

# Cleanup
RUN rm -rf /var/cache/apk/*

