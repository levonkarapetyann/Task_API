import json, boto3
s3 = boto3.client("s3")
bucket_name = "tumo-task"

def lambda_handler(event, context):
    
    httpMethods = event.get("requestContext", {}).get("http", {}).get("method") 

    if httpMethods == "POST":
        info = json.loads(event.get("body", "{}"))
        student_id = info.get("studentId", "")

        s3_path = f"students/{student_id}.json"

        s3.put_object(
            Bucket = bucket_name,
            Key = s3_path,
            Body = json.dumps(info),
            ContentType = "application/json"
        )

        return {
            "statusCode": 200,
            "headers": {
                "ContentType": "application/json" 
            },
            "body": json.dumps(info)
        }

    elif httpMethods == "GET":
        info = event.get("pathParameters") or {}
        student_id = info.get("studentId", "")

        s3_path = f"students/{student_id}.json"

        try:
            response = s3.get_object(
                Bucket = bucket_name,
                Key = s3_path
            )

            read = response["Body"].read().decode("utf-8")

            return {
                "statusCode": 200,
                "headers": {
                    "ContentType": "application/json"
                },
                "body": read
            }

        except Exception as e:
            return {
                "statusCode": 404,
                "headers": {
                    "ContentType": "application/json"
                },
                "body": json.dumps({
                    "error": "Student not found"
                })
            }

    elif httpMethods == "DELETE":
        info = event.get("pathParameters") or {}
        student_id = info.get("studentId", "")

        s3_path = f"students/{student_id}.json"

        try:
            file_delete = s3.delete_object(
                Bucket = bucket_name,
                Key = s3_path
            )

            return {
                "statusCode": 200,
                "headers": {
                    "ContentType": "application/json"
                },
                "body": json.dumps({
                    "message": "Student deleted successfully"
                })
            }
        
        except Exception as e:
            return {
                "statusCode": 404,
                "headers": {
                    "ContenType": "application/json"
                },
                "body": json.dumps({
                    "error": "Student not found"
                })
            }

    return {
        "statusCode": 400,
        "body": json.dumps({"message": "Unsupported method"})
    }
