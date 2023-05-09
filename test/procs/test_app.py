
import pytest
from snowflake.snowpark.session import Session
from snowflake.snowpark.types import StringType
from src.util.local import get_env_var_config
from src.procs.app import run


@pytest.fixture
def local_session():
    return Session.builder.configs(get_env_var_config()).create()


# @pytest.mark.snowflake_vcr
# def test_app_sproc(local_session):
#     expected_df = local_session.create_dataframe(["Welcome to Snowflake!", "Learn more: https://www.snowflake.com/snowpark/"]).toDF("Hello world")
#     actual_df = run(local_session)
#     assert expected_df.collect() == actual_df.collect()
