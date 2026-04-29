# uac-care-load-forecast
Data-driven predictive analytics dashboard forecasting UAC care load and placement demand. Uses SARIMA time-series models to enable proactive resource planning and early-warning alerts for HHS decision-makers.

## Dashboard link
http://localhost:8502/

## Research Paper Link
https://zenodo.org/records/19567055

### Video link
https://drive.google.com/file/d/14_Dht8-nIiDDTyLs5J_dbnqEzryFT9Bn/view?usp=drive_link

# 📊 Predictive Forecasting of Care Load & Placement Demand



---

## 🎯 Overview

A **data-driven predictive analytics dashboard** for forecasting Unaccompanied Alien Children (UAC) care load and placement demand. This application uses advanced time-series forecasting models to enable HHS decision-makers to **anticipate future care demands, allocate resources proactively, and strengthen child-welfare outcomes**.

**From reactive decisions to forward-looking intelligence.** 🔮

---

## 🚀 Quick Access

**📊 [Care Load Forecast Dashboard - Live Demo](http://localhost:8502/)**

*Replace the link above with your deployed Streamlit Cloud URL*

---

## 🔴 The Problem

The UAC Program operates in a **high-uncertainty environment** where sudden policy changes, border activity fluctuations, and humanitarian crises can rapidly increase the number of children entering federal care.

**Current Challenge:**
- ❌ High-quality daily data exists, but lacks predictive power
- ❌ Decision-makers operate reactively, not proactively
- ❌ Overcrowding risks and staff burnout increase due to poor planning
- ❌ No early-warning system for capacity stress

**This project changes that.**

---

## 💡 Key Objectives

✅ **Forecast** the number of children in HHS care for the next 12 months  
✅ **Estimate** future discharge (placement) demand  
✅ **Predict** short-term capacity stress indicators  
✅ **Provide** early-warning alerts for healthcare planners  
✅ **Quantify** forecast uncertainty with confidence intervals  

---

## 🚀 Core Features

### 📈 Advanced Forecasting
- **SARIMA Models** with seasonal decomposition
- **12-month forward prediction** with confidence intervals
- **Multi-horizon evaluation** (short & medium-term accuracy)
- **Scenario simulation** for growth planning

### 📊 Interactive Dashboard
- Real-time KPI tracking (Care Load, Placement Rate, Utilization)
- Dynamic filtering by date range, year, and month
- Comprehensive visualizations with Plotly
- Alert system for capacity breaches and placement delays

### 🧠 Predictive Intelligence
- Daily change tracking and trend analysis
- Placement rate efficiency monitoring
- System utilization forecasting
- Data-driven risk assessment

### 📥 Data Management
- Automated data cleaning and preprocessing
- 7-day rolling averages for trend smoothing
- Feature engineering (lag features, rolling statistics)
- Download filtered datasets for further analysis

---

## 📋 Dataset

**Source:** HHS Unaccompanied Alien Children Program  
**Granularity:** Daily observations  
**Key Metrics:**
| Field | Description |
|-------|-------------|
| **Date** | Reporting date |
| **Apprehended** | Daily intake volume |
| **CBP_Custody** | Active CBP care load |
| **Transferred** | Flow into HHS system |
| **HHS_Care** | Active HHS care load (target variable) |
| **Discharged** | Successful sponsor placements |

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Streamlit |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly Express, Plotly Graph Objects |
| **Time-Series Forecasting** | StatsModels (SARIMAX) |
| **Model Evaluation** | Scikit-learn Metrics |
| **Language** | Python 3.8+ |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip or conda package manager

### Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/care-load-forecast.git
cd care-load-forecast

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Verify installation
python -c "import streamlit; print('✅ Streamlit installed')"
```

### Requirements.txt
```
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.24.0
plotly>=5.17.0
scikit-learn>=1.3.0
statsmodels>=0.14.0
```

---

## 🎮 Quick Start

### Run the Dashboard
```bash
streamlit run app.py
```

The dashboard will open at `http://localhost:8501` in your default browser.

### First Steps
1. **Explore KPIs** - Check the 5 key metrics at the top
2. **Apply Filters** - Use the sidebar to select date ranges and years
3. **Review Charts** - Analyze care load trends and patterns
4. **Check Alerts** - Look for risk indicators (red/yellow alerts)
5. **View Forecast** - Scroll to the 12-month prediction with confidence intervals
6. **Run Scenarios** - Adjust the growth slider to simulate different outcomes
7. **Download Data** - Export filtered data for external analysis

---

## 📊 Key Performance Indicators (KPIs)

| KPI | Definition | Business Impact |
|-----|-----------|-----------------|
| **Care Load** | Current children in HHS care | Operational capacity planning |
| **Avg Load** | Historical daily average | Baseline for comparison |
| **Placement Rate** | % of children successfully discharged | System efficiency metric |
| **Delay** | Avg days before placement | Care quality indicator |
| **Utilization** | % of max capacity in use | Risk alert trigger |

---

## 🔮 Forecasting Models

### SARIMA (Seasonal ARIMA)
```
Configuration: (1,1,1) × (1,1,1,12)
- Order: (p=1, d=1, q=1)
- Seasonal Order: (P=1, D=1, Q=1, s=12)
- Captures both trend and 12-month seasonality
```

### Model Evaluation Metrics
- **MAE** - Mean Absolute Error (forecast accuracy)
- **RMSE** - Root Mean Squared Error (penalizes large deviations)
- **MAPE** - Mean Absolute Percentage Error (relative accuracy)

### Feature Engineering
- 7-day and 14-day rolling averages
- Daily change indicators
- Placement rate calculations
- Lag features (t-1, t-7, t-14)

---

## 📈 Dashboard Sections

### 1. **KPI Summary**
Real-time metrics showing:
- Current care load with daily change
- Average load baseline
- Placement efficiency rate
- Average delay in days
- System utilization percentage

### 2. **Care Load Trends**
- Actual vs. 7-day rolling average
- Helps identify underlying trends vs. daily noise

### 3. **Intake & Discharge Flow**
- Apprehended vs. Discharged volumes
- Critical for capacity planning

### 4. **Custody Transfer Analysis**
- CBP custody vs. HHS care load relationship
- Shows conversion pipeline

### 5. **Monthly Aggregation**
- Smoothed monthly views for long-term patterns
- Easier to spot seasonal cycles

### 6. **Distribution Analysis**
- Histogram of care load values
- Identifies typical ranges and outliers

### 7. **Daily Change Volatility**
- Day-to-day changes in care load
- Flags sudden surges

### 8. **Placement Rate Tracking**
- Efficiency of the discharge process
- Alert threshold: < 50%

### 9. **Capacity Utilization**
- % of maximum capacity in use
- Alert threshold: > 85%

### 10. **12-Month Forecast**
- SARIMA predictions with confidence intervals
- Scenario simulation with growth sliders

---

## ⚠️ Alert System

The dashboard automatically triggers alerts for critical conditions:

| Alert Type | Condition | Action |
|-----------|-----------|--------|
| 🚨 **High Utilization** | > 85% capacity | Activate surge protocols |
| ⚠️ **Low Placement** | < 50% rate | Investigate discharge bottlenecks |
| ⚠️ **Sudden Surge** | > 1,000 daily change | Mobilize additional resources |

---

## 🧠 Scenario Analysis

The dashboard includes an interactive **growth simulator**:
- Adjust expected growth percentage (0-50%)
- See projected impact on care loads
- Plan resource allocation proactively
- Compare baseline vs. stressed scenarios

---

## 📂 Project Structure

```
care-load-forecast/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── HHS_Unaccompanied_Alien_        # Dataset (CSV)
│   Children_Program.csv
├── README.md                       # This file
├── LICENSE                         # MIT License
└── docs/
    ├── METHODOLOGY.md              # Technical approach
    ├── MODEL_EVALUATION.md         # Performance metrics
    └── DEPLOYMENT.md               # Production guidelines
```

---

## 🔍 Model Performance

### Train-Test Split Strategy
- **Training Set:** All data except last 12 months
- **Test Set:** Last 12 months of historical data
- **Validation:** Walk-forward evaluation

### Evaluation Results
```
Mean Absolute Error (MAE): [Model Performance]
Root Mean Squared Error (RMSE): [Model Performance]
Mean Absolute Percentage Error (MAPE): [Model Performance]
```

---

## 🚀 Deployment

### Local Deployment
```bash
streamlit run app.py
```

### Cloud Deployment (Streamlit Cloud)
1. Push repository to GitHub
2. Go to https://share.streamlit.io
3. Connect your GitHub repo
4. Select `app.py` as the main file
5. Deploy in seconds

### Docker Deployment
```bash
docker build -t care-load-forecast .
docker run -p 8501:8501 care-load-forecast
```

---

## 📚 Data Dictionary

### Computed Features

| Feature | Calculation | Purpose |
|---------|-----------|---------|
| **HHS_Rolling** | 7-day rolling mean of HHS_Care | Trend smoothing |
| **Daily_Change** | Day-to-day difference in HHS_Care | Volatility tracking |
| **Placement_Rate** | Discharged / HHS_Care | Efficiency metric |
| **Estimated_Delay** | HHS_Care / (Discharged + 1) | Avg days in care |
| **Utilization** | HHS_Care / Max_Capacity | Capacity pressure |

---

## 🎓 Methodology Highlights

### Time-Series Preparation
✓ Convert Date to datetime index  
✓ Ensure daily observation continuity  
✓ Handle missing data via forward fill  
✓ Decompose into trend, seasonality, residuals  

### Feature Engineering
✓ Lag features (t-1, t-7, t-14)  
✓ Rolling statistics (mean & variance)  
✓ Flow-based signals (net pressure)  
✓ Calendar effects (day of week, month)  

### Model Selection
✓ Baseline models (Naïve, Moving Average)  
✓ Statistical models (ARIMA/SARIMA)  
✓ ML models (Random Forest, Gradient Boosting)  
✓ Ensemble comparisons  

---

## 🤝 Contributing

We welcome contributions! Here's how:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/improvement`)
3. **Commit** changes (`git commit -m 'Add improvement'`)
4. **Push** to branch (`git push origin feature/improvement`)
5. **Open** a Pull Request

### Areas for Contribution
- [ ] Additional forecasting models (Prophet, LSTM)
- [ ] Enhanced visualizations
- [ ] Performance optimization
- [ ] Data quality improvements
- [ ] Documentation expansion

---

## 📖 Documentation

For detailed technical documentation, see:
- **[METHODOLOGY.md](docs/METHODOLOGY.md)** - Statistical approach & model details
- **[MODEL_EVALUATION.md](docs/MODEL_EVALUATION.md)** - Performance metrics & benchmarks
- **[DEPLOYMENT.md](docs/DEPLOYMENT.md)** - Production deployment guide

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🤖 About

**Project:** Predictive Forecasting of Care Load & Placement Demand  
**Organization:** U.S. Department of Health and Human Services (HHS)  
**Program:** Unaccompanied Alien Children (UAC) Program  
**Sponsor:** Unified Mentor  

---

## 📞 Author and Contact

<p align="center">
  <b>Ram Prakash Patel</b><br>
  <i>Data Analyst </i>
</p>

<p align="center">
  <a href="mailto:ram8756patel@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
  <a href="https://github.com/Ramprakas87">
    <img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white" />
  </a>
  <a href="https://www.linkedin.com/in/ram-prakash-patel-62863b378/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
</p>

---

### 💬 Get in Touch
If you have any questions, feedback, or collaboration ideas, feel free to connect.  
I’m always open to discussing **data science, forecasting models, and real-world problem solving**.

---

### ⭐ Support
If you found this project helpful, consider giving it a ⭐!
---

