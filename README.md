# MLOps Flask Azure Assignment

This project implements a complete assignment example using Flask, scikit-learn, GitHub Actions, Azure App Service, and Azure Pipelines.

## Local setup

```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/macOS: source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python train_model.py
pytest -v
python app.py
```

The API exposes `GET /`, `GET /health`, and `POST /predict`.

Example prediction body:

```json
{"features": [5.1, 3.5, 1.4, 0.2]}
```

## Azure configuration before deployment

In `azure-pipelines.yml`, replace `YOUR-ARM-SERVICE-CONNECTION` and `YOUR-AZURE-APP-NAME` with the real Azure values. In `make_predict_azure_app.sh`, either replace `YOUR-APP-NAME` or set the `APP_URL` environment variable.

## Evidence

Place the required screenshots in the `screenshots` folder. See `SUBMISSION_CHECKLIST.md`.
