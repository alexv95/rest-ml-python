
flight_responses = {
 404: {
        "description": "Error",
        "content": {
            "application/json": {
                "examples": {
                    "default": {
                        "summary": "Not found",
                        "value": {"code": 404, "message": "Not found error",}
                    },
                    
                }
            }
        }
    },
     500: {
        "description": "InternalServerError",
        "content": {
            "application/json": {
                "examples": {
                    "default": {
                        "summary": "Server error",
                        "value": {"code": 500, "message": "Could not process your request, please retry later",}
                    },
                    
                }
            }
        }
    },
}