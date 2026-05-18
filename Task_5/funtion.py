import json, random

def lambda_handler(event, context):
    info = event.get("queryStringParameters") or {}
    str_min = info.get("min", "1")
    str_max = info.get("max", "100000")

    min = int(str_min)
    max = int(str_max)

    random_num = random.randint(min, max)
    return {
        'statusCode': 200,
        "headerts": {
            "Content-Type": "application/json"
        },
        'body': json.dumps({
            "min": min,
            "max": max,
            "random": random_num
        })
    }

