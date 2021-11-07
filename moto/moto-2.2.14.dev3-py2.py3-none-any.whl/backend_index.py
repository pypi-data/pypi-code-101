# autogenerated by /Users/markus/git_projects_os/moto/scripts/update_backend_index.py
import re

backend_url_patterns = [
    ("acm", re.compile("https?://acm\\.(.+)\\.amazonaws\\.com")),
    ("apigateway", re.compile("https?://apigateway\\.(.+)\\.amazonaws.com")),
    (
        "applicationautoscaling",
        re.compile("https?://application-autoscaling\\.(.+)\\.amazonaws.com"),
    ),
    ("athena", re.compile("https?://athena\\.(.+)\\.amazonaws\\.com")),
    ("autoscaling", re.compile("https?://autoscaling\\.(.+)\\.amazonaws\\.com")),
    ("batch", re.compile("https?://batch\\.(.+)\\.amazonaws.com")),
    ("cloudformation", re.compile("https?://cloudformation\\.(.+)\\.amazonaws\\.com")),
    ("cloudtrail", re.compile("https?://cloudtrail\\.(.+)\\.amazonaws\\.com")),
    ("cloudwatch", re.compile("https?://monitoring\\.(.+)\\.amazonaws.com")),
    ("codecommit", re.compile("https?://codecommit\\.(.+)\\.amazonaws\\.com")),
    ("codepipeline", re.compile("https?://codepipeline\\.(.+)\\.amazonaws\\.com")),
    (
        "cognito-identity",
        re.compile("https?://cognito-identity\\.(.+)\\.amazonaws.com"),
    ),
    ("cognito-idp", re.compile("https?://cognito-idp\\.(.+)\\.amazonaws.com")),
    ("config", re.compile("https?://config\\.(.+)\\.amazonaws\\.com")),
    ("datapipeline", re.compile("https?://datapipeline\\.(.+)\\.amazonaws\\.com")),
    ("datasync", re.compile("https?://(.*\\.)?(datasync)\\.(.+)\\.amazonaws.com")),
    ("dms", re.compile("https?://dms\\.(.+)\\.amazonaws\\.com")),
    ("ds", re.compile("https?://ds\\.(.+)\\.amazonaws\\.com")),
    ("dynamodb", re.compile("https?://dynamodb\\.(.+)\\.amazonaws\\.com")),
    ("dynamodb2", re.compile("https?://dynamodb\\.(.+)\\.amazonaws\\.com")),
    (
        "dynamodbstreams",
        re.compile("https?://streams\\.dynamodb\\.(.+)\\.amazonaws.com"),
    ),
    ("ec2", re.compile("https?://ec2\\.(.+)\\.amazonaws\\.com(|\\.cn)")),
    (
        "ec2instanceconnect",
        re.compile("https?://ec2-instance-connect\\.(.+)\\.amazonaws\\.com"),
    ),
    ("ecr", re.compile("https?://ecr\\.(.+)\\.amazonaws\\.com")),
    ("ecr", re.compile("https?://api\\.ecr\\.(.+)\\.amazonaws\\.com")),
    ("ecs", re.compile("https?://ecs\\.(.+)\\.amazonaws\\.com")),
    ("efs", re.compile("https?://elasticfilesystem\\.(.+)\\.amazonaws.com")),
    ("efs", re.compile("https?://elasticfilesystem\\.amazonaws.com")),
    ("eks", re.compile("https?://eks\\.(.+)\\.amazonaws.com")),
    (
        "elasticbeanstalk",
        re.compile(
            "https?://elasticbeanstalk\\.(?P<region>[a-zA-Z0-9\\-_]+)\\.amazonaws.com"
        ),
    ),
    (
        "elastictranscoder",
        re.compile("https?://elastictranscoder\\.(.+)\\.amazonaws.com"),
    ),
    ("elb", re.compile("https?://elasticloadbalancing\\.(.+)\\.amazonaws.com")),
    ("elbv2", re.compile("https?://elasticloadbalancing\\.(.+)\\.amazonaws.com")),
    ("emr", re.compile("https?://(.+)\\.elasticmapreduce\\.amazonaws.com")),
    ("emr", re.compile("https?://elasticmapreduce\\.(.+)\\.amazonaws.com")),
    ("emr-containers", re.compile("https?://emr-containers\\.(.+)\\.amazonaws\\.com")),
    ("events", re.compile("https?://events\\.(.+)\\.amazonaws\\.com")),
    ("firehose", re.compile("https?://firehose\\.(.+)\\.amazonaws\\.com")),
    ("forecast", re.compile("https?://forecast\\.(.+)\\.amazonaws\\.com")),
    ("glacier", re.compile("https?://glacier\\.(.+)\\.amazonaws.com")),
    ("glue", re.compile("https?://glue\\.(.+)\\.amazonaws\\.com")),
    ("iam", re.compile("https?://iam\\.(.*\\.)?amazonaws\\.com")),
    ("iot", re.compile("https?://iot\\.(.+)\\.amazonaws\\.com")),
    ("iot-data", re.compile("https?://data\\.iot\\.(.+)\\.amazonaws.com")),
    ("kinesis", re.compile("https?://kinesis\\.(.+)\\.amazonaws\\.com")),
    ("kinesisvideo", re.compile("https?://kinesisvideo\\.(.+)\\.amazonaws.com")),
    (
        "kinesis-video-archived-media",
        re.compile("https?://.*\\.kinesisvideo\\.(.+)\\.amazonaws.com"),
    ),
    ("kms", re.compile("https?://kms\\.(.+)\\.amazonaws\\.com")),
    ("lambda", re.compile("https?://lambda\\.(.+)\\.amazonaws\\.com")),
    ("logs", re.compile("https?://logs\\.(.+)\\.amazonaws\\.com")),
    (
        "managedblockchain",
        re.compile("https?://managedblockchain\\.(.+)\\.amazonaws.com"),
    ),
    ("mediaconnect", re.compile("https?://mediaconnect\\.(.+)\\.amazonaws.com")),
    ("medialive", re.compile("https?://medialive\\.(.+)\\.amazonaws.com")),
    ("mediapackage", re.compile("https?://mediapackage\\.(.+)\\.amazonaws.com")),
    ("mediastore", re.compile("https?://mediastore\\.(.+)\\.amazonaws\\.com")),
    ("mediastore-data", re.compile("https?://data.mediastore\\.(.+)\\.amazonaws.com")),
    ("opsworks", re.compile("https?://opsworks\\.us-east-1\\.amazonaws.com")),
    ("organizations", re.compile("https?://organizations\\.(.+)\\.amazonaws\\.com")),
    ("polly", re.compile("https?://polly\\.(.+)\\.amazonaws.com")),
    ("ram", re.compile("https?://ram\\.(.+)\\.amazonaws.com")),
    ("rds", re.compile("https?://rds\\.(.+)\\.amazonaws\\.com")),
    ("rds", re.compile("https?://rds\\.amazonaws\\.com")),
    ("redshift", re.compile("https?://redshift\\.(.+)\\.amazonaws\\.com")),
    (
        "resource-groups",
        re.compile("https?://resource-groups(-fips)?\\.(.+)\\.amazonaws.com"),
    ),
    ("resourcegroupstaggingapi", re.compile("https?://tagging\\.(.+)\\.amazonaws.com")),
    ("route53", re.compile("https?://route53(.*)\\.amazonaws.com")),
    ("s3", re.compile("https?://s3(.*)\\.amazonaws.com")),
    (
        "s3",
        re.compile(
            "https?://(?P<bucket_name>[a-zA-Z0-9\\-_.]*)\\.?s3(.*)\\.amazonaws.com"
        ),
    ),
    ("sagemaker", re.compile("https?://api.sagemaker\\.(.+)\\.amazonaws.com")),
    ("secretsmanager", re.compile("https?://secretsmanager\\.(.+)\\.amazonaws\\.com")),
    ("ses", re.compile("https?://email\\.(.+)\\.amazonaws\\.com")),
    ("ses", re.compile("https?://ses\\.(.+)\\.amazonaws\\.com")),
    ("sns", re.compile("https?://sns\\.(.+)\\.amazonaws\\.com")),
    ("sqs", re.compile("https?://(.*\\.)?(queue|sqs)\\.(.*\\.)?amazonaws\\.com")),
    ("ssm", re.compile("https?://ssm\\.(.+)\\.amazonaws\\.com")),
    ("ssm", re.compile("https?://ssm\\.(.+)\\.amazonaws\\.com\\.cn")),
    ("stepfunctions", re.compile("https?://states\\.(.+)\\.amazonaws.com")),
    ("sts", re.compile("https?://sts\\.(.*\\.)?amazonaws\\.com")),
    ("support", re.compile("https?://support\\.(.+)\\.amazonaws\\.com")),
    ("swf", re.compile("https?://swf\\.(.+)\\.amazonaws\\.com")),
    (
        "timestream-write",
        re.compile("https?://ingest\\.timestream\\.(.+)\\.amazonaws\\.com"),
    ),
    (
        "timestream-write",
        re.compile("https?://ingest\\.timestream\\.(.+)\\.amazonaws\\.com/"),
    ),
    ("transcribe", re.compile("https?://transcribe\\.(.+)\\.amazonaws\\.com")),
    ("wafv2", re.compile("https?://wafv2\\.(.+)\\.amazonaws.com")),
    ("xray", re.compile("https?://xray\\.(.+)\\.amazonaws.com")),
]
