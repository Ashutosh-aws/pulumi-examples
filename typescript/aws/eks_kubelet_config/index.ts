import * as pulumi from "@pulumi/pulumi"
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";
import * as cloudinit from "@pulumi/cloudinit";
import * as custom from "./reserved";

const name = 'nginx-helm-helm'

const config = new pulumi.Config("aws");
const profile = config.require("profile")

const vpc = new awsx.ec2.Vpc(`${name}-vpc`, {
    cidrBlock: "172.16.0.0/24",
    subnets: [
        {
            type: "private",
            tags: {
                "kubernetes.io/role/internal-elb": "1",
            }
        },
        {
            type: "public",
            tags: {
                "kubernetes.io/role/elb": "1",
            }
        }],
    tags: {
        Name: `${name}-vpc`,
        Owner: "lbriggs",
        owner: "lbriggs",
    }
});

const kubeconfigOpts: eks.KubeconfigOptions = {profileName: profile};

const cluster = new eks.Cluster(name, {
    providerCredentialOpts: kubeconfigOpts,
    vpcId: vpc.id,
    privateSubnetIds: vpc.privateSubnetIds,
    publicSubnetIds: vpc.publicSubnetIds,
    instanceType: "t2.medium",
    desiredCapacity: 2,
    minSize: 1,
    maxSize: 2,
    createOidcProvider: true,
    tags: {
        Owner: "lbriggs",
        owner: "lbriggs",
    }
});

const group = new custom.ReservedNodeGroup("extra", {
    nodeSubnetIds: vpc.privateSubnetIds,
    kubeReservedMemory: "128Mi",
    systemReservedMemory: "25Mi",
    cluster: cluster,
})


vpc.privateSubnetIds.then(id => id.forEach((id, index) => {
    new aws.ec2.Tag(`subnettag-${index}`, {
        key: cluster.eksCluster.name.apply(name => `kubernetes.io/cluster/${name}`),
        resourceId: id,
        value: "owned",
    }, { parent: cluster})
}))

export const clusterName = cluster.eksCluster.name
export const kubeconfig = cluster.kubeconfig
export const oidcUrl = cluster.core.oidcProvider?.url
export const oidcArn = cluster.core.oidcProvider?.arn
