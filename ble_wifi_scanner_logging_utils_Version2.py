"""
Rotating CSV loggers for BLE/Wi-Fi events.
Handles daily log rotation and thread safety.
"""

import threading
import csv
from pathlib import Path
from typing import List, Any, Optional
from datetime import date

class CsvRotatingLogger:
    """Logger that rotates CSV files daily."""
    def __init__(self, log_dir: str, log_prefix: str, header: List[str]):
        self.log_dir = Path(log_dir)
        self.log_prefix = log_prefix
        self.header = header
        self.current_date = date.today()
        self.lock = threading.Lock()
        self.file: Optional[Any] = None
        self.writer: Optional[csv.writer] = None
        self._open_new_log()

    def _log_file_path(self) -> Path:
        filename = f"{self.log_prefix}_{self.current_date.isoformat()}.csv"
        return self.log_dir / filename

    def _open_new_log(self):
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.file = open(self._log_file_path(), mode='a', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        if self.file.tell() == 0:
            self.writer.writerow(self.header)

    def log(self, row: List[Any]):
        with self.lock:
            today = date.today()
            if today != self.current_date:
                self.file.close()
                self.current_date = today
                self._open_new_log()
            self.writer.writerow(row)
            self.file.flush()

    def close(self):
        with self.lock:
            if self.file:
                self.file.close()
                self.file = None
                self.writer = None
