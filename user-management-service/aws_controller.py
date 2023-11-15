import boto3


class DynamodbTable:
    def __init__(self, table_name):
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table(table_name)

    def get_user(self, email):
        response = self.table.get_item(
            Key={
                'email': email
            }
        )
        return response['Item']
    
    def get_password_hash(self, email):
        response = self.table.get_item(
            Key={
                'email': email
            }
        )
        return response['Item']['password_hash']
    
    def check_user_exist(self, email):
        response = self.table.get_item(
            Key={
                'email': email
            }
        )
        return 'Item' in response
    
    def add_user(self, email, password_hash):
        self.table.put_item(
            Item={
                'email': email,
                'password_hash': password_hash
            }
        )

    def delete_user(self, email):
        self.table.delete_item(
            Key={
                'email': email
            }
        )
        
table = DynamodbTable('anemone-user')
print(table.check_user_exist('dynamodb_controller@test.com'))