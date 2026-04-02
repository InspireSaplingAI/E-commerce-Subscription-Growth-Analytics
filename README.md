# E-commerce Growth & A/B Testing Analytics Platform

A comprehensive, enterprise-grade data analytics project for e-commerce subscription growth analysis. This repository follows the **"Notebook Exploratory → Python Module Consolidation → Web App Deployment"** workflow, exactly as practiced by data teams at top tech companies.

## 📋 Project Overview

This project demonstrates:
- **Stage 1**: Business metrics modeling using SQL and RFM segmentation
- **Stage 2**: BI dashboard development with Tableau
- **Stage 3**: A/B testing statistical analysis with Python
- **Stage 4**: Cloud integration (AWS S3) and Streamlit web app deployment
- **Stage 5**: Production-ready code documentation and packaging

## 🏗️ Project Structure

```
ecommerce-growth-analytics/
├── data/                           # Data storage
│   ├── raw/                        # Original CSV downloads
│   └── processed/                  # Cleaned, processed data
│
├── notebooks/                      # Jupyter Notebooks (Exploratory Phase)
│   ├── 01_data_cleaning_and_rfm.ipynb              # RFM modeling
│   ├── 02_bi_data_export.ipynb                     # BI data prep
│   ├── 03_ab_testing_analysis.ipynb                # Statistical testing
│   └── 04_aws_and_streamlit_test.ipynb             # Cloud & App integration
│
├── src/                            # Production code modules
│   ├── data_pipeline/              # ETL & data storage
│   │   ├── aws_client.py           # S3 upload/download
│   │   └── sql_queries.py          # SQL query templates
│   └── analysis/                   # Statistical analysis
│       ├── ab_test.py              # A/B testing module
│       └── rfm_model.py            # RFM segmentation module
│
├── dashboards/                     # Tableau dashboard files (.twb)
│
├── app/                            # Streamlit web application
│   └── main.py                     # Main Streamlit app
│
├── scripts/                        # Utility scripts
│   └── init_db.py                  # Database initialization
│
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Anaconda or venv for environment management
- VS Code + Jupyter extension (recommended)
- PostgreSQL or SQLite (local database)

### Setup

1. **Clone repository and navigate to directory**
   ```bash
   cd ecommerce-growth-analytics
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download data** (Olist E-Commerce Dataset from Kaggle)
   ```bash
   # Option 1: Using Kaggle API (if configured)
   kaggle datasets download -d olistbr/brazilian-ecommerce
   
   # Option 2: Manual download from https://www.kaggle.com/olistbr/brazilian-ecommerce
   # Extract CSV files to data/raw/
   ```

5. **Initialize local database**
   ```bash
   python scripts/init_db.py
   ```

## 📊 Development Workflow

### Stage 1: Data Exploration & RFM Modeling
- **Notebook**: `01_data_cleaning_and_rfm.ipynb`
- **Tasks**:
  - Load Olist dataset
  - Clean and validate data
  - Calculate RFM (Recency, Frequency, Monetary) scores
  - Validate SQL queries with real data
- **Output**: Tested SQL queries → save to `src/data_pipeline/sql_queries.py`

### Stage 2: BI Dashboard Development
- **Notebook**: `02_bi_data_export.ipynb`
- **Tasks**:
  - Export processed data to CSV
  - (Optional) Upload to AWS S3
  - Create visualizations in Tableau Desktop
- **Output**: Dashboard file → `dashboards/growth_dashboard.twb`
- **Code Consolidation**: AWS integration functions → `src/data_pipeline/aws_client.py`

### Stage 3: A/B Testing Analysis
- **Notebook**: `03_ab_testing_analysis.ipynb`
- **Tasks**:
  - Simulate A/B test with treatment/control groups
  - Inject test labels into user data
  - Perform statistical testing (Z-test for conversion, T-test for AOV)
  - Calculate power and sample size
- **Output**: Statistical test functions → `src/analysis/ab_test.py`

### Stage 4: Cloud Integration & Web App
- **Notebook/Script**: `04_aws_and_streamlit_test.ipynb` or direct to `app/main.py`
- **Tasks**:
  - Import modules from `src/`
  - Streamlit UI for RFM segmentation display
  - Real-time A/B test results calculation
  - (Optional) AWS S3 integration for data persistence
- **Output**: Runnable web app

### Stage 5: Testing & Documentation
- Write unit tests for key modules
- Generate API documentation
- Prepare deployment instructions

## 🔧 How to Run

### Run Notebooks
```bash
# Start Jupyter server
jupyter notebook

# Navigate to notebooks/ folder and open any notebook
```

### Run Streamlit App
```bash
streamlit run app/main.py

# App will open at http://localhost:8501
```

### Run Analysis Scripts
```bash
python scripts/init_db.py
```

## 📚 Key Concepts

### RFM Segmentation
Customers are scored on a scale of 1-5 for each dimension  (R, F, M, three dimensions) and grouped into segments:
- **Champions** (5-5-5): Best customers
- **Loyal** (High F, M): Frequent, high-value
- **At-Risk** (Low R): Haven't purchased recently
- **Lost** (1-1-1): Inactive customers

### A/B Testing
Statistical comparison of two page variants using:
- **Z-test**: For conversion rate (binary outcome)
- **T-test**: For continuous metrics (AOV, LTV)
- **Significance level**: α = 0.05
- **Power**: 0.80 (80% chance to detect true effect if it exists)

## 🔐 AWS Configuration (Optional)

If using AWS S3:

1. **Configure AWS CLI**
   ```bash
   aws configure
   ```
   Provide: Access Key ID, Secret Access Key, Region (e.g., us-east-1)

2. **Set environment variable**
   ```bash
   export AWS_S3_BUCKET_NAME=my-bucket-name
   ```

3. **AWS functions in code**
   - See `src/data_pipeline/aws_client.py` for S3 integration examples

## 📖 Data Source

**Brazilian E-Commerce Public Dataset** by Olist
- **Source**: [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce)
- **Records**: ~100K orders, ~32K customers, ~73K products
- **Time period**: 2016-2018
- **License**: CC BY-SA 2.0

## 🎓 Learning Objectives

After completing this project, you will understand:
- ✅ Data exploration and validation best practices
- ✅ SQL optimization for analytical queries
- ✅ RFM segmentation and customer lifetime value
- ✅ A/B testing design and statistical significance
- ✅ Data pipeline and ETL principles
- ✅ Cloud integration (AWS S3)
- ✅ Building interactive web dashboards with Streamlit
- ✅ Professional code structuring and packaging

## 🐛 Troubleshooting

### Issue: Import errors for `src` modules
- **Solution**: Ensure you're running from the project root directory and Python path includes the project

### Issue: Database connection errors
- **Solution**: Verify PostgreSQL/SQLite is running, update connection string in code

### Issue: Streamlit app not displaying charts
- **Solution**: Ensure all `src/` modules are implemented before running app

## 📝 TODO Checkpoints

Each `.py` file contains TODO comments marking what needs to be implemented:
- [ ] Stage 1: SQL queries in `src/data_pipeline/sql_queries.py`
- [ ] Stage 2: AWS functions in `src/data_pipeline/aws_client.py`
- [ ] Stage 3: Statistical tests in `src/analysis/ab_test.py`
- [ ] Stage 4: Streamlit UI in `app/main.py`
- [ ] Stage 5: Testing & documentation

## 📞 Support

For questions or issues:
1. Check existing GitHub issues
2. Consult Notebook comments for context
3. Review `TODO` comments in skeleton code

## 📄 License

MIT License - See LICENSE file for details

---

**Happy analyzing! 📊📈**
