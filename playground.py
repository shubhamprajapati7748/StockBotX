import os
import phi
from dotenv import load_dotenv
from phi.playground import Playground, serve_playground_app
from agents import web_search_agent, finance_agent

# Load environment variables
load_dotenv()

phi.api = os.getenv("PHI_API_KEY")

# Playground app
app = Playground(agents = [finance_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)