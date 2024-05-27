import json
from eval_retriever.metrics import Metric
from eval_retriever.utils import load_json
import argparse
import warnings

warnings.filterwarnings(action="ignore")


def evaluate_metrics(
    pred_tables_path, label_tables_path, pred_columns_path, label_columns_path
):
    # Load data
    pred_tables = load_json(pred_tables_path)
    pred_columns = load_json(pred_columns_path)
    label_tables = load_json(label_tables_path)
    label_columns = load_json(label_columns_path)

    # Calculate metrics
    results = {
        "averaged_tables": Metric.averaged(pred_tables, label_tables),
        "averaged_columns": Metric.averaged(pred_columns, label_columns),
        "jaccard_tables": Metric.jaccard(pred_tables, label_tables),
        "jaccard_columns": Metric.jaccard(pred_columns, label_columns),
        "hamming_tables": Metric.hamming(pred_tables, label_tables),
        "hamming_columns": Metric.hamming(pred_columns, label_columns),
    }

    return results


def main():
    parser = argparse.ArgumentParser(description="Evaluate retrieval metrics.")
    parser.add_argument(
        "--pred_tables", required=True, help="Path to predicted tables JSON file."
    )
    parser.add_argument(
        "--label_tables", required=True, help="Path to label tables JSON file."
    )
    parser.add_argument(
        "--pred_columns", required=True, help="Path to predicted columns JSON file."
    )
    parser.add_argument(
        "--label_columns", required=True, help="Path to label columns JSON file."
    )

    args = parser.parse_args()

    results = evaluate_metrics(
        args.pred_tables, args.label_tables, args.pred_columns, args.label_columns
    )
    print(json.dumps(results, indent=4))


if __name__ == "__main__":
    main()
