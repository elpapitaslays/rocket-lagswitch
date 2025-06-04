#GitHub: elpapitaslays

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QSlider, QHBoxLayout, QLineEdit,
    QSystemTrayIcon, QMenu, QAction, QApplication, QGraphicsDropShadowEffect
)
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, QPoint, QSize
from PyQt5.QtGui import QColor, QIcon, QPainter, QLinearGradient, QFont
import keyboard
import random
import os
from core.traffic_controller import TrafficController
from utils.network_stats import NetworkStats
from utils.process_utils import is_rocket_league_running


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rocket League LagSwitch")
        self.setFixedSize(600, 550)

        self.controller = TrafficController()
        self.net_stats = NetworkStats()
        self.current_key = "f8"
        self.compact_mode = False

        self.build_ui()
        self.apply_styles()
        self.animate_entry()
        self.setup_tray()
        self.setup_timers()
        self.setup_keybinding()

    def build_ui(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(15)
        self.layout.setContentsMargins(30, 30, 30, 30)

        self.title = QLabel("🛠️ Rocket League LagSwitch")
        self.title.setStyleSheet("color: #00ffff; font-size: 22px; font-weight: bold;")
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)

        self.status_label = QLabel("Rocket League: Checking...")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.status_label)

        self.led = QLabel("●", alignment=Qt.AlignCenter)
        self.led.setStyleSheet("font-size: 32px; color: #999;")
        self.layout.addWidget(self.led)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(100)
        self.slider.setMaximum(3000)
        self.slider.setValue(1000)
        self.layout.addWidget(self.slider)

        self.toggle_btn = QPushButton("ACTIVATE LAG")
        self.toggle_btn.setMinimumHeight(45)
        self.toggle_btn.clicked.connect(self.toggle_lag)
        self.layout.addWidget(self.toggle_btn)

        key_layout = QHBoxLayout()
        key_layout.addWidget(QLabel("Key:"))
        self.key_input = QLineEdit(self.current_key.upper())
        self.key_input.setFixedWidth(100)
        self.key_input.returnPressed.connect(self.set_keybind)
        key_layout.addWidget(self.key_input)
        self.layout.addLayout(key_layout)

        self.stats_label = QLabel("Network Stats:\nLoading...")
        self.layout.addWidget(self.stats_label)

        self.compact_btn = QPushButton("🗜️ Compact Mode")
        self.compact_btn.clicked.connect(self.toggle_compact)
        self.layout.addWidget(self.compact_btn)

        self.setLayout(self.layout)

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #111;
                color: #ccc;
                font-family: Consolas;
            }
            QSlider::groove:horizontal {
                height: 8px;
                background: #444;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #00ffff;
                width: 18px;
                margin: -6px 0;
                border-radius: 9px;
            }
            QPushButton {
                background-color: #333;
                color: #fff;
                border: 1px solid #555;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #00ccff;
                color: black;
            }
            QLineEdit {
                background: #222;
                color: #fff;
                border: 1px solid #555;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 255, 255, 100))
        shadow.setOffset(0, 0)
        self.toggle_btn.setGraphicsEffect(shadow)

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor("#1c1c1c"))
        gradient.setColorAt(1, QColor("#0d0d0d"))
        painter.fillRect(self.rect(), gradient)

    def animate_entry(self):
        self.anim = QPropertyAnimation(self, b"windowOpacity")
        self.anim.setDuration(800)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        self.anim.start()

    def setup_keybinding(self):
        keyboard.add_hotkey(self.current_key, self.toggle_lag)

    def set_keybind(self):
        key = self.key_input.text().lower().strip()
        if key:
            keyboard.unhook_all_hotkeys()
            self.current_key = key
            self.setup_keybinding()

    def toggle_lag(self):
        delay = self.slider.value()
        self.controller.set_delay(delay)
        self.controller.toggle()
        self.update_button()

    def update_button(self):
        if self.controller.active:
            self.toggle_btn.setText("DEACTIVATE LAG")
            self.toggle_btn.setStyleSheet("background-color: #00ff88; color: black;")
        else:
            self.toggle_btn.setText("ACTIVATE LAG")
            self.toggle_btn.setStyleSheet("background-color: #333; color: white;")

    def update_status(self):
        if is_rocket_league_running():
            self.status_label.setText("Rocket League: Running ✅")
            self.led.setStyleSheet("color: #00ff99; font-size: 34px;")
        else:
            self.status_label.setText("Rocket League: Not running ❌")
            self.led.setStyleSheet("color: #ff5555; font-size: 34px;")

    def update_stats(self):
        stats = self.net_stats.get_stats()
        self.stats_label.setText(
            f"Network Stats:\n↑ {stats['upload_kbps']} KB/s\n↓ {stats['download_kbps']} KB/s\n"
            f"↑ Total: {stats['total_sent_mb']} MB\n↓ Total: {stats['total_recv_mb']} MB"
        )

    def setup_timers(self):
        self.status_timer = QTimer()
        self.status_timer.timeout.connect(self.update_status)
        self.status_timer.start(1500)

        self.stats_timer = QTimer()
        self.stats_timer.timeout.connect(self.update_stats)
        self.stats_timer.start(1000)

    def toggle_compact(self):
        if not self.compact_mode:
            self.resize(600, 250)
            self.compact_btn.setText("🧰 Full Mode")
        else:
            self.resize(600, 550)
            self.compact_btn.setText("🗜️ Compact Mode")
        self.compact_mode = not self.compact_mode

    def setup_tray(self):
        self.tray = QSystemTrayIcon(QIcon(os.path.join(os.path.dirname(__file__), "icon.png")), self)
        menu = QMenu()
        show_action = QAction("Show")
        quit_action = QAction("Exit")
        show_action.triggered.connect(self.show)
        quit_action.triggered.connect(QApplication.instance().quit)
        menu.addAction(show_action)
        menu.addAction(quit_action)
        self.tray.setContextMenu(menu)
        self.tray.setToolTip("LagSwitch running")
        self.tray.show()