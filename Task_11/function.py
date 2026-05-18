import json, boto3

s3 = boto3.client('s3')
bucket_name = "tumo-task"

def lambda_handler(event, context):
    info = event.get("pathParameters") or {}
    filename = info.get("filename", "")

    s3_path = f"messages/{filename}"

    
    try:
        file_delete = s3.delete_object(
            Bucket = bucket_name,
            Key = s3_path
        )

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "File deleted successfully"
            })
        }
        
    except Exception as e:
        return {
            "statusCode": 404,
            "headers": {
                "ContenType": "application/json"
            },
            "body": json.dumps({
                "error": "File not found"
            })
        }


