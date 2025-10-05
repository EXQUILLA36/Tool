from python_aternos import Client
from python_aternos.aterrors import ServerStartError
import os
from dotenv import load_dotenv
load_dotenv()


try:
    # Create client
    print("USER:", os.getenv("DISCORD_USER"))
    print("PASS FOUND:", bool(os.getenv("DISCORD_PASS")))
    atclient = Client()

    # Log in with username + password
    atclient.login(os.getenv("DISCORD_USER"), os.getenv("DISCORD_PASS"))

    # Get account
    aternos = atclient.account

    # --- FIX DUPLICATE COOKIE ISSUE ---
    cookies = aternos.atconn.session.cookies
    if 'ATERNOS_SESSION' in cookies:
        matches = [c for c in cookies if c.name == 'ATERNOS_SESSION']
        if len(matches) > 1:
            # Keep only the last one (most valid)
            for c in matches[:-1]:
                cookies.clear(c.domain, c.path, c.name)

    # Get servers list
    servs = aternos.list_servers()

    # Use the first server
    myserv = servs[0]
    
    try:
        myserv.start()
        print("Server Starting")
    except ServerStartError as e:
        print("Server might be already running")

    # Optional: Stop server later
    # myserv.stop()
except Exception as e:
    print("There seems to be a problem starting the server")