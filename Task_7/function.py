import json

def lambda_handler(event, context):
    info = json.loads(event.get("body", "{}"))
    name = info.get("name", "")
    age = info.get("age", "")
    course = info.get("course", "")
    return {
        'statusCode': 200,
        "headers": {
            "Content-Type": "application/json"
        },
        'body': json.dumps({
            "success": True,
            "message": f"Student {name} registered for {course}"
        })
    }

