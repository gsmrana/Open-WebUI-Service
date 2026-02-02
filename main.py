import os
import sys
from dotenv import load_dotenv

# load .env in os.environ
load_dotenv()

def start_app():
    try:
        # Get configuration from environment (with defaults)
        host = os.getenv("HOST", "0.0.0.0")
        port = int(os.getenv("PORT", 8080))
        print(f"Starting Open WebUI on {host}:{port}")
        
        # Import Open WebUI after the environment is ready
        import open_webui.main
        import uvicorn

        # Launch the server
        uvicorn.run(open_webui.main.app, host=host, port=port)
        
    except ImportError as e:
        print(f"Error: Required packages not found. {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Failed to start: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_app()
