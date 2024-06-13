from src.app import main

if __name__ == "__main__":
    event_by_sqs_trigger = {
        "Records": [
            {
                "messageId": "ad956138-7c34-4897-938a-ae832701e434",
                "receiptHandle": "AQXLyd9YSMvhxhyircETPk0KuNVzouCAyKfd",
                "body": '{"update": true, "token": "456", "sku": "123","product": {"sku": "123", "price": "123.08"}}',
                "attributes": {
                    "ApproximateReceiveCount": "1",
                    "SentTimestamp": "1642657839344",
                    "SequenceNumber": "18867264480581615872",
                    "MessageGroupId": "comms_cards",
                    "SenderId": "AROAIF5RVFVVU2CA7A4HG:wolf-sender",
                    "MessageDeduplicationId": "b83dafcd0a283f09eb5e644b0161969a2bec610a413ff4b30f85490048f930cf",
                    "ApproximateFirstReceiveTimestamp": "1642657856151",
                },
                "messageAttributes": {},
                "md5OfBody": "f6bdaa20df256d77243cd96c5bd3c90a",
                "eventSource": "aws:sqs",
                "eventSourceARN": "arn:aws:sqs:us-west-2:180477243137:MyQueue",
                "awsRegion": "us-east-2",
            }
        ]
    }

    resp = main(event_by_sqs_trigger, None)
    print(resp)
