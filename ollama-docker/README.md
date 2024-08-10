# Setting up Ollama in Docker
This setup was tested with WSL2 in Windows 11.

## Prerequisites
- Latest version of Docker Desktop (for Windpws)
- Latest version of Docker Engine and Docker Compose (for Linux)
- Confirmed GPU support in Docker (Refer to the [Docker documentation](https://docs.docker.com/desktop/gpu/) for more information)

## First Time Setup
1. Clone the repository if you have not done so already.
2. Copy `.env.copy` to `.env` and fill in the values as described in the comments.
3. Follow the [Operational Commands](#operational-commands) to start the container.

## Operational Commands
```bash
# Move to the docker file directory
cd ollama-docker

# Run the docker compose file
docker compose up -d

# Once done with the container, you can stop it
docker compose down
```

### CPU-only mode
If you want to run the Ollama container in CPU-only mode, you may use the `compose.cpu.yml` file instead of the default `compose.yml` file. To do so, append `-f compose.cpu.yml` to the `docker compose` command.

Example:
```bash
docker compose -f compose.cpu.yml up -d
```