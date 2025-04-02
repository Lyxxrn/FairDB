from functools import wraps
from django.db import connection, reset_queries
import time

def sql_debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        reset_queries()
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print("\n" + "=" * 80)
        print(f"Funktion: {func.__name__}")
        print(f"Anzahl Queries: {len(connection.queries)}")
        print(f"Dauer: {(end - start):.4f}s")
        print("-" * 80)

        for i, query in enumerate(connection.queries):
            print(f"SQL {i+1}: {query['sql']}")
            print(f"Zeit: {float(query['time']):.4f}s")
            print("-" * 60)

        print("=" * 80 + "\n")
        return result
    return wrapper

class SQLDebugMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return sql_debug(view)