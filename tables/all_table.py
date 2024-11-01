# Import 複合主鍵的 `create_table` 函式
from indicators import (
    get_all_roe_columns, get_all_roa_columns, get_all_revenue_columns, 
    get_all_gross_margin_columns, get_all_eps_columns, 
    get_all_operating_margin_columns, get_all_pe_ratio_columns, 
    get_all_free_cash_flow_columns, create_table
)

def create_all_tables():
    # 創建包含複合主鍵 (year, quarter) 的表格
    roe_columns = get_all_roe_columns() 
    create_table("roe", roe_columns)

    roa_columns = get_all_roa_columns()  
    create_table("roa", roa_columns)
    
    # 創建每月營收表
    revenue_columns = get_all_revenue_columns()
    create_table("revenue", revenue_columns)

    # 創建毛利率表
    gross_margin_columns = get_all_gross_margin_columns()
    create_table("gross_margin", gross_margin_columns)

    # 創建 EPS 表
    eps_columns = get_all_eps_columns()
    create_table("eps", eps_columns)

    # 創建營業利益率表
    operating_margin_columns = get_all_operating_margin_columns()
    create_table("operating_margin", operating_margin_columns)

    # 創建本益比表
    pe_ratio_columns = get_all_pe_ratio_columns()
    create_table("pe_ratio", pe_ratio_columns)

    # 創建自由現金流表
    free_cash_flow_columns = get_all_free_cash_flow_columns()
    create_table("free_cash_flow", free_cash_flow_columns)

if __name__ == "__main__":
    create_all_tables()
