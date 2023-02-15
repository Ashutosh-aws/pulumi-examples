"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws
import boto3 as boto


def wait_for_loadbalancer(arn: str) -> str:
    if pulumi.is_dry_run():
        return arn

    client = boto.client("elbv2")

    pulumi.log.info(
        msg="Waiting for ELB to be active",
        ephemeral=True,
    )

    waiter = client.get_waiter("load_balancer_available")

    waiter.wait(LoadBalancerArns=[arn], WaitConfig={"Delay": 45, "MaxAttempts": 10})

    pulumi.log.info(msg="LoadBalancer is Active", ephemeral=True)

    return arn


default_vpc = aws.ec2.get_vpc(default=True)
default_vpc_subnets = aws.ec2.get_subnet_ids(vpc_id=default_vpc.id)

lb = aws.lb.LoadBalancer(
    "lbriggs-lb",
    subnets=default_vpc_subnets.ids,
)

result = lb.arn.apply(lambda a: wait_for_loadbalancer(arn=a))
