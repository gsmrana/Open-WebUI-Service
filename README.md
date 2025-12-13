# Open WebUI Service
Deploy Open WebUI as a web service to use it using any web browser.

## Environment Setup

Install Python and UV Package Manager

https://docs.astral.sh/uv/getting-started/installation

```
winget install --id Python.Python.3.12
winget install --id=astral-sh.uv  -e
```

Install packages in a virtual environment

```
uv sync
cp .env.sample .env
```

Upgrade all packages

```
uv lock --upgrade
uv sync
```

## Install and run systemd service.

```
sudo cp open_webui.service /etc/systemd/system/open_webui.service
sudo systemctl daemon-reload
sudo systemctl enable open_webui.service
sudo systemctl restart open_webui.service
```

- Browse url: http://localhost:8080
