import os

TORTOISE_ORM = {
    "connections": {"default": "mysql://root:password@localhost:3306/gatewayti"},
    "apps": {
        "models": {
            "models": [
                "database.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}