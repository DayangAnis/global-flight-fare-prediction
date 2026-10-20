import unittest
import pandas as pd

from src.preprocessing.utilities import (
    audit_dataframe,
    standardise_airline_names,
    aggregate_fuel_surcharges,
    aggregate_route_costs,
    assert_unique_keys,
)


class PreprocessingUtilityTests(unittest.TestCase):
    def test_audit_dataframe_counts_missing_and_duplicates(self):
        df = pd.DataFrame({"a": [1, 1, None], "b": ["x", "x", "z"]})
        result = audit_dataframe(df)
        self.assertEqual(result["rows"], 3)
        self.assertEqual(result["columns"], 2)
        self.assertEqual(result["duplicate_rows"], 1)
        self.assertEqual(result["missing_cells"], 1)

    def test_standardise_airline_names_does_not_mutate_input(self):
        original = pd.DataFrame({"airline": ["Japanese Airlines"]})
        fixed = standardise_airline_names(original)
        self.assertEqual(fixed.loc[0, "airline"], "Japan Airlines")
        self.assertEqual(original.loc[0, "airline"], "Japanese Airlines")

    def test_aggregate_fuel_surcharges(self):
        df = pd.DataFrame({
            "month": ["2024-01", "2024-01"],
            "airline": ["A", "A"],
            "fuel_surcharge_usd": [10, 20],
            "surcharge_as_pct_base": [0.1, 0.3],
        })
        result = aggregate_fuel_surcharges(df)
        self.assertEqual(len(result), 1)
        self.assertEqual(result.loc[0, "avg_fuel_surcharge_usd"], 15)
        self.assertAlmostEqual(result.loc[0, "avg_surcharge_as_pct_base"], 0.2)

    def test_aggregate_route_costs(self):
        df = pd.DataFrame({
            "month": ["2024-01", "2024-01"],
            "airline": ["A", "A"],
            "extra_fuel_cost_usd": [5, 7],
            "rerouted": ["Yes", "No"],
            "flight_cancelled": ["No", "Yes"],
            "fuel_pct_of_cost": [0.2, 0.4],
        })
        result = aggregate_route_costs(df)
        self.assertEqual(result.loc[0, "total_extra_fuel_cost_usd"], 12)
        self.assertEqual(result.loc[0, "total_rerouted_flights"], 1)
        self.assertEqual(result.loc[0, "total_cancelled_flights"], 1)

    def test_assert_unique_keys_raises_on_duplicates(self):
        with self.assertRaises(ValueError):
            assert_unique_keys(pd.DataFrame({"k": [1, 1]}), ["k"])


if __name__ == "__main__":
    unittest.main()
