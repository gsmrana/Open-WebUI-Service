# Open WebUI Service
Deploy Open WebUI as web service to use it using any web browser.

## Install Python package manager UV
https://docs.astral.sh/uv/getting-started/installation

## Environment setup
1. Setup required packages.

```
uv sync
```

2. Install and run systemd service.

```
sudo cp open_webui.service /etc/systemd/system/open_webui.service
sudo systemctl daemon-reload
sudo systemctl enable open_webui.service
sudo systemctl restart open_webui.service
```

3. Browse url: http://localhost:8080
