from pydantic import BaseModel, Field,conint, constr, validator

class PredictionInput(BaseModel):
    call_failure: int = Field(..., alias="Call  Failure")
    complains: int = Field(..., alias="Complains")
    subscription_length: int = Field(..., alias="Subscription  Length")
    charge_amount: float = Field(..., alias="Charge  Amount")
    seconds_of_use: float = Field(..., alias="Seconds of Use")
    frequency_of_use: int = Field(..., alias="Frequency of use")
    frequency_of_sms: int = Field(..., alias="Frequency of SMS")
    distinct_called_numbers: int = Field(..., alias="Distinct Called Numbers")
    age: int = Field(..., alias="Age")
    customer_value: float = Field(..., alias="Customer Value")

    class Config:
        populate_by_name = True




class KMeansInput(BaseModel):
    Age: int
    Gender: str
    Annual_Income: float
    Total_Spend: float
    Years_as_Customer: int
    Num_of_Purchases: int
    Average_Transaction_Amount: float
    Num_of_Returns: int
    Num_of_Support_Contacts: int
    Satisfaction_Score: int
    Last_Purchase_Days_Ago: int
    Promotion_Response: str