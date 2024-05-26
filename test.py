import json
from sql_metadata import Parser

# 示例 SQL 查询
sql = """
SELECT a.name, a.age, b.salary
FROM employees a
JOIN salary b ON a.id = b.emp_id
WHERE a.age > 30
"""
parser = Parser(sql)
print(parser.tables)
print(parser.columns)
