#GitHub: elpapitaslays

import time
import threading
import os
import platform
from core.config import DEFAULT_DELAY_MS

class TrafficController:
    def __init__(self):
        self.active = False
        self.delay_ms = DEFAULT_DELAY_MS
        self._thread = None

    def set_delay(self, ms):
        self.delay_ms = ms

    def toggle(self):
        self.active = not self.active
        if self.active:
            self._thread = threading.Thread(target=self._run, daemon=True)
            self._thread.start()

    def _run(self):
        print("[LagSwitch] Activado")
        while self.active:
            self._block_traffic()
            time.sleep(self.delay_ms / 1000.0)
            self._restore_traffic()
            time.sleep(0.05)

        print("[LagSwitch] Desactivado")

    def _block_traffic(self):
        if platform.system() == "Windows":
            os.system("netsh interface set interface name=\"Wi-Fi\" admin=disable")
        else:
            os.system("sudo ifconfig wlan0 down")

    def _restore_traffic(self):
        if platform.system() == "Windows":
            os.system("netsh interface set interface name=\"Wi-Fi\" admin=enable")
        else:
            os.system("sudo ifconfig wlan0 up")