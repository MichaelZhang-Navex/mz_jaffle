from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig

import os
from datetime import datetime

airflow_home = os.environ["AIRFLOW_HOME"]
dag_folder = os.path.join(airflow_home, "dags")
jaffle_home = os.path.join(dag_folder, "jaffle-shop")

profile_config = ProfileConfig(
    profile_name="jaffle_shop",
    target_name="qa",
    profiles_yml_filepath=os.path.join(jaffle_home, "profiles.yml"),
)

my_cosmos_dag = DbtDag(
    project_config=ProjectConfig(
        jaffle_home,
    ),
    profile_config=profile_config,
    execution_config=ExecutionConfig(
        dbt_executable_path="dbt",
    ),
    # normal dag parameters
    schedule_interval="@daily",
    start_date=datetime(2024, 12, 1),
    catchup=False,
    dag_id="jaffleshop_dag",
    default_args={"retries": 1},
)