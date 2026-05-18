import json

def lambda_handler(event, context):
    info = event.get("pathParameters") or {}
    name = info.get("username", "")
    return {
        'statusCode': 200,
        "headers": {
            "Content-Type": "application/json"
        },
        'body': json.dumps({
            "username": name,
            "profile": f"This is {name}'s profile"
        })
    }

