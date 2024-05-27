#!/bin/bash

# 定义或生成你的路径，这里为了演示，直接使用硬编码的示例路径
PRED_TABLES_PATH="eval_retriever/preds/pred_tables.json"
LABEL_TABLES_PATH="eval_retriever/data/y_tables.json"
PRED_COLUMNS_PATH="eval_retriever/preds/pred_columns.json"
LABEL_COLUMNS_PATH="eval_retriever/data/y_columns.json"

# 调用main.py，并将路径作为参数传递
python eval.py \
    --pred_tables "$PRED_TABLES_PATH" \
    --label_tables "$LABEL_TABLES_PATH" \
    --pred_columns "$PRED_COLUMNS_PATH" \
    --label_columns "$LABEL_COLUMNS_PATH"