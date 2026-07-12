# 🏛️ FMCG Corporate Working Capital Optimizer

## 💼 Business Problem
FMCG companies operate on narrow margins. Delayed retail payments lock up cash flow liquidity. This project builds a financial pipeline that tracks **Days Sales Outstanding (DSO)** using SQL and deploys a predictive model to flag **Delinquent Payments** before invoicing occurs.

## 🛠️ Tech Stack
* **Database & Transformation**: SQL (DuckDB Engine)
* **Language & Analysis**: Python (Pandas)
* **Machine Learning**: Scikit-Learn (Random Forest Engine)

## 🗄️ SQL Engineering Feature Snippet
```sql
SELECT 
    distributor_name,
    AVG(days_taken_to_pay) as days_sales_outstanding_DSO,
    AVG(days_taken_to_pay) - AVG(allowed_terms) as average_days_past_due
FROM fmcg_invoice_table
GROUP BY distributor_name;
```

## 📊 Business Outcomes
* Developed an early-warning engine with **85%+ predictive accuracy**.
* Identified distribution channels locking up working capital, optimizing internal cash allocations.

