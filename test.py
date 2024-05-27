# import json
# from eval_retriever.metrics import Metric
# from eval_retriever.utils import load_json
# import warnings

# warnings.filterwarnings(action="ignore")
# # pred
# pred_tables = load_json("eval_retriever/preds/pred_tables.json")
# pred_columns = load_json("eval_retriever/preds/pred_columns.json")
# # label
# label_tables = load_json("eval_retriever/data/y_tables.json")
# label_columns = load_json("eval_retriever/data/y_columns.json")
# #################
# # averaged
# print(Metric.averaged(pred_tables, label_tables))
# print(Metric.averaged(pred_columns, label_columns))
# # jaccard
# print(Metric.jaccard(pred_tables, label_tables))
# print(Metric.jaccard(pred_columns, label_columns))
# # hamming
# print(Metric.hamming(pred_tables, label_tables))
# print(Metric.hamming(pred_columns, label_columns))


from eval_retriever.utils import load_llm
from eval_retriever.extract import extract_from_sql
from eval_retriever.extract import extract_from_python
from eval_retriever.chain_extract_sql import ExtractSqlChain
from eval_retriever.chain_extract_python import ExtractPythonChain


llm = load_llm(infer_url="http://localhost:8081", model="hf")
sql_chain = ExtractSqlChain.from_llm(llm=llm)
python_chain = ExtractPythonChain.from_llm(llm=llm)


code = """
SELECT c.customer_name, o.order_date, c.country
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_date IN (
    SELECT MAX(order_date)
    FROM orders
    WHERE customer_id = o.customer_id
    GROUP BY customer_id
    ORDER BY MAX(order_date) DESC
    LIMIT 5
)
ORDER BY o.order_date DESC;
"""
resp = extract_from_sql(code, sql_chain)
print(resp)
# {
#     "tables": ["orders", " customers"],
#     "columns": [
#         "c.customer_name",
#         "o.order_date",
#         "c.country",
#         "o.customer_id",
#         "c.customer_id",
#         "c.country",
#     ],
# }

code = """
import pandas as pd

# 读取CSV文件
orders_df = pd.read_csv('orders.csv')
customers_df = pd.read_csv('customers.csv')

# 将两个DataFrame通过customer_id连接
merged_df = pd.merge(orders_df, customers_df, on='customer_id')

# 对每个国家的订单按日期降序排序，并分组提取最新的5个订单
latest_orders = merged_df.sort_values(['country', 'order_date'], ascending=[True, False])
top_orders = latest_orders.groupby('country').head(5)

# 打印结果
print(top_orders[['customer_name', 'order_date', 'country']])
"""
resp = extract_from_python(code, python_chain)
print(resp)

# {
#     "tables": ["orders.csv", " customers.csv"],
#     "columns": ["customer_name", " order_date", " country"],
# }
