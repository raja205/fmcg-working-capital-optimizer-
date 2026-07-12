import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_fmcg_data(records=5000):
    np.random.seed(42)
    distributors = ['Walmart_Dist', 'Tesco_Wholesale', 'Carrefour_Retail', 'Target_Supply', 'Costco_Bulk']
    skus = ['SKU_Soap_Pack', 'SKU_SoftDrink_Case', 'SKU_Snack_Box', 'SKU_Detergent_Jug']
    
    start_date = datetime(2025, 1, 1)
    
    data = []
    for i in range(records):
        distributor = np.random.choice(distributors)
        sku = np.random.choice(skus)
        invoice_amount = round(float(np.random.exponential(scale=15000) + 500), 2)
        
        # Payment terms (standard FMCG options: 30, 45, or 60 days)
        allowed_terms = np.random.choice([30, 45, 60], p=[0.5, 0.3, 0.2])
        
        # Chronological dates
        invoice_days_offset = np.random.randint(0, 365)
        inv_date = start_date + timedelta(days=invoice_days_offset)
        due_date = inv_date + timedelta(days=int(allowed_terms))
        
        # Simulate payment behavior (some pay early, many pay late)
        days_to_pay = int(np.random.normal(loc=allowed_terms + 5, scale=10))
        days_to_pay = max(5, days_to_pay) # cannot pay in less than 5 days
        
        payment_date = inv_date + timedelta(days=days_to_pay)
        actual_days_taken = (payment_date - inv_date).days
        
        # Target label for ML: 1 if payment missed due date by > 7 days (Delinquent)
        is_delinquent = 1 if actual_days_taken > (allowed_terms + 7) else 0
        
        data.append([
            f"INV-{10000+i}", distributor, sku, inv_date.strftime('%Y-%m-%d'), 
            due_date.strftime('%Y-%m-%d'), payment_date.strftime('%Y-%m-%d'),
            allowed_terms, invoice_amount, actual_days_taken, is_delinquent
        ])
        
    df = pd.DataFrame(data, columns=[
        'invoice_id', 'distributor_name', 'sku_category', 'invoice_date', 
        'due_date', 'payment_date', 'allowed_terms', 'invoice_amount', 
        'days_taken_to_pay', 'is_delinquent'
    ])
    
    # Save to CSV
    df.to_csv('fmcg_invoice_data.csv', index=False)
    print("✅ Mock dataset generated successfully: 'fmcg_invoice_data.csv'")

generate_fmcg_data()

