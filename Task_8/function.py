import json

def lambda_handler(event, context):
    info = event.get("queryStringParameters") or {}
    value_str = info.get("value", "")
    from_str = info.get("from", "")
    to_str = info.get("to", "")

    value = int(value_str)
    result = int((value * 9/5) + 32)
    return {
        'statusCode': 200,
        "headers": {
            "Content-Type": "application/json"
        },
        'body': json.dumps({
            "value": value,
            "from": from_str,
            "to": to_str,
            "result": result
        })
    }
