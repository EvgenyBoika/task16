#!/usr/bin/python3

import boto3

def publish_to_sns(sub, msg):
    topic_arn = "arn:aws:sns:us-east-1:371428523361:Commit"
    sns = boto3.client("sns")
    response = sns.publish(
        TopicArn=topic_arn,
        Message=msg,
        Subject=sub
    )
publish_to_sns("Commit","This man made a commit")