# Image de base
FROM python:3.12-slim

# Créer un dossier dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY app.py .
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Lancer le service Flask
CMD ["python", "app.py"]
