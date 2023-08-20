def decorator_logging_factory(logger):
    def decorator_logging(func):
        def wrapper(*args, **kwargs):
            logger.info("%s %s", str(func.__name__), "start")
            ans = func(*args, **kwargs)
            logger.info("%s %s", str(func.__name__), "successfully finished")
            return ans

        return wrapper

    return decorator_logging


def decorator_logging_factory_class(logger):
    def decorator_logging(func):
        def wrapper(self, *args, **kwargs):
            logger.info(
                "%s.%s %s",
                str(type(self)),
                str(func.__name__),
                "start",
            )
            ans = func(self, *args, **kwargs)
            logger.info(
                "%s.%s %s",
                str(type(self)),
                str(func.__name__),
                "successfully finished",
            )
            return ans

        return wrapper

    return decorator_logging


def decorator_logging_factory_async(logger):
    def decorator_logging(func):
        async def wrapper(*args, **kwargs):
            logger.info("%s %s", str(func.__name__), "start")
            ans = await func(*args, **kwargs)
            logger.info("%s %s", str(func.__name__), "successfully finished")
            return ans

        return wrapper

    return decorator_logging


def decorator_logging_factory_class_async(logger):
    def decorator_logging(func):
        async def wrapper(self, *args, **kwargs):
            logger.info(
                "%s.%s %s",
                str(type(self)),
                str(func.__name__),
                "start",
            )
            ans = await func(self, *args, **kwargs)
            logger.info(
                "%s.%s %s",
                str(type(self)),
                str(func.__name__),
                "successfully finished",
            )
            return ans

        return wrapper

    return decorator_logging
