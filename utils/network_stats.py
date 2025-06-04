#GitHub: elpapitaslays

import psutil
import time

class NetworkStats:
    def __init__(self):
        self.last_bytes_sent = 0
        self.last_bytes_recv = 0
        self.last_time = time.time()

    def get_stats(self):
        now = time.time()
        counters = psutil.net_io_counters()
        interval = now - self.last_time if self.last_time else 1

        sent_speed = (counters.bytes_sent - self.last_bytes_sent) / interval
        recv_speed = (counters.bytes_recv - self.last_bytes_recv) / interval

        self.last_bytes_sent = counters.bytes_sent
        self.last_bytes_recv = counters.bytes_recv
        self.last_time = now

        return {
            "upload_kbps": round(sent_speed / 1024, 2),
            "download_kbps": round(recv_speed / 1024, 2),
            "total_sent_mb": round(counters.bytes_sent / (1024 * 1024), 2),
            "total_recv_mb": round(counters.bytes_recv / (1024 * 1024), 2)
        }