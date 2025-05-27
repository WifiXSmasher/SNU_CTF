from supabase import create_client
from decouple import config
import os 


SUPABASE_URL = config("SUPABASE_URL")
SUPABASE_KEY = config("SUPABASE_SERVICE_KEY")  # Use service role key for uploads

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

