"""Small reusable data-preprocessing utilities for the portfolio project.

These helpers are a portfolio refactoring, separate from the original coursework notebook.
"""
from __future__ import annotations

from collections.abc import Iterable
import pandas as pd


def audit_dataframe(df: pd.DataFrame) -> dict:
    """Return a compact data-quality audit for a DataFrame."""
    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_cells": int(df.isna().sum().sum()),
        "columns_with_missing": int((df.isna().sum() > 0).sum()),
        "dtypes": {str(k): str(v) for k, v in df.dtypes.items()},
    }


def standardise_airline_names(
    df: pd.DataFrame,
    column: str = "airline",
    replacements: dict[str, str] | None = None,
) -> pd.DataFrame:
    """Return a copy with known airline-name inconsistencies corrected."""
    if column not in df.columns:
        raise KeyError(f"Required column {column!r} not found")
    result = df.copy()
    mapping = replacements or {"Japanese Airlines": "Japan Airlines"}
    result[column] = result[column].replace(mapping)
    return result


def aggregate_fuel_surcharges(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate surcharge observations to one record per month and airline."""
    required = {"month", "airline", "fuel_surcharge_usd", "surcharge_as_pct_base"}
    missing = required.difference(df.columns)
    if missing:
        raise KeyError(f"Missing required columns: {sorted(missing)}")
    return (
        df.groupby(["month", "airline"], as_index=False)
        .agg(
            avg_fuel_surcharge_usd=("fuel_surcharge_usd", "mean"),
            avg_surcharge_as_pct_base=("surcharge_as_pct_base", "mean"),
        )
    )


def aggregate_route_costs(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate route-level records to airline-month level."""
    required = {
        "month", "airline", "extra_fuel_cost_usd",
        "rerouted", "flight_cancelled", "fuel_pct_of_cost"
    }
    missing = required.difference(df.columns)
    if missing:
        raise KeyError(f"Missing required columns: {sorted(missing)}")
    return (
        df.groupby(["month", "airline"], as_index=False)
        .agg(
            total_extra_fuel_cost_usd=("extra_fuel_cost_usd", "sum"),
            total_rerouted_flights=("rerouted", lambda s: int((s == "Yes").sum())),
            total_cancelled_flights=("flight_cancelled", lambda s: int((s == "Yes").sum())),
            avg_fuel_pct_of_cost=("fuel_pct_of_cost", "mean"),
        )
    )


def assert_unique_keys(df: pd.DataFrame, keys: Iterable[str]) -> None:
    """Raise ValueError if the given join keys do not uniquely identify rows."""
    keys = list(keys)
    missing = set(keys).difference(df.columns)
    if missing:
        raise KeyError(f"Missing key columns: {sorted(missing)}")
    duplicates = int(df.duplicated(subset=keys).sum())
    if duplicates:
        raise ValueError(f"Expected unique keys {keys}; found {duplicates} duplicate rows")
