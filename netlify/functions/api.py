import sys
import os
from mangum import Mangum
from backend.app import app  # Import your main FastAPI app

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'backend'))

# Create a handler for the FastAPI app
handler = Mangum(app)