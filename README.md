# 🚀 Phishing URL Detector

Detect phishing URLs using a machine learning model trained on 10,000+ URLs from **Tranco** and **PhishTank** datasets. Includes both CLI and web app (Streamlit) interfaces.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3.0-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-FF4B4B)
[![Live Demo](https://img.shields.io/badge/Live_Demo-PhishGuard_AI-00f)](https://phishing-detector-l9ycye9whhqh4gjybgmqhn.streamlit.app/)

---

## 🔍 Features
- Extracts 15+ lexical, host-based, and path-based URL features
- Real-time phishing detection via CLI or Streamlit UI
- Trained Logistic Regression model with **95% accuracy**

---

## 🛠️ Setup
```bash
git clone https://github.com/meghanacycarat/phishing-detector.git
cd phishing-detector
pip install -r requirements.txt
````

---

## 🖥️ Usage

### Web App

👉 [Try it Live](https://phishing-detector-l9ycye9whhqh4gjybgmqhn.streamlit.app/)
OR
```bash
streamlit run streamlit_app.py
```

## 📁 Project Structure

```
phishing-detector/
├── streamlit_app.py       # Web UI
├── phishing_model.pkl     # Trained model
├── code.ipynb             # Notebook: training + EDA
└── requirements.txt       # Python dependencies
```

---

## 📜 License

MIT © [Meghana M J](https://github.com/meghanacycarat)


