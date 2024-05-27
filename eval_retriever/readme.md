# Evaluation of Tabele Retriever

1. datasets

   - SPIDER(dev)
   - BIRD(dev)

   数据合计 2311条，可通过入参 `num` 控制测试的样本集大小。

2. files

   ```bash
   # code_gen_eval/eval_retriever/data
   ├── querys.json # 问题集
   ├── tables.json # 表格信息
   ├── y_columns.json # 字段召回标签
   └── y_tables.json # 表格召回标签
   ```

3. eval

   - 提供 `模型url`

     ```bash
     # python
     python eval_llm.py \
         --gen_model_url "http://localhost:8081" \
         --extract_model_url "http://localhost:8082" \
         --num 100
     # or bash
     bash run_llm.sh
     ```

   - 提供 `预测结果`

        ```bash
     # python
     python eval.py \
     	--pred_tables eval_retriever/preds/pred_tables.json \
     	--label_tables eval_retriever/data/y_tables.json \
     	--pred_columns eval_retriever/preds/pred_columns.json \
     	--label_columns eval_retriever/data/y_columns.json
     # or bash
     bash run.sh
        ```

4. response example

   ```json
   {
       "table": {
           "micro-Averaged Precision": 0.22109067017082787,
           "micro-Averaged Recall": 0.6735051288466349,
           "micro-Averaged F1": 0.33290051320101405,
           "macro-Averaged Precision": 0.13976550733152518,
           "macro-Averaged Recall": 0.3881846449171073,
           "macro-Averaged F1": 0.1857803816650417,
           "samples-Averaged Precision": 0.2676472224827915,
           "samples-Averaged Recall": 0.6640806906925472,
           "samples-Averaged F1": 0.35717170717066893,
           "weighted-Averaged Precision": 0.3637433649379988,
           "weighted-Averaged Recall": 0.6735051288466349,
           "weighted-Averaged F1": 0.4459455511007109,
           "Jaccard Similarity": 0.25583090223397414,
           "Hamming Loss": 0.020386645226267385
       },
       "column": {
           "micro-Averaged Precision": 0.024689698436169735,
           "micro-Averaged Recall": 0.19107617616460526,
           "micro-Averaged F1": 0.043729001878257186,
           "macro-Averaged Precision": 0.014774926641471512,
           "macro-Averaged Recall": 0.07186279322877256,
           "macro-Averaged F1": 0.020838020850031357,
           "samples-Averaged Precision": 0.03255324831448256,
           "samples-Averaged Recall": 0.1643324198278763,
           "samples-Averaged F1": 0.04558131269968282,
           "weighted-Averaged Precision": 0.098891750157333,
           "weighted-Averaged Recall": 0.19107617616460526,
           "weighted-Averaged F1": 0.11313546677422914,
           "Jaccard Similarity": 0.02539466616130353,
           "Hamming Loss": 0.015312494903495233
       }
   }
   ```

   