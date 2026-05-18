import json

def lambda_handler(event, context):
    info = event.get("queryStringParameters") or {}
    name = info.get("name", "")
    return {
        'statusCode': 200,
        "headers": {
            "ContentType": "applicatuon/json"
        },
        'body': json.dumps(f"Hello {name}")
    }

