from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.environ.get("TOKEN")
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
