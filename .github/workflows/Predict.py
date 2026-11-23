# predict.py
import joblid
import pandas as pd
from sklearn.datasets import load_breast_cancer
# STEP 1: Load the saved model
def load_model(model_path="best_model.joblib"):
  model = joblid.load(model_path)
  return model
  #STEP 2: Create a reusable predict(input_data)
  def make_prediction(model. input_data):
    prediction = model.predict(input_data)
    probabilities = model.predict_proba(input_data)
    result = "Malignant" if prediction[0] == 0 else "Benign"
    return {
    "prediction": result,
    "probabilities": {
    "malignant": probabilities[0][0],
    "benign": probabilities[0][0]
    }
    }
    #STEP 3: Run a sample prediction when executed directly
    if __name__ =="__main__":
      model = load_model()
      data = load_breasst__concer()
      feature_names = data.feature_names
      sample_input = dict(zip(feature_names, data.data[0])
      # Modify a few values for demonstration
      sample__input["mean radius"] = 15.0
      sample__input["mean texture"] = 18.0
      sample__input["mean perimeter"] = 100.0
      input_df = pd.DataFrame(
      [sample_input].
      columns=feature_names
      )
      output = make_prediction(model, input_df)
      print("Model loaded successfully!")
      print("\nPrediction Probabilities:")
      print("Malignant:", output["probababilities"]["malignant"])
      print("Benign:", output["probabilities"]["benign"])
