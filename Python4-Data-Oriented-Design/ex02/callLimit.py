def callLimit(limit: int):
    """Takes an int as a limit to how many times a function can be called."""

    count = 0

    def callLimiter(function):
        """Wraps a function, limits the number of times it can be executed."""

        def limit_function(*args: any, **kwds: any):
            """Increments count and checks it against the limit.
               Execute function if count is still within limits."""

            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: {function} call too many times")
                return None

            function(*args, **kwds)
            return None

        return limit_function

    return callLimiter
