#!/usr/bin/env bash
set -euo pipefail
APP_URL="${APP_URL:-https://YOUR-APP-NAME.azurewebsites.net}"
echo "Sending prediction request to ${APP_URL}/predict"
curl --fail-with-body -X POST "${APP_URL}/predict" -H "Content-Type: application/json" -d '{"features":[5.1,3.5,1.4,0.2]}'
echo
