from abc import ABC,abstractmethod

import pandas as pd

class DataInspectionStatergy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        pass

class DataTypeInspectionStatergy(DataInspectionStatergy):
    def inspect(self, df: pd.DataFrame):
        print("\nData Types and Non-Null Counts: ")
        print(df.info())

class SummaryStatisticsInspectionStatergy(DataInspectionStatergy):
    def inspect(self, df: pd.DataFrame):
        print("\nSummary Statistics (Numerical Features):")
        print(df.describe())
        print("\nSummary Statistics (Categorical Features):")
        print(df.describe(include=["0"]))

class DataInspector:
    def __init__(self, statergy: DataTypeInspectionStatergy):
        self._statergy = statergy

    def set_statergy(self, statergy: DataInspectionStatergy):
        self._statergy = statergy

    def execute_statergy(self, df: pd.DataFrame):
        self._statergy.inspect(df)


if __name__ == "__main__":
    pass