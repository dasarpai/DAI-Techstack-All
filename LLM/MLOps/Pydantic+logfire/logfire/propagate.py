"""This module provides a thin wrapper around the OpenTelemetry propagate API to allow
the OpenTelemetry contexts (and therefore Logfire contexts) to be transferred between
different code running in different threads, processes or even services.

In general, you should not need to use this module since Logfire will automatically
patch [`ThreadPoolExecutor`][concurrent.futures.ThreadPoolExecutor] and
[`ProcessPoolExecutor`][concurrent.futures.ProcessPoolExecutor] to carry over the context.
And existing plugins exist to propagate the context with
[requests](https://pypi.org/project/opentelemetry-instrumentation-requests/) and
[httpx](https://pypi.org/project/opentelemetry-instrumentation-httpx/).
"""  # noqa: D205

from contextlib import contextmanager
from typing import Any, Iterator, Mapping

from opentelemetry import context, propagate

# anything that can be used to carry context, e.g. Headers or a dict
ContextCarrier = Mapping[str, Any]

__all__ = 'get_context', 'attach_context', 'ContextCarrier'


def get_context() -> ContextCarrier:
    """Create a new empty carrier dict and inject context into it.

    Returns:
        A new dict with the context injected into it.

    Usage:

    ```py
    from logfire.propagate import get_context, attach_context

    logfire_context = get_context()

    ...

    # later on in another thread, process or service
    with attach_context(logfire_context):
        ...
    ```

    You could also inject context into an existing mapping like headers with:

    ```py
    from logfire.propagate import get_context

    existing_headers = {'X-Foobar': 'baz'}
    existing_headers.update(get_context())
    ...
    ```
    """
    carrier: ContextCarrier = {}
    propagate.inject(carrier)
    return carrier


@contextmanager
def attach_context(carrier: ContextCarrier) -> Iterator[None]:
    """Attach a context as generated by [`get_context`][logfire.propagate.get_context] to the current execution context.

    Since `attach_context` is a context manager, it restores the previous context when exiting.
    """
    # capture the current context to restore it later
    old_context = context.get_current()
    new_context = propagate.extract(carrier=carrier)
    try:
        context.attach(new_context)
        yield
    finally:
        context.attach(old_context)