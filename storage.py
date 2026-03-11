import json
import os
from dataclasses import asdict
from datetime import datetime
from devlog.models import LogEntry
FILE = 'devlog_entries.json'


def save_entry(entry: LogEntry):
    entries = load_entries()
    data = asdict(entry)
    data['timestamp'] = entry.timestamp.isoformat()
    entries.append(data)
    with open(FILE, 'w') as f:
        json.dump(entries, f)

def load_entries():
    if not os.path.exists(FILE):
        return []
    with open(FILE, 'r') as f:
        data = json.load(f)
    for d in data:
        d['timestamp'] = datetime.fromisoformat(d['timestamp'])
    return [LogEntry(**d) for d in data]