class Service:
    def __init__(self, client, arn):
        self.client = client
        self.arn = self._long_arn(arn)
        self.name = arn.split("/")[-1]

    @property
    def hostname(self):
        hostname = f"{self.name}.{self.client.namespace}"
        return hostname

    @property
    def tags(self):
        tags = self.client.ecs.list_tags_for_resource(resourceArn=self.arn).get("tags")
        return dict([(tag["key"], tag["value"]) for tag in tags])

    def _long_arn(self, arn):
        # https://docs.aws.amazon.com/AmazonECS/latest/userguide/ecs-account-settings.html#ecs-resource-ids
        arn_parts = arn.split("/")
        if len(arn_parts) == 3:
            # A new long arn:
            # arn:aws:ecs:region:aws_account_id:service/cluster-name/service-name
            # Return it as is
            return arn
        else:
            # An old short arn:
            # arn:aws:ecs:region:aws_account_id:service/service-name
            # Add the cluster name
            return "/".join([arn_parts[0], self.client.cluster_name, arn_parts[1]])
