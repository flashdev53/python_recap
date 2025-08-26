try:
    with open("config.json", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("Config file missing, falling back to defaults...")
finally:
    print("Cleanup if needed")