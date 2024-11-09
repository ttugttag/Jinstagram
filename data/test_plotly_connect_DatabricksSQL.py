from dash import Dash, dash_table
from databricks import sql
import os

# pip install databricks-sql-connector

app = Dash(__name__)
server = app.server

# Set these as environment variables in Dash Enterprise or locally
SERVER_HOSTNAME = os.getenv("SERVER_HOSTNAME")
HTTP_PATH = os.getenv("HTTP_PATH")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# Configure according to your table and database names in Databricks
DB_NAME = "plotly_iot_dashboard"
TABLE_NAME = "silver_users"

with sql.connect(
    server_hostname=SERVER_HOSTNAME, http_path=HTTP_PATH, access_token=ACCESS_TOKEN
) as connection:
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {DB_NAME}.{TABLE_NAME} LIMIT 100")
        df = cursor.fetchall_arrow()
        df = df.to_pandas()

app.layout = dash_table.DataTable(
    df.to_dict("records"), [{"name": i, "id": i} for i in df.columns]
)

if __name__ == "__main__":
    app.run(debug=True)
