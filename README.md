<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Rocket League LagSwitch - README</title>
<style>
  body {
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    background: #121212;
    color: #ddd;
    margin: 0;
    padding: 2rem;
    line-height: 1.6;
  }
  h1, h2, h3 {
    color: #00ffff;
  }
  a {
    color: #00aaff;
    text-decoration: none;
  }
  a:hover {
    text-decoration: underline;
  }
  code {
    background: #222;
    color: #0ff;
    padding: 0.2em 0.4em;
    border-radius: 4px;
    font-family: Consolas, monospace;
  }
  pre {
    background: #222;
    color: #0ff;
    padding: 1em;
    border-radius: 6px;
    overflow-x: auto;
  }
  table {
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 2rem;
  }
  th, td {
    border: 1px solid #333;
    padding: 0.5rem;
    text-align: center;
  }
  th {
    background: #0a0a0a;
  }
  .container {
    max-width: 900px;
    margin: auto;
  }
  .screenshot {
    width: 100%;
    max-width: 450px;
    border-radius: 8px;
    box-shadow: 0 0 15px #00ffff77;
  }
  .button {
    display: inline-block;
    padding: 0.6em 1.2em;
    margin-top: 0.5rem;
    background: #00ccff;
    color: #000;
    font-weight: bold;
    border-radius: 6px;
    text-decoration: none;
  }
  .button:hover {
    background: #00aacc;
    color: #fff;
  }
</style>
</head>
<body>
  <div class="container">
    <h1>🚀 Rocket League LagSwitch - Python Edition</h1>
    <p>
      A <strong>professional-grade, customizable LagSwitch tool</strong> designed specifically for Rocket League.<br />
      Built with Python and PyQt5, this tool simulates network lag to help <strong>Psyonix test anti-lag measures</strong> and ensure fair play for all.
    </p>

    <img src="assets/screenshot.png" alt="GUI Screenshot" class="screenshot" />

    <h2>🔧 Features</h2>
    <ul>
      <li>🎮 <strong>Designed for Rocket League</strong></li>
      <li>💻 <strong>Real-time network traffic manipulation</strong></li>
      <li>🖥️ <strong>Modern animated GUI with neon-inspired design</strong></li>
      <li>🧠 <strong>Network usage stats (live upload/download)</strong></li>
      <li>🎛️ <strong>Custom lag duration slider (100ms – 3000ms)</strong></li>
      <li>⌨️ <strong>Configurable hotkey (default: F8)</strong></li>
      <li>🗜️ <strong>Compact Mode toggle</strong></li>
      <li>📊 <strong>Dark mode with smooth gradients and shadows</strong></li>
      <li>🧲 <strong>System tray minimization support</strong></li>
      <li>✅ <strong>Tested on Windows 10 &amp; 11</strong></li>
    </ul>

    <h2>📁 Project Structure</h2>
    <pre><code>RocketLeagueLagSwitch/
├── core/
│   └── traffic_controller.py       # Controls network delay logic
├── gui/
│   └── main_window.py              # Full GUI and interaction logic
├── utils/
│   ├── network_stats.py            # Real-time network monitoring
│   └── process_utils.py            # Rocket League process detection
├── main.py                         # Entry point of the application
└── README.md
</code></pre>

    <h2>📷 Screenshots</h2>
    <table>
      <tr>
        <th>Full Mode</th>
        <th>Compact Mode</th>
      </tr>
      <tr>
        <td><img src="assets/full.png" alt="Full Mode" class="screenshot" /></td>
        <td><img src="assets/compact.png" alt="Compact Mode" class="screenshot" /></td>
      </tr>
    </table>

    <h2>🚀 Getting Started</h2>
    <h3>🔗 Requirements</h3>
    <pre><code>pip install pyqt5 psutil keyboard</code></pre>

    <h3>▶️ Running</h3>
    <pre><code>python main.py</code></pre>

    <p><strong>⚠️ Admin privileges may be required to simulate network lag properly.</strong></p>

    <h2>⚙️ Customization</h2>
    <ul>
      <li><strong>Hotkey</strong>: Enter a new key (e.g., <code>F9</code>, <code>Ctrl+Shift+L</code>) in the text input</li>
      <li><strong>Delay</strong>: Drag the slider to choose delay in milliseconds</li>
      <li><strong>Compact Mode</strong>: Click “🗜️ Compact Mode” to toggle a smaller layout</li>
      <li><strong>System Tray</strong>: Minimize the app and restore via tray icon</li>
    </ul>

    <h2>🧪 Use Case</h2>
    <p>
      This LagSwitch was developed for <strong>internal testing purposes only</strong> to help game developers detect and prevent unfair network manipulation tactics in Rocket League.<br />
      <strong>Do not use this in online matches or for malicious purposes.</strong>
    </p>

    <h2>🔐 Legal Disclaimer</h2>
    <p>
      This software is intended strictly for <strong>educational and testing</strong> purposes.<br />
      We do <strong>not</strong> condone the use of lag-switching in competitive environments.<br />
      Use responsibly and only with <strong>explicit authorization</strong> from the relevant game or network owner.
    </p>

    <h2>💡 Credits</h2>
    <p>Created by elpapitaslays with ❤️<br />
      Special thanks to the <a href="https://www.psyonix.com" target="_blank" rel="noopener noreferrer">Psyonix</a> team for supporting ethical game development tools.
    </p>

    <h2>📦 Packaging (optional)</h2>
    <pre><code>pip install pyinstaller
pyinstaller --noconfirm --windowed --icon=assets/icon.ico main.py
</code></pre>

    <p>Feel free to <a href="https://x.com/elpepasdev">contact me</a> for support or feedback!</p>
  </div>
</body>
</html>
