"""Run the flask server"""
import os
from SteamScout import app

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

    # site url: https://002-pyp-demoday-g1-chanchar.c9.io

    # server error: Port being used ... yada yada
    # terminal: "lsof -i :8080" looks for a process that using port 8080.
    # "kill {process number}", it's usually the first one listing using the
    # second number in the listing.
    # Rerun the serve to see if it works.
