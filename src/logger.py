import json
import os
from datetime import datetime

LOG_FILE_PATH = "logs/capture_log.json"

def save_log_entry(src, dst, version, size):
    """
    Appends a structured TLS ClientHello event entry into our JSON log file.
    """
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source": src,
        "destination": dst,
        "tls_version": version,
        "payload_size_bytes": size
    }
    
    # Ensure logs directory exists
    os.makedirs("logs", exist_ok=True)
    
    # Load existing logs or initialize new list
    logs = []
    if os.path.exists(LOG_FILE_PATH):
        try:
            with open(LOG_FILE_PATH, "r") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []
            
    logs.append(entry)
    
    # Write back formatted JSON
    with open(LOG_FILE_PATH, "w") as f:
        json.dump(logs, f, indent=4)