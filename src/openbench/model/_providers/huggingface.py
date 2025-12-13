"""Hugging Face Inference Providers - backwards compatibility wrapper.

Re-exports inspect-ai's HFInferenceProvidersAPI under the 'huggingface' name.
"""

from inspect_ai.model._providers.hf_inference_providers import (  # type: ignore[import-not-found]
    HFInferenceProvidersAPI,
)

__all__ = ["HFInferenceProvidersAPI"]
