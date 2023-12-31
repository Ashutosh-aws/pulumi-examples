// *** WARNING: this file was generated by crd2pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Outputs.Configuration.V1
{

    /// <summary>
    /// NamespacedSecretValueFromSource represents the source of a secret value specifying the secret namespace
    /// </summary>
    [OutputType]
    public sealed class KongClusterPluginConfigfromSecretkeyref
    {
        /// <summary>
        /// the key containing the value
        /// </summary>
        public readonly string Key;
        /// <summary>
        /// the secret containing the key
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The namespace containing the secret
        /// </summary>
        public readonly string Namespace;

        [OutputConstructor]
        private KongClusterPluginConfigfromSecretkeyref(
            string key,

            string name,

            string @namespace)
        {
            Key = key;
            Name = name;
            Namespace = @namespace;
        }
    }
}
