"""
SQL Queries Module
Store all production-level SQL queries here after validating them in Notebook 1
"""

# TODO: 学生在此处填入 Notebook 1 中验证过的 RFM 计算 SQL
# 该查询应使用 CTE 和 NTILE 窗口函数，计算每个用户的 R(Recency), F(Frequency), M(Monetary)
RFM_CALCULATION_QUERY = """
WITH user_purchase_stats AS (
    SELECT 
        customer_id,
        MAX(order_date) as last_purchase_date,
        COUNT(DISTINCT order_id) as purchase_count,
        SUM(total_amount) as total_monetary
    FROM orders
    GROUP BY customer_id
),
rfm_scores AS (
    SELECT 
        customer_id,
        last_purchase_date,
        purchase_count,
        total_monetary,
        -- TODO: 使用 NTILE 或类似窗口函数划分 R, F, M 的等级（1-5分）
        -- NTILE(5) OVER (ORDER BY last_purchase_date) as recency_score,
        -- NTILE(5) OVER (ORDER BY purchase_count DESC) as frequency_score,
        -- NTILE(5) OVER (ORDER BY total_monetary DESC) as monetary_score
    FROM user_purchase_stats
)
SELECT * FROM rfm_scores;
"""

# TODO: 学生在此处填入留存率计算 SQL
# 该查询应使用窗口函数 LEAD() 或 LAG() 计算次月留存率
RETENTION_RATE_QUERY = """
WITH monthly_cohort AS (
    SELECT 
        customer_id,
        DATE_TRUNC('month', order_date) as cohort_month,
        -- TODO: 编写窗口函数逻辑
    FROM orders
)
SELECT * FROM monthly_cohort;
"""

# 用户漏斗分析 SQL
FUNNEL_ANALYSIS_QUERY = """
-- TODO: 计算各转化环节的用户数和转化率
-- 例如: 访问 -> 加入购物车 -> 支付成功
SELECT 
    step,
    COUNT(DISTINCT customer_id) as unique_users,
    -- TODO: 添加转化率字段
FROM user_events
GROUP BY step
"""
