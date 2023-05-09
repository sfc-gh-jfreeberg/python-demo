"""
This module contains the UDFs for the project.
"""

from snowflake.snowpark.functions import udf

@udf(is_permanent=False)
def identity(string_a: str) -> str:
    """
    A sample UDF implementation
    """
    return string_a
