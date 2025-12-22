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

## Run the application

```
uv run open-webui serve
```
- Browse: http://localhost:8080

## Install and run systemd service (Linux)

```
sudo cp open_webui.service /etc/systemd/system/open_webui.service
sudo systemctl daemon-reload
sudo systemctl enable open_webui.service
sudo systemctl restart open_webui.service
```
