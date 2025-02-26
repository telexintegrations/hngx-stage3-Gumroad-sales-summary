import os
from dotenv import load_dotenv

load_dotenv()

def integrationJSON():
    GUMROAD_API_KEY = os.getenv("GUMROAD_API_KEY", "").strip()

    integration_JSON = {
        "data": {
            "date": {
                "created_at": "2025-02-22",
                "updated_at": "2025-02-22"
            },
            "descriptions": {
                "app_name": "Gumroad Revenue Tracker",
                "app_description": "Tracks revenue and sales data from Gumroad accounts in real time.",
                "app_logo": "https://res.cloudinary.com/ddcq3n8nr/image/upload/v1740245016/Telex_Gumroad_byuxfv.jpg",
                "app_url": "https://hngx-stage3-gumroad-sales-summary.onrender.com/",
                "background_color": "#fff"
            },
            "is_active": True,
            "integration_type": "interval",
            "integration_category": "Finance & Payments",
            "key_features": [
                "Fetch real-time revenue data from Gumroad",
                "Track sales count and revenue trends",
                "Automate financial monitoring for your Gumroad account"
            ],
            "author": "Ikwuegbu Onyeka",
            "settings": [
                {
                    "label": "gumroad_api_key",
                    "type": "text",
                    "required": True,
                    "default": f"{GUMROAD_API_KEY}"
                },
                {
                    "label": "interval",
                    "type": "text",
                    "required": True,
                    "default": "* * * * *"
                }
            ],
            "target_url": "",
            "tick_url": "https://hngx-stage3-gumroad-sales-summary.onrender.com/tick"
        }
    }

    return integration_JSON
