from fastapi import FastAPI
from app.schemas import PredictionInput, KMeansInput
from app.models_loader import load_model
from app.predictors import make_prediction, make_kmeans_prediction

app = FastAPI(title="Prediction API V1 V2 V3")

model_v1 = load_model("models/logistic_regression_pipeline.pkl")
model_v2 = load_model("models/random_forest_pipeline.pkl")
model_v3 = load_model("models/gradient_boosting_pipeline.pkl")
model_kmeans = load_model("models/kmeans_cluster_pipeline.pkl")


@app.post("/predict/v1")
def predict_v1(data: PredictionInput):
    result = make_prediction(model_v1, data)
    churn = "oui" if result == 1 else "non"
    return {"version": "v1", "prediction": result, "churn": churn}


@app.post("/predict/v2")
def predict_v2(data: PredictionInput):
    result = make_prediction(model_v2, data)
    churn = "oui" if result == 1 else "non"
    return {"version": "v2", "prediction": result, "churn": churn}


@app.post("/predict/v3")
def predict_v3(data: PredictionInput):
    result = make_prediction(model_v3, data)
    churn = "oui" if result == 1 else "non"
    return {"version": "v3", "prediction": result, "churn": churn}

@app.post("/predict/kmeans")
def predict_kmeans(data: KMeansInput):
    result = make_kmeans_prediction(model_kmeans, data)
    return {"version": "kmeans", "cluster": result}
