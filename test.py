import json
from eval_retriever.metrics import Metric
from eval_retriever.utils import load_json
import warnings

warnings.filterwarnings(action="ignore")
# pred
pred_tables = load_json("eval_retriever/preds/pred_tables.json")
pred_columns = load_json("eval_retriever/preds/pred_columns.json")
# label
label_tables = load_json("eval_retriever/data/y_tables.json")
label_columns = load_json("eval_retriever/data/y_columns.json")
#################
# averaged
print(Metric.averaged(pred_tables, label_tables))
print(Metric.averaged(pred_columns, label_columns))
# jaccard
print(Metric.jaccard(pred_tables, label_tables))
print(Metric.jaccard(pred_columns, label_columns))
# hamming
print(Metric.hamming(pred_tables, label_tables))
print(Metric.hamming(pred_columns, label_columns))
