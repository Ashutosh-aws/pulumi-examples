// Code generated by crd2pulumi DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// KongClusterPlugin is the Schema for the kongclusterplugins API
type KongClusterPlugin struct {
	pulumi.CustomResourceState

	ApiVersion pulumi.StringPtrOutput `pulumi:"apiVersion"`
	// Config contains the plugin configuration.
	Config pulumi.MapOutput `pulumi:"config"`
	// ConfigFrom references a secret containing the plugin configuration.
	ConfigFrom KongClusterPluginConfigfromPtrOutput `pulumi:"configFrom"`
	// ConsumerRef is a reference to a particular consumer
	ConsumerRef pulumi.StringPtrOutput `pulumi:"consumerRef"`
	// Disabled set if the plugin is disabled or not
	Disabled pulumi.BoolPtrOutput       `pulumi:"disabled"`
	Kind     pulumi.StringPtrOutput     `pulumi:"kind"`
	Metadata metav1.ObjectMetaPtrOutput `pulumi:"metadata"`
	// Ordering overrides the normal plugin execution order
	Ordering KongClusterPluginOrderingPtrOutput `pulumi:"ordering"`
	// PluginName is the name of the plugin to which to apply the config
	Plugin pulumi.StringOutput `pulumi:"plugin"`
	// Protocols configures plugin to run on requests received on specific protocols.
	Protocols pulumi.StringArrayOutput `pulumi:"protocols"`
	// RunOn configures the plugin to run on the first or the second or both nodes in case of a service mesh deployment.
	Run_on pulumi.StringPtrOutput `pulumi:"run_on"`
}

// NewKongClusterPlugin registers a new resource with the given unique name, arguments, and options.
func NewKongClusterPlugin(ctx *pulumi.Context,
	name string, args *KongClusterPluginArgs, opts ...pulumi.ResourceOption) (*KongClusterPlugin, error) {
	if args == nil {
		args = &KongClusterPluginArgs{}
	}

	args.ApiVersion = pulumi.StringPtr("configuration.konghq.com/v1")
	args.Kind = pulumi.StringPtr("KongClusterPlugin")
	var resource KongClusterPlugin
	err := ctx.RegisterResource("kubernetes:configuration.konghq.com/v1:KongClusterPlugin", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetKongClusterPlugin gets an existing KongClusterPlugin resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetKongClusterPlugin(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *KongClusterPluginState, opts ...pulumi.ResourceOption) (*KongClusterPlugin, error) {
	var resource KongClusterPlugin
	err := ctx.ReadResource("kubernetes:configuration.konghq.com/v1:KongClusterPlugin", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering KongClusterPlugin resources.
type kongClusterPluginState struct {
}

type KongClusterPluginState struct {
}

func (KongClusterPluginState) ElementType() reflect.Type {
	return reflect.TypeOf((*kongClusterPluginState)(nil)).Elem()
}

type kongClusterPluginArgs struct {
	ApiVersion *string `pulumi:"apiVersion"`
	// Config contains the plugin configuration.
	Config map[string]interface{} `pulumi:"config"`
	// ConfigFrom references a secret containing the plugin configuration.
	ConfigFrom *KongClusterPluginConfigfrom `pulumi:"configFrom"`
	// ConsumerRef is a reference to a particular consumer
	ConsumerRef *string `pulumi:"consumerRef"`
	// Disabled set if the plugin is disabled or not
	Disabled *bool              `pulumi:"disabled"`
	Kind     *string            `pulumi:"kind"`
	Metadata *metav1.ObjectMeta `pulumi:"metadata"`
	// Ordering overrides the normal plugin execution order
	Ordering *KongClusterPluginOrdering `pulumi:"ordering"`
	// PluginName is the name of the plugin to which to apply the config
	Plugin *string `pulumi:"plugin"`
	// Protocols configures plugin to run on requests received on specific protocols.
	Protocols []string `pulumi:"protocols"`
	// RunOn configures the plugin to run on the first or the second or both nodes in case of a service mesh deployment.
	Run_on *string `pulumi:"run_on"`
}

// The set of arguments for constructing a KongClusterPlugin resource.
type KongClusterPluginArgs struct {
	ApiVersion pulumi.StringPtrInput
	// Config contains the plugin configuration.
	Config pulumi.MapInput
	// ConfigFrom references a secret containing the plugin configuration.
	ConfigFrom KongClusterPluginConfigfromPtrInput
	// ConsumerRef is a reference to a particular consumer
	ConsumerRef pulumi.StringPtrInput
	// Disabled set if the plugin is disabled or not
	Disabled pulumi.BoolPtrInput
	Kind     pulumi.StringPtrInput
	Metadata metav1.ObjectMetaPtrInput
	// Ordering overrides the normal plugin execution order
	Ordering KongClusterPluginOrderingPtrInput
	// PluginName is the name of the plugin to which to apply the config
	Plugin pulumi.StringPtrInput
	// Protocols configures plugin to run on requests received on specific protocols.
	Protocols pulumi.StringArrayInput
	// RunOn configures the plugin to run on the first or the second or both nodes in case of a service mesh deployment.
	Run_on pulumi.StringPtrInput
}

func (KongClusterPluginArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*kongClusterPluginArgs)(nil)).Elem()
}

type KongClusterPluginInput interface {
	pulumi.Input

	ToKongClusterPluginOutput() KongClusterPluginOutput
	ToKongClusterPluginOutputWithContext(ctx context.Context) KongClusterPluginOutput
}

func (*KongClusterPlugin) ElementType() reflect.Type {
	return reflect.TypeOf((**KongClusterPlugin)(nil)).Elem()
}

func (i *KongClusterPlugin) ToKongClusterPluginOutput() KongClusterPluginOutput {
	return i.ToKongClusterPluginOutputWithContext(context.Background())
}

func (i *KongClusterPlugin) ToKongClusterPluginOutputWithContext(ctx context.Context) KongClusterPluginOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KongClusterPluginOutput)
}

type KongClusterPluginOutput struct{ *pulumi.OutputState }

func (KongClusterPluginOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**KongClusterPlugin)(nil)).Elem()
}

func (o KongClusterPluginOutput) ToKongClusterPluginOutput() KongClusterPluginOutput {
	return o
}

func (o KongClusterPluginOutput) ToKongClusterPluginOutputWithContext(ctx context.Context) KongClusterPluginOutput {
	return o
}

func (o KongClusterPluginOutput) ApiVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *KongClusterPlugin) pulumi.StringPtrOutput { return v.ApiVersion }).(pulumi.StringPtrOutput)
}

// Config contains the plugin configuration.
func (o KongClusterPluginOutput) Config() pulumi.MapOutput {
	return o.ApplyT(func(v *KongClusterPlugin) pulumi.MapOutput { return v.Config }).(pulumi.MapOutput)
}

// ConfigFrom references a secret containing the plugin configuration.
func (o KongClusterPluginOutput) ConfigFrom() KongClusterPluginConfigfromPtrOutput {
	return o.ApplyT(func(v *KongClusterPlugin) KongClusterPluginConfigfromPtrOutput { return v.ConfigFrom }).(KongClusterPluginConfigfromPtrOutput)
}

// ConsumerRef is a reference to a particular consumer
func (o KongClusterPluginOutput) ConsumerRef() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *KongClusterPlugin) pulumi.StringPtrOutput { return v.ConsumerRef }).(pulumi.StringPtrOutput)
}

// Disabled set if the plugin is disabled or not
func (o KongClusterPluginOutput) Disabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *KongClusterPlugin) pulumi.BoolPtrOutput { return v.Disabled }).(pulumi.BoolPtrOutput)
}

func (o KongClusterPluginOutput) Kind() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *KongClusterPlugin) pulumi.StringPtrOutput { return v.Kind }).(pulumi.StringPtrOutput)
}

func (o KongClusterPluginOutput) Metadata() metav1.ObjectMetaPtrOutput {
	return o.ApplyT(func(v *KongClusterPlugin) metav1.ObjectMetaPtrOutput { return v.Metadata }).(metav1.ObjectMetaPtrOutput)
}

// Ordering overrides the normal plugin execution order
func (o KongClusterPluginOutput) Ordering() KongClusterPluginOrderingPtrOutput {
	return o.ApplyT(func(v *KongClusterPlugin) KongClusterPluginOrderingPtrOutput { return v.Ordering }).(KongClusterPluginOrderingPtrOutput)
}

// PluginName is the name of the plugin to which to apply the config
func (o KongClusterPluginOutput) Plugin() pulumi.StringOutput {
	return o.ApplyT(func(v *KongClusterPlugin) pulumi.StringOutput { return v.Plugin }).(pulumi.StringOutput)
}

// Protocols configures plugin to run on requests received on specific protocols.
func (o KongClusterPluginOutput) Protocols() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *KongClusterPlugin) pulumi.StringArrayOutput { return v.Protocols }).(pulumi.StringArrayOutput)
}

// RunOn configures the plugin to run on the first or the second or both nodes in case of a service mesh deployment.
func (o KongClusterPluginOutput) Run_on() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *KongClusterPlugin) pulumi.StringPtrOutput { return v.Run_on }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*KongClusterPluginInput)(nil)).Elem(), &KongClusterPlugin{})
	pulumi.RegisterOutputType(KongClusterPluginOutput{})
}
