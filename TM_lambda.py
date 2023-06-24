import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('Tasks')
    
    # The event object should include your data
    task_id = event['taskID']
    content = event['content']
    creation_date = event['creationDate']
    completion_date = event['completionDate']
    status = event['status']
    
    try:
        response = table.put_item(
           Item={
                'taskID': task_id,
                'content': content,
                'creationDate': creation_date,
                'completionDate': completion_date,
                'status': status
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {
            'statusCode': 500,
            'body': e.response['Error']['Message']
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('Success!')
        }
