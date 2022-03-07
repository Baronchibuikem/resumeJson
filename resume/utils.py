from django.db import connection, reset_queries
import time
import functools


def query_debugger(func):
    """For logging query counts of function"""

    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()
        start_queries = len(connection.queries)
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        end_queries = len(connection.queries)
        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        return result

    return inner_func


def generic_documents_directory(instance, filename) -> str:
    """Get generic document directory."""
    return f"uploads/documents/{str(instance.id)[-12:]}/{filename}"
