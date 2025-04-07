
# SynthexAI Take Home Assignment

This project is a simple FastAPI backend that wraps around a pre-trained Linear Regression model. The API accepts a numeric input and returns a numeric prediction. It is deployed on Heroku and can be accessed publicly.

---

## Setup Instructions (Run Locally)

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. **Create and activate Virtual Environment**
```bash
python3 -m venv synthexAI
source synthexAI/bin/activate 
```
3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
4. **(Optional) Train and save the model locally**
```bash
python take_home_model.py
```
5. **Run the app locally**
```bash
uvicorn app:app --host=0.0.0.0 --port=8000
```
6. **Testing the service**
GET Request
```bash
curl "https://synthexai-takehome-6439c31477e9.herokuapp.com/predict?x=4.2"
```
POST Request
```bash
curl -X POST "https://synthexai-takehome-6439c31477e9.herokuapp.com/predict" \\
  -H "Content-Type: application/json" \\
  -d '{"x": 4.2}'
```
You can use both a public or local URL.

## Possible Improvements

Addition of a basic front-end that allows the user to enter to test the model without a get or post request.
