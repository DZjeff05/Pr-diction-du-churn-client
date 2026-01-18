# API de Prédiction du Churn Client

API REST développée avec FastAPI pour prédire le churn (attrition) des clients à l'aide de modèles de machine learning.

## 🚀 Démarrage rapide avec Docker

### Prérequis

- Docker installé sur votre machine ([Télécharger Docker](https://www.docker.com/get-started))

### Installation et lancement

1. **Cloner le dépôt** (si vous utilisez Git)
```bash
git clone <url-du-repo>
cd "Prediction du churn client"
```

2. **Construire l'image Docker**
```bash
docker build -t churn-prediction-api .
```

3. **Lancer le conteneur**
```bash
docker run -p 8000:8000 churn-prediction-api
```

4. **Accéder à l'API**
- Documentation interactive (Swagger UI) : http://localhost:8000/docs
- Documentation alternative (ReDoc) : http://localhost:8000/redoc
- API : http://localhost:8000

## 📦 Installation manuelle (sans Docker)

### Prérequis

- Python 3.11 ou supérieur
- pip

### Étapes

1. **Cloner le dépôt**
```bash
git clone <url-du-repo>
cd "Prediction du churn client"
```

2. **Créer un environnement virtuel** (recommandé)
```bash
python -m venv venv
# Sur Windows
venv\Scripts\activate
# Sur Linux/Mac
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Lancer l'application**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 🔌 Endpoints disponibles

### Prédiction du churn (modèles supervisés)

L'API propose 3 versions de modèles pour la prédiction du churn :

- **POST** `/predict/v1` - Modèle de régression logistique
- **POST** `/predict/v2` - Modèle Random Forest
- **POST** `/predict/v3` - Modèle Gradient Boosting

#### Paramètres d'entrée

```json
{
  "Call  Failure": 0,
  "Complains": 0,
  "Subscription  Length": 10,
  "Charge  Amount": 10.5,
  "Seconds of Use": 1000.0,
  "Frequency of use": 5,
  "Frequency of SMS": 3,
  "Distinct Called Numbers": 10,
  "Age": 30,
  "Customer Value": 150.0
}
```

#### Réponse

```json
{
  "version": "v1",
  "prediction": 0,
  "churn": "non"
}
```

### Clustering KMeans

- **POST** `/predict/kmeans` - Prédiction du cluster client

#### Paramètres d'entrée

```json
{
  "Age": 35,
  "Gender": "M",
  "Annual_Income": 50000.0,
  "Total_Spend": 2000.0,
  "Years_as_Customer": 3,
  "Num_of_Purchases": 15,
  "Average_Transaction_Amount": 133.33,
  "Num_of_Returns": 1,
  "Num_of_Support_Contacts": 0,
  "Satisfaction_Score": 4,
  "Last_Purchase_Days_Ago": 30,
  "Promotion_Response": "Yes"
}
```

#### Réponse

```json
{
  "version": "kmeans",
  "cluster": 1
}
```

## 📝 Exemple d'utilisation avec cURL

### Prédiction du churn (v1)
```bash
curl -X POST "http://localhost:8000/predict/v1" \
  -H "Content-Type: application/json" \
  -d '{
    "Call  Failure": 0,
    "Complains": 0,
    "Subscription  Length": 10,
    "Charge  Amount": 10.5,
    "Seconds of Use": 1000.0,
    "Frequency of use": 5,
    "Frequency of SMS": 3,
    "Distinct Called Numbers": 10,
    "Age": 30,
    "Customer Value": 150.0
  }'
```

### Clustering KMeans
```bash
curl -X POST "http://localhost:8000/predict/kmeans" \
  -H "Content-Type: application/json" \
  -d '{
    "Age": 35,
    "Gender": "M",
    "Annual_Income": 50000.0,
    "Total_Spend": 2000.0,
    "Years_as_Customer": 3,
    "Num_of_Purchases": 15,
    "Average_Transaction_Amount": 133.33,
    "Num_of_Returns": 1,
    "Num_of_Support_Contacts": 0,
    "Satisfaction_Score": 4,
    "Last_Purchase_Days_Ago": 30,
    "Promotion_Response": "Yes"
  }'
```

## 📚 Documentation interactive

Une fois l'API lancée, vous pouvez accéder à la documentation interactive :
- **Swagger UI** : http://localhost:8000/docs
- **ReDoc** : http://localhost:8000/redoc

Ces interfaces vous permettent de tester l'API directement depuis votre navigateur.

## 🏗️ Structure du projet

```
.
├── app/
│   ├── main.py              # Point d'entrée de l'API FastAPI
│   ├── schemas.py           # Schémas de validation des données
│   ├── models_loader.py     # Chargement des modèles
│   └── predictors.py        # Fonctions de prédiction
├── models/                  # Modèles entraînés (.pkl)
├── data/                    # Données d'entraînement
├── requirements.txt         # Dépendances Python
├── Dockerfile              # Configuration Docker
└── README.md               # Ce fichier
```

## 📋 Dépendances principales

- FastAPI - Framework web moderne pour l'API
- Uvicorn - Serveur ASGI
- scikit-learn - Bibliothèque de machine learning
- pandas - Manipulation de données
- numpy - Calculs numériques
- pydantic - Validation des données

## 🐳 Docker

Le projet inclut un `Dockerfile` pour faciliter le déploiement. Le fichier `.dockerignore` optimise la construction de l'image en excluant les fichiers non nécessaires.



