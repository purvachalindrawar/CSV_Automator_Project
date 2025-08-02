# CSV Automator Project – Dockerized

![Docker Pulls](https://img.shields.io/docker/pulls/chalindrawar19241/csv-processor)


A simple Python CLI tool to explore and search CSV files. Fully Dockerized for universal compatibility and easy sharing.

---

## Features

- View column names
- Preview first 5 rows
- Count total rows
- Search values in any column

---

## Docker Support

This project is fully containerized with Docker.

---


### Build the Docker Image

```bash
docker build -t csv-processor .
```

---

### Run the App Inside a Container
```bash
docker run -it csv-processor
```

---


### Run from DockerHub
```bash
docker pull chalindrawar19241/csv-processor
docker run -it chalindrawar19241/csv-processor
```

#### No setup needed. Just Docker installed and you're good to go
