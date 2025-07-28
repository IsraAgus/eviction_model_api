# Eviction Model API

A lightweight Flask web app to predict eviction risk based on engineered census data features using a trained RandomForestRegressor model.

## 📁 Project Structure

```
eviction_model_api/
├── app/
│   ├── __init__.py         # Flask app factory
│   └── routes.py           # Routes and prediction logic
├── brains/
│   └── random_forest_model.pkl  # Your trained model (place here)
├── static/                 # Static assets (optional)
├── templates/
│   └── index.html          # Frontend form for input
├── run.py                  # Entrypoint to run Flask app
├── pyproject.toml          # Project dependencies (Poetry)
└── README.md               # This file
```

## 🚀 Getting Started

### 1. Install dependencies

We recommend using [UV](https://docs.astral.sh/uv/guides/projects/):

```bash
uv init
uv run
uv run run.py
```

Or install manually:

```bash
pip install flask numpy scikit-learn pandas matplotlib seaborn
```

### 2. Add your model

Place your trained model file as:

```
Brains/random_forest_model.pkl
```

### 3. Run the app

```bash
python run.py
```

Then visit: [http://localhost:5000](http://localhost:5000)

## 🧠 Model Input

The form currently expects **4 numeric features** (you can customize this in `routes.py` and `index.html`).

## 📦 Dependencies

- Flask
- NumPy
- scikit-learn
- Pandas
- Matplotlib
- Seaborn

## 📝 Author

Created by **Israel Vargas / ITESM - MNA**  
Date: 2025-07-28