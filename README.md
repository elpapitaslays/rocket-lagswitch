# 🚀 Rocket League LagSwitch - Python Edition

A **professional-grade, customizable LagSwitch tool** designed specifically for Rocket League.  
Built with Python and PyQt5, this tool simulates network lag to help **Psyonix test anti-lag measures** and ensure fair play for all.

<p align="center">
  <img src="assets/screenshot.png" alt="GUI Screenshot" width="450" />
</p>

---

## 🔧 Features

- 🎮 **Designed for Rocket League**  
- 💻 **Real-time network traffic manipulation**  
- 🖥️ **Modern animated GUI with neon-inspired design**  
- 🧠 **Network usage stats (live upload/download)**  
- 🎛️ **Custom lag duration slider (100ms – 3000ms)**  
- ⌨️ **Configurable hotkey (default: F8)**  
- 🗜️ **Compact Mode toggle**  
- 📊 **Dark mode with smooth gradients and shadows**  
- 🧲 **System tray minimization support**  
- ✅ **Tested on Windows 10 & 11**

---

## 📁 Project Structure
```bash
RocketLeagueLagSwitch/
├── core/
│ └── traffic_controller.py # Controls network delay logic
├── gui/
│ └── main_window.py # Full GUI and interaction logic
├── utils/
│ ├── network_stats.py # Real-time network monitoring
│ └── process_utils.py # Rocket League process detection
├── assets/
│ └── icon.png # App icon for system tray
├── main.py # Entry point of the application
└── README.md
```


---

## 📷 Screenshots

| Full Mode | Compact Mode |
|-----------|--------------|
| ![Full Mode](assets/full.png) | ![Compact Mode](assets/compact.png) |

---

## 🚀 Getting Started

### 🔗 Requirements

Install Python 3.10+ and then install dependencies:

```bash
pip install pyqt5 psutil keyboard
▶️ Running

python main.py
⚠️ Admin privileges may be required to simulate network lag properly.

⚙️ Customization
Hotkey: Enter a new key (e.g., F9, Ctrl+Shift+L) in the text input

Delay: Drag the slider to choose delay in milliseconds

Compact Mode: Click “🗜️ Compact Mode” to toggle a smaller layout

System Tray: Minimize the app and restore via tray icon

🧪 Use Case
This LagSwitch was developed for internal testing purposes only to help game developers detect and prevent unfair network manipulation tactics in Rocket League.
Do not use this in online matches or for malicious purposes.

🔐 Legal Disclaimer
This software is intended strictly for educational and testing purposes.
We do not condone the use of lag-switching in competitive environments.
Use responsibly and only with explicit authorization from the relevant game or network owner.

💡 Credits
Created by elpapitaslays with ❤️

📦 Packaging (optional)
To convert to .exe (Windows):

pip install pyinstaller
pyinstaller --noconfirm --windowed --icon=assets/icon.ico main.py
Feel free to open issues or PRs for feedback and improvements!
Contact: [your.email@example.com]
