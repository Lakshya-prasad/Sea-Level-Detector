# 🌊 Sea Level Rise Predictor

## 📌 Overview
This project analyzes the **EPA's Global Average Absolute Sea Level Change** dataset (1880–2014) to visualize historical trends and forecast ocean rise through **2050**.  
Two linear regression models are built — one on the full dataset and one on post-2000 data — to compare historical and accelerating modern rates of sea level rise.

---

## 📂 Project Structure
```
sea-level-predictor/
│
├── data/
│   └── epa-sea-level.csv
│
├── output/
│   └── sea_level_plot.png
│
├── sea_level_predictor.py
├── main.py
├── test_module.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Technologies Used
- Python
- Pandas
- Matplotlib
- SciPy

---

## 🚀 How to Run

### 1. Clone the Repository
```
git clone https://github.com/your-username/sea-level-predictor.git
cd sea-level-predictor
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Run the Project
```
python main.py
```

---

## 📊 Output

The script generates a scatter plot with two regression lines saved as `sea level detector.png`:

| Element | Description |
|---|---|
| 🔵 Blue dots | Observed sea level data (1880–2014) |
| 🔴 Red line | Linear regression over full dataset — predicts **~10.1 inches** rise by 2050 |
| 🟢 Green line | Regression from 2000 onwards — predicts **~15.3 inches** rise by 2050 |

> The steeper green line highlights the **accelerating rate** of sea level rise since 2000 compared to the historical average.

 Example
 
![Sea Level Plot](output/sea%20level%20detector.png)

---

## 🧠 Key Features
- CSV data loading and processing with Pandas
- Scatter plot visualization of sea level change since 1880
- Full-range linear regression (1880 → 2050) using SciPy `linregress`
- Recent-trend regression (2000 → 2050) to model accelerated rise
- Exported chart as PNG using Matplotlib

---

## ⚠️ Dataset Info
- **Source:** US Environmental Protection Agency (CSIRO, 2015 / NOAA, 2015)
- **Years Covered:** 1880–2014
- **Key Column:** `CSIRO Adjusted Sea Level` (inches)
- **Target Year:** 2050 (predicted)

---

## 📈 Future Improvements
- Add polynomial regression for non-linear trend modeling
- Incorporate confidence intervals around predictions
- Support multiple sea level datasets (NOAA, satellite data)
- Build an interactive dashboard using Plotly or Streamlit
- Deploy as a web app with real-time data updates

---

## 🔗 Project Resources
### Dataset (data/epa-sea-level.csv) — [Click to Download](https://datahub.io/core/sea-level-rise)

This project is part of the **freeCodeCamp Data Analysis with Python** certification.  
[View Certification](https://www.freecodecamp.org/certification/your-username/data-analysis-with-python-v7)

---

## 👨‍💻 Author
**Lakshya Prasad**  
B.Tech CSE (AI)  
Data Analytics | Machine Learning
