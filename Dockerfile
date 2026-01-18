# Utiliser une image Python officielle comme base
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système si nécessaire
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Copier le fichier requirements.txt
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu du projet
COPY app/ ./app/
COPY models/ ./models/

# Exposer le port sur lequel FastAPI va tourner
EXPOSE 8000

# Commande pour lancer l'application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

