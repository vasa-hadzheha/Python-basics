#!/bin/bash
# Run every script in the course, feeding stdin where a script asks for input.
#
# Usage, from the repository root:
#     bash tools/run-all-scripts.sh
#
# Exits 0 if every script succeeds, 1 otherwise. Use it after editing any
# lesson example or solution - a course whose examples do not run is worse
# than no course.
cd "$(dirname "$0")/.." || exit 1
rm -rf out
pass=0; fail=0; failed=""
run(){
  printf '%s' "$2" | timeout 60 python3 "$1" >/tmp/runout 2>&1
  if [ $? -ne 0 ]; then
    echo "FAIL  $1"; sed -n '$p' /tmp/runout | sed 's/^/        /'
    fail=$((fail+1)); failed="$failed $1"
  else
    pass=$((pass+1))
  fi
}
NUM3="3
4
5
"
# ---- examples ----
run examples/meeting-1/01_types.py ""
run examples/meeting-1/01_float_precision.py ""
run examples/meeting-1/02_formatting.py ""
run examples/meeting-1/01_triangle_area.py ""
run examples/meeting-1/02_piecewise.py "2
5
"
run examples/meeting-1/03_triangle_validated.py "$NUM3"
run examples/meeting-1/03_right_triangle.py ""
run examples/meeting-1/04_count_zeros.py "1020
"
# 04_infinite_loops.py runs forever by design - interrupt it and
# check it still reports the fix.
printf '' | timeout -s INT 3 python3 examples/meeting-1/04_infinite_loops.py 1 > /tmp/runout 2>&1
if grep -q "THE FIX" /tmp/runout; then pass=$((pass+1)); echo "ok   examples/meeting-1/04_infinite_loops.py (interrupted, showed the fix)";
else fail=$((fail+1)); echo "FAIL examples/meeting-1/04_infinite_loops.py"; fi
run examples/meeting-1/04_series_precision.py "0.5
0.000001
"
run examples/meeting-1/04_validated_input.py "abc
-5
3.5
"
run examples/meeting-1/05_sum_of_logs.py "2
3
"
run examples/meeting-1/05_recurrence.py "6
"
run examples/meeting-2/06_geometric_mean.py "3
2
4
8
"
run examples/meeting-2/06_generate_and_filter.py "5
"
run examples/meeting-2/07_print_table.py ""
run examples/meeting-2/07_selective_sum.py ""
run examples/meeting-2/07_columns_without_zero.py ""
run examples/meeting-2/08_piecewise_function.py "1
1
"
run examples/meeting-2/08_recurrence_function.py ""
run examples/meeting-2/08_validation_functions.py ""
run examples/meeting-2/09_warehouse.py ""
run examples/meeting-3/10_largest_negative.py ""
run examples/meeting-3/10_replace_zeros.py ""
run examples/meeting-3/10_search_catalogue.py ""
run examples/meeting-3/11_load_products.py ""
run examples/meeting-3/11_excel_demo.py ""
run examples/meeting-3/12_csv_to_sqlite.py ""
run examples/meeting-3/13_etl_pipeline.py ""
run examples/appendix-classes/vector.py ""
# ---- meeting 1 solutions ----
B=exercise-bank/meeting-1
run $B/ex_1_02_rectangle_report.py "3.5
2
"
run $B/ex_1_03_triangle_area.py "$NUM3"
run $B/ex_1_04_interval_membership.py "1.5
3
1
2
"
run $B/ex_1_05_right_triangle.py "0
0
4
0
0
3
"
run $B/ex_1_06_piecewise.py "2
5
"
run $B/ex_1_07_largest_of_three.py "1
5
3
"
run $B/ex_1_08_sum_even.py ""
run $B/ex_1_09_sum_until_20.py "abc
10
15
"
run $B/ex_1_10_three_even.py "1
2
x
4
6
"
run $B/ex_1_11_count_zeros.py "-500
"
run $B/ex_1_12_sum_of_logs.py "2
3
"
run $B/ex_1_13_series_precision.py "0.5
0.000001
"
run $B/ex_1_14_recurrence.py "6
"
run $B/ex_1_15_invoice_line.py "12345
4006381333931
abc
0
12
13,50
25
19
"
# ---- meeting 2 solutions ----
B=exercise-bank/meeting-2
run $B/ex_2_02_geometric_mean.py "3
2
4
8
"
run $B/ex_2_03_generate_and_filter.py "5
"
run $B/ex_2_04_vector_scalar.py "2
3
4
2
"
run $B/ex_2_05_sort_descending.py "3
5
1
3
"
run $B/ex_2_06_selective_sum.py "4
5
"
run $B/ex_2_07_replace_zeros.py "2
2
1
0
0
4
"
run $B/ex_2_08_matrix_vector.py "2
2
1
1
1
2
3
4
3
7
"
run $B/ex_2_09_sort_odd_rows.py "4
"
run $B/ex_2_10_columns_without_zero.py "4
6
"
run $B/ex_2_11_rows_by_even_sum.py "4
5
"
run $B/ex_2_12_left_integral.py ""
run $B/ex_2_13_cooks_directory.py ""
run $B/ex_2_14_column_stats.py ""
run $B/ex_2_15_find_duplicates.py ""
run $B/ex_2_16_reconcile_prices.py ""
# ---- meeting 3 solutions (order matters: 3.08/3.09 need the pipeline db) ----
B=exercise-bank/meeting-3
run $B/ex_3_01_largest_negative.py ""
run $B/ex_3_02_replace_zeros.py ""
run $B/ex_3_03_search_catalogue.py "1975
"
run $B/ex_3_04_pair_points.py ""
run $B/ex_3_05_sales_summary.py ""
run $B/ex_3_06_validate_products.py ""
run $B/ex_3_07_csv_to_sqlite.py ""
run $B/ex_3_08_five_questions.py ""
run $B/ex_3_09_monthly_report.py ""
run $B/ex_3_10_incremental_load.py ""
run $B/ex_3_11_code_review.py ""
run $B/ex_3_12_ai_review.py ""
# ---- appendix solutions ----
B=exercise-bank/appendix-classes
run $B/ex_a_01_vector.py "2
3
4
"
run $B/ex_a_02_phone_tariff.py ""
run $B/ex_a_03_rectangle.py ""
run $B/ex_a_04_rectangle_indexing.py ""
run $B/ex_a_05_angle.py ""
run $B/ex_a_06_matrix.py ""
run $B/ex_a_07_box_inheritance.py ""
run $B/ex_a_08_circle_cone.py ""
run $B/ex_a_09_prism.py ""
echo ""
echo "================================================"
echo "  passed: $pass    failed: $fail"
echo "================================================"
[ $fail -gt 0 ] && { echo "failed:$failed"; exit 1; }
exit 0
