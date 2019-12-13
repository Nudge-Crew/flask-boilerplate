from functools import wraps
from flask_restful import reqparse


def param_parser(*arguments):
    # Forward params to wrapper function as named Parameters
    def parse(func):
        # Wrapper
        @wraps(func)
        def resource_verb(*args, **kwargs):
            parser = reqparse.RequestParser()
            for argument in arguments:
                parser.add_argument(argument)
            kwargs.update(parser.parse_args())
            return func(*args, **kwargs)

        return resource_verb

    return parse
