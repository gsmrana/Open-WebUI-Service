# Open WebUI Service
Deploy Open WebUI as a web service to use it using any web browser.

## Environment Setup

Install Python and UV Package Manager

https://docs.astral.sh/uv/getting-started/installation

```
winget install --id Python.Python.3.11
winget install --id=astral-sh.uv  -e
```

Install packages in a virtual environment

```
uv sync
```

Upgrade all packages

```
uv lock --upgrade
uv sync
```

## Run the application (SQLite DB)

```
uv run open-webui serve
```

## Run the application (PostgreSQL)

```
cp .env.sample .env
uv run main.py
```
- Browse: http://localhost:8080

## Install and run systemd service (Linux)

Service Setup
```
sudo cp open_webui.service /etc/systemd/system/open_webui.service
sudo systemctl daemon-reload
sudo systemctl enable open_webui.service
```

Service Start/Restart
```
sudo systemctl restart open_webui.service
```

## Install and run launchd service (macOS)

Service Setup
```
sudo cp com.openwebui.service.plist /Library/LaunchDaemons/
sudo chown root:wheel /Library/LaunchDaemons/com.openwebui.service.plist
sudo chmod 644 /Library/LaunchDaemons/com.openwebui.service.plist
```

Service First Load
```
sudo launchctl load -w /Library/LaunchDaemons/com.openwebui.service.plist
```

Service Stop
```
sudo launchctl bootout system /Library/LaunchDaemons/com.openwebui.service.plist
```

Service Restart
```
sudo launchctl kickstart -k system/com.openwebui.service
```
