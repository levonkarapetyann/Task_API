import json

def lambda_handler(event, context):
    info = event.get("queryStringParameters") or {}
    str_a = info.get("a", "0")
    str_b = info.get("b", "0")
    operation = info.get("operation", "add")

    try:
        a = float(str_a)
        b = float(str_b)
    except ValueError:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid input. Please provide valid numbers.')
        }

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return {
                'statusCode': 400,
                'body': json.dumps('Division by zero is not allowed.')
            }
        result = a / b
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid operation. Please use add, subtract, multiply, or divide.')
        }

    return {
        'statusCode': 200,
        "headers": {
            "Content-Type": "application/json"
        },
        'body': json.dumps({
            "a": a,
            "b": b,
            "operatoin": operation,
            "result": int(result)
        })
    }

