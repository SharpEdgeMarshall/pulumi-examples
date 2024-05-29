import json

import pulumi_aws as aws


def wrong_way():
    # Create an S3 bucket
    s3_bucket = aws.s3.Bucket("myBucket")

    # Create the policy inside the apply callback
    s3_bucket.arn.apply(
        lambda arn: aws.s3.BucketPolicy(
            "myBucketPolicy",
            bucket=s3_bucket.id,
            policy=json.dumps(
                {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {"Service": "lambda.amazonaws.com"},
                            "Action": ["s3:PutObject", "s3:PutObjectAcl"],
                            "Resource": f"{arn}/*",
                        }
                    ],
                }
            ),
        )
    )


def good_way():
    # Create an S3 bucket
    s3_bucket = aws.s3.Bucket("myBucket")

    # IAM Policy Document that allows the Lambda service to write to the S3 bucket
    s3_bucket_policy_document = s3_bucket.arn.apply(
        lambda arn: json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {"Service": "lambda.amazonaws.com"},
                        "Action": ["s3:PutObject", "s3:PutObjectAcl"],
                        "Resource": f"{arn}/*",
                    }
                ],
            }
        )
    )

    # Attach the policy to the bucket
    s3_bucket_policy = aws.s3.BucketPolicy(
        "myBucketPolicy",
        bucket=s3_bucket.id,
        policy=s3_bucket_policy_document,
    )
