# coding=utf-8
# *** WARNING: this file was generated by crd2pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'TelemetrySpec',
    'TelemetrySpecAccessLogging',
    'TelemetrySpecAccessLoggingFilter',
    'TelemetrySpecAccessLoggingProviders',
    'TelemetrySpecMetrics',
    'TelemetrySpecMetricsOverrides',
    'TelemetrySpecMetricsOverridesTagOverrides',
    'TelemetrySpecMetricsProviders',
    'TelemetrySpecSelector',
    'TelemetrySpecTracing',
    'TelemetrySpecTracingProviders',
]

@pulumi.output_type
class TelemetrySpec(dict):
    """
    Telemetry configuration for workloads. See more details at: https://istio.io/docs/reference/config/telemetry.html
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "accessLogging":
            suggest = "access_logging"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TelemetrySpec. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TelemetrySpec.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TelemetrySpec.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 access_logging: Optional[Sequence['outputs.TelemetrySpecAccessLogging']] = None,
                 metrics: Optional[Sequence['outputs.TelemetrySpecMetrics']] = None,
                 selector: Optional['outputs.TelemetrySpecSelector'] = None,
                 tracing: Optional[Sequence['outputs.TelemetrySpecTracing']] = None):
        """
        Telemetry configuration for workloads. See more details at: https://istio.io/docs/reference/config/telemetry.html
        :param Sequence['TelemetrySpecAccessLoggingArgs'] access_logging: Optional.
        :param Sequence['TelemetrySpecMetricsArgs'] metrics: Optional.
        :param 'TelemetrySpecSelectorArgs' selector: Optional.
        :param Sequence['TelemetrySpecTracingArgs'] tracing: Optional.
        """
        if access_logging is not None:
            pulumi.set(__self__, "access_logging", access_logging)
        if metrics is not None:
            pulumi.set(__self__, "metrics", metrics)
        if selector is not None:
            pulumi.set(__self__, "selector", selector)
        if tracing is not None:
            pulumi.set(__self__, "tracing", tracing)

    @property
    @pulumi.getter(name="accessLogging")
    def access_logging(self) -> Optional[Sequence['outputs.TelemetrySpecAccessLogging']]:
        """
        Optional.
        """
        return pulumi.get(self, "access_logging")

    @property
    @pulumi.getter
    def metrics(self) -> Optional[Sequence['outputs.TelemetrySpecMetrics']]:
        """
        Optional.
        """
        return pulumi.get(self, "metrics")

    @property
    @pulumi.getter
    def selector(self) -> Optional['outputs.TelemetrySpecSelector']:
        """
        Optional.
        """
        return pulumi.get(self, "selector")

    @property
    @pulumi.getter
    def tracing(self) -> Optional[Sequence['outputs.TelemetrySpecTracing']]:
        """
        Optional.
        """
        return pulumi.get(self, "tracing")


@pulumi.output_type
class TelemetrySpecAccessLogging(dict):
    def __init__(__self__, *,
                 disabled: Optional[bool] = None,
                 filter: Optional['outputs.TelemetrySpecAccessLoggingFilter'] = None,
                 providers: Optional[Sequence['outputs.TelemetrySpecAccessLoggingProviders']] = None):
        """
        :param bool disabled: Controls logging.
        :param 'TelemetrySpecAccessLoggingFilterArgs' filter: Optional.
        :param Sequence['TelemetrySpecAccessLoggingProvidersArgs'] providers: Optional.
        """
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if providers is not None:
            pulumi.set(__self__, "providers", providers)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[bool]:
        """
        Controls logging.
        """
        return pulumi.get(self, "disabled")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.TelemetrySpecAccessLoggingFilter']:
        """
        Optional.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def providers(self) -> Optional[Sequence['outputs.TelemetrySpecAccessLoggingProviders']]:
        """
        Optional.
        """
        return pulumi.get(self, "providers")


@pulumi.output_type
class TelemetrySpecAccessLoggingFilter(dict):
    """
    Optional.
    """
    def __init__(__self__, *,
                 expression: Optional[str] = None):
        """
        Optional.
        :param str expression: CEL expression for selecting when requests/connections should be logged.
        """
        if expression is not None:
            pulumi.set(__self__, "expression", expression)

    @property
    @pulumi.getter
    def expression(self) -> Optional[str]:
        """
        CEL expression for selecting when requests/connections should be logged.
        """
        return pulumi.get(self, "expression")


@pulumi.output_type
class TelemetrySpecAccessLoggingProviders(dict):
    def __init__(__self__, *,
                 name: Optional[str] = None):
        """
        :param str name: Required.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Required.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class TelemetrySpecMetrics(dict):
    def __init__(__self__, *,
                 overrides: Optional[Sequence['outputs.TelemetrySpecMetricsOverrides']] = None,
                 providers: Optional[Sequence['outputs.TelemetrySpecMetricsProviders']] = None):
        """
        :param Sequence['TelemetrySpecMetricsOverridesArgs'] overrides: Optional.
        :param Sequence['TelemetrySpecMetricsProvidersArgs'] providers: Optional.
        """
        if overrides is not None:
            pulumi.set(__self__, "overrides", overrides)
        if providers is not None:
            pulumi.set(__self__, "providers", providers)

    @property
    @pulumi.getter
    def overrides(self) -> Optional[Sequence['outputs.TelemetrySpecMetricsOverrides']]:
        """
        Optional.
        """
        return pulumi.get(self, "overrides")

    @property
    @pulumi.getter
    def providers(self) -> Optional[Sequence['outputs.TelemetrySpecMetricsProviders']]:
        """
        Optional.
        """
        return pulumi.get(self, "providers")


@pulumi.output_type
class TelemetrySpecMetricsOverrides(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "tagOverrides":
            suggest = "tag_overrides"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TelemetrySpecMetricsOverrides. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TelemetrySpecMetricsOverrides.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TelemetrySpecMetricsOverrides.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 disabled: Optional[bool] = None,
                 match: Optional[Any] = None,
                 tag_overrides: Optional[Mapping[str, 'outputs.TelemetrySpecMetricsOverridesTagOverrides']] = None):
        """
        :param bool disabled: Optional.
        :param Any match: Match allows provides the scope of the override.
        :param Mapping[str, 'TelemetrySpecMetricsOverridesTagOverridesArgs'] tag_overrides: Optional.
        """
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if match is not None:
            pulumi.set(__self__, "match", match)
        if tag_overrides is not None:
            pulumi.set(__self__, "tag_overrides", tag_overrides)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[bool]:
        """
        Optional.
        """
        return pulumi.get(self, "disabled")

    @property
    @pulumi.getter
    def match(self) -> Optional[Any]:
        """
        Match allows provides the scope of the override.
        """
        return pulumi.get(self, "match")

    @property
    @pulumi.getter(name="tagOverrides")
    def tag_overrides(self) -> Optional[Mapping[str, 'outputs.TelemetrySpecMetricsOverridesTagOverrides']]:
        """
        Optional.
        """
        return pulumi.get(self, "tag_overrides")


@pulumi.output_type
class TelemetrySpecMetricsOverridesTagOverrides(dict):
    def __init__(__self__, *,
                 operation: Optional[str] = None,
                 value: Optional[str] = None):
        """
        :param str operation: Operation controls whether or not to update/add a tag, or to remove it.
        :param str value: Value is only considered if the operation is `UPSERT`.
        """
        if operation is not None:
            pulumi.set(__self__, "operation", operation)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def operation(self) -> Optional[str]:
        """
        Operation controls whether or not to update/add a tag, or to remove it.
        """
        return pulumi.get(self, "operation")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Value is only considered if the operation is `UPSERT`.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class TelemetrySpecMetricsProviders(dict):
    def __init__(__self__, *,
                 name: Optional[str] = None):
        """
        :param str name: Required.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Required.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class TelemetrySpecSelector(dict):
    """
    Optional.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "matchLabels":
            suggest = "match_labels"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TelemetrySpecSelector. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TelemetrySpecSelector.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TelemetrySpecSelector.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 match_labels: Optional[Mapping[str, str]] = None):
        """
        Optional.
        """
        if match_labels is not None:
            pulumi.set(__self__, "match_labels", match_labels)

    @property
    @pulumi.getter(name="matchLabels")
    def match_labels(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "match_labels")


@pulumi.output_type
class TelemetrySpecTracing(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "customTags":
            suggest = "custom_tags"
        elif key == "disableSpanReporting":
            suggest = "disable_span_reporting"
        elif key == "randomSamplingPercentage":
            suggest = "random_sampling_percentage"
        elif key == "useRequestIdForTraceSampling":
            suggest = "use_request_id_for_trace_sampling"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TelemetrySpecTracing. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TelemetrySpecTracing.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TelemetrySpecTracing.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 custom_tags: Optional[Mapping[str, Any]] = None,
                 disable_span_reporting: Optional[bool] = None,
                 providers: Optional[Sequence['outputs.TelemetrySpecTracingProviders']] = None,
                 random_sampling_percentage: Optional[float] = None,
                 use_request_id_for_trace_sampling: Optional[bool] = None):
        """
        :param Mapping[str, Any] custom_tags: Optional.
        :param bool disable_span_reporting: Controls span reporting.
        :param Sequence['TelemetrySpecTracingProvidersArgs'] providers: Optional.
        """
        if custom_tags is not None:
            pulumi.set(__self__, "custom_tags", custom_tags)
        if disable_span_reporting is not None:
            pulumi.set(__self__, "disable_span_reporting", disable_span_reporting)
        if providers is not None:
            pulumi.set(__self__, "providers", providers)
        if random_sampling_percentage is not None:
            pulumi.set(__self__, "random_sampling_percentage", random_sampling_percentage)
        if use_request_id_for_trace_sampling is not None:
            pulumi.set(__self__, "use_request_id_for_trace_sampling", use_request_id_for_trace_sampling)

    @property
    @pulumi.getter(name="customTags")
    def custom_tags(self) -> Optional[Mapping[str, Any]]:
        """
        Optional.
        """
        return pulumi.get(self, "custom_tags")

    @property
    @pulumi.getter(name="disableSpanReporting")
    def disable_span_reporting(self) -> Optional[bool]:
        """
        Controls span reporting.
        """
        return pulumi.get(self, "disable_span_reporting")

    @property
    @pulumi.getter
    def providers(self) -> Optional[Sequence['outputs.TelemetrySpecTracingProviders']]:
        """
        Optional.
        """
        return pulumi.get(self, "providers")

    @property
    @pulumi.getter(name="randomSamplingPercentage")
    def random_sampling_percentage(self) -> Optional[float]:
        return pulumi.get(self, "random_sampling_percentage")

    @property
    @pulumi.getter(name="useRequestIdForTraceSampling")
    def use_request_id_for_trace_sampling(self) -> Optional[bool]:
        return pulumi.get(self, "use_request_id_for_trace_sampling")


@pulumi.output_type
class TelemetrySpecTracingProviders(dict):
    def __init__(__self__, *,
                 name: Optional[str] = None):
        """
        :param str name: Required.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Required.
        """
        return pulumi.get(self, "name")


