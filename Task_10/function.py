import json, boto3

s3 = boto3.client('s3')
bucket_name = "tumo-task"

def lambda_handler(event, context):
    info = event.get("pathParameters") or {}
    filename = info.get("filename", "")

    s3_path = f"messages/{filename}"

    try:
        response = s3.get_object(
            Bucket = bucket_name,
            Key = s3_path
        )

        read = response["Body"].read().decode("utf-8")

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": read
        }
    except Exception as e:
            return {
                "statusCode": 404,
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": json.dumps({
                    "error": "file not found"
                })
            }

