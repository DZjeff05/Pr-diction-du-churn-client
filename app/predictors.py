import pandas as pd
from app.schemas import PredictionInput, KMeansInput

COLUMNS = [
    "Call  Failure",
    "Complains",
    "Subscription  Length",
    "Charge  Amount",
    "Seconds of Use",
    "Frequency of use",
    "Frequency of SMS",
    "Distinct Called Numbers",
    "Age",
    "Customer Value"
]

KMEANS_COLUMNS = [
    "Annual_Income",
    "Total_Spend",
    "Years_as_Customer",
    "Num_of_Purchases",
    "Average_Transaction_Amount",
    "Num_of_Returns",
    "Num_of_Support_Contacts",
    "Last_Purchase_Days_Ago",
    "Age",
    "Satisfaction_Score",
    "Gender",
    "Promotion_Response"
]
CLUSTER_NAMES = {
    0: "Clients Fidèles",
    1: "Clients à Risque",
    2: "Clients Volatils"
}





def make_prediction(model, data: PredictionInput):
    row = {
        "Call  Failure": data.call_failure,
        "Complains": data.complains,
        "Subscription  Length": data.subscription_length,
        "Charge  Amount": data.charge_amount,
        "Seconds of Use": data.seconds_of_use,
        "Frequency of use": data.frequency_of_use,
        "Frequency of SMS": data.frequency_of_sms,
        "Distinct Called Numbers": data.distinct_called_numbers,
        "Age": data.age,
        "Customer Value": data.customer_value
    }

    df = pd.DataFrame([row], columns=COLUMNS)

    prediction = model.predict(df)
    return prediction[0].item()


def prepare_kmeans_input(data) -> pd.DataFrame:

    df = pd.DataFrame([{
        "Satisfaction_Score": data.Satisfaction_Score,
        "Annual_Income": data.Annual_Income,
        "Total_Spend": data.Total_Spend,
        "Years_as_Customer": data.Years_as_Customer,
        "Num_of_Purchases": data.Num_of_Purchases,
        "Average_Transaction_Amount": data.Average_Transaction_Amount,
        "Num_of_Returns": data.Num_of_Returns,
        "Num_of_Support_Contacts": data.Num_of_Support_Contacts,
        "Last_Purchase_Days_Ago": data.Last_Purchase_Days_Ago,
        "Age": data.Age,
        "Gender": data.Gender,
        "Promotion_Response": data.Promotion_Response
    }])

    return df


def make_kmeans_prediction(model, data):
    df = prepare_kmeans_input(data)

    cluster_id = int(model.predict(df)[0])

    return {
        "cluster": cluster_id,
        "cluster_label": CLUSTER_NAMES.get(cluster_id, "Inconnu")
    }

