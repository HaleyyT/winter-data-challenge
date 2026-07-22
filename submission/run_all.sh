#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPOSITORY_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
EXECUTED_NOTEBOOK_DIR="${TMPDIR:-/tmp}/winter-data-challenge-executed"

cd "$REPOSITORY_ROOT"
mkdir -p "$EXECUTED_NOTEBOOK_DIR"

echo "Running OECD data audit module..."
python -m submission.code.oecd_audit

notebooks=(
  "submission/code/data_audit.ipynb"
  "submission/code/method1_eda.ipynb"
  "submission/code/method02_primary_same_endpoint.ipynb"
  "submission/code/method03_comparator_bootstrap_placebo.ipynb"
  "submission/code/method4_theilsen_kendall.ipynb"
  "submission/code/method5_spearman_association.ipynb"
  "submission/code/final_visuals.ipynb"
)

for notebook in "${notebooks[@]}"; do
  echo "Executing $notebook..."
  jupyter nbconvert \
    --to notebook \
    --execute "$notebook" \
    --output-dir "$EXECUTED_NOTEBOOK_DIR" \
    --ExecutePreprocessor.timeout=600
done

echo "Running submission tests..."
python -m pytest submission/tests -q

echo "Rendering report..."
quarto render submission/report/australia_material_social_report.qmd

echo "Submission completed successfully."
echo "Rendered report: $SCRIPT_DIR/report/australia_material_social_report.html"
echo "Executed notebook copies: $EXECUTED_NOTEBOOK_DIR"
