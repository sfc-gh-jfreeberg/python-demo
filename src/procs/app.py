"""
An example stored procedure. __main__ provides an entrypoint for local development
and testing.
"""

from snowflake.snowpark.session import Session
from snowflake.snowpark.dataframe import col, DataFrame
from snowflake.snowpark.types import StringType, StructType, StructField
from snowflake.snowpark.functions import concat

def run(snowpark_session: Session) -> int:
    """
    A sample stored procedure which creates a small DataFrame, prints it to the
    console, and returns the number of rows in the table.
    """

    schema = StructType([StructField("col_1", StringType()), StructField("col_2", StringType())])

    data = [
        ("Welcome to ", "Snowflake!"),
        ("Learn more: ", "https://www.snowflake.com/snowpark/"),
    ]

    df: DataFrame = snowpark_session.create_dataframe(data, schema)

    df2 = df.select(concat(df["col_1"],df["col_2"]).as_("Hello world")).sort(
        "Hello world", ascending=False
    )

    df2.show()
    return df2.count()


if __name__ == "__main__":
    # This entrypoint is used for local development.

    import sys

    sys.path.insert(0, "..")  # Necessary to import from udf and util directories

    from src.util.local import get_env_var_config

    print("Creating session...")
    session = Session.builder.configs(get_env_var_config()).create()

    print("Running stored proc...")
    run(session)
