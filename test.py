from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

sql_query = """
    CREATE TABLE IF NOT EXISTS example_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        value INTEGER
    );
    """

data, error = supabase.rpc('sql', {'query': sql_query}).execute()

if error:
    print(f"Error creating table: {error}")
else:
    print("Table created successfully")