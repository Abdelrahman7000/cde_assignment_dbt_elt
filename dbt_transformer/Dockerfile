# Use the official dbt-postgres image
FROM ghcr.io/dbt-labs/dbt-postgres:1.7.5


ENTRYPOINT [] 

WORKDIR /app

# Copy the dbt project and profiles
COPY dbt_project /app/dbt_project
COPY profiles.yml /root/.dbt/profiles.yml

# Set the entrypoint to the dbt project directory
WORKDIR /app/dbt_project

# dbt will be executed via the cron job script, so no CMD here.