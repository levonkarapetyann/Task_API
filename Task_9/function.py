import json, boto3

s3 = boto3.client("s3")
bucket_name = "tumo-task"

def lambda_handler(event, context):
    info = json.loads(event.get("body", "{}"))
    filename = info.get("filename", "")
    message = info.get("message", "")

    s3_path = f"messages/{filename}"

    s3.put_object(
        Bucket = bucket_name,
        Key = s3_path,
        Body = json.dumps(info),
        ContentType = "application/json"
    )
    return {
        'statusCode': 200,
        "headers": {
            "Content-Type": "application/json"
        },
        'body': json.dumps({
            "success": True,
            "message": message,
            "path": s3_path
        })
    }

