# 🐳 Docker Command Reference

A quick reference of useful Docker commands for building, running, and pushing your AI agent app.

---

## 🛠️ 1. Build Docker Images

```bash
# Build local image named 'pyapp' using default Dockerfile
docker build -t pyapp .

# (Optional) Explicitly specify Dockerfile (same result as above)
docker build -f Dockerfile -t pyapp .

# Build image and tag for Docker Hub
docker build -t shahmeer123/ai-agent-app:latest .
```

> ⚠️ Note: Avoid this command — it contains a typo in the filename:
> ```bash
> docker build -f Docklerfile -t shahmeer123/ai-agent-app:latest  # Typo: 'Docklerfile'
> ```

---

## 🚀 2. Run Docker Containers

```bash
# Run 'pyapp' with a pseudo-TTY (non-interactive)
docker run -t -p pyapp

# Run 'pyapp' with interactive shell and TTY (recommended for development)
docker run -it pyapp

# Run the tagged Docker Hub image interactively
docker run -it shahmeer123/ai-agent-app:latest

docker run -it -p 3000:8000 pyapp
# Map port 8000 inside the container to port 3000 on my local machine (host)


```

---

## 🔐 3. Docker Hub: Login & Push

```bash
# Log in to Docker Hub
docker login

# Push 'pyapp' to Docker Hub (only works if tagged with Docker Hub username)
docker push pyapp

# Push properly tagged image to Docker Hub
docker push shahmeer123/ai-agent-app:latest
```

---

## ✅ Recommended Workflow

```bash
# Step 1: Build and tag image
docker build -t shahmeer123/ai-agent-app:latest .

# Step 2: Log in to Docker Hub
docker login

# Step 3: Push to Docker Hub
docker push shahmeer123/ai-agent-app:latest

# Step 4: Run the image
docker run -it shahmeer123/ai-agent-app:latest
```

