import duckdb

# Connect to DuckDB and load our fresh CSV
con = duckdb.connect()
df = pd.read_csv('fmcg_invoice_data.csv')

sql_query = """
SELECT 
    distributor_name,
    COUNT(invoice_id) as total_invoices,
    SUM(invoice_amount) as total_revenue,
    AVG(allowed_terms) as avg_allowed_terms,
    AVG(days_taken_to_pay) as days_sales_outstanding_DSO,
    AVG(days_taken_to_pay) - AVG(allowed_terms) as average_days_past_due,
    SUM(CASE WHEN is_delinquent = 1 THEN invoice_amount ELSE 0 END) / SUM(invoice_amount) as cash_at_risk_ratio
FROM df
GROUP BY distributor_name
ORDER BY cash_at_risk_ratio DESC;
"""

sql_features = con.execute(sql_query).fetchdf()
print(sql_features)

