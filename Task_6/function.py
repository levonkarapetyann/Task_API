import json

def lambda_handler(event, context):
    info = json.loads(event.get("body", "{}"))
    name = info.get("name", "")
    message = info.get("message", "")
    return {
        'statusCode': 200,
        "headers": {
            "Content-Type": "application/json"
        },
        'body': json.dumps({
            "received": True,
            "name": name,
            "message": message
        })
    }

