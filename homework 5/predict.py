import pickle

with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

client = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

prob = pipeline.predict_proba([client])[0][1]
print(f' Prob: {round(prob,3)}')
