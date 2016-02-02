__author__ = 'or'


def with_alarm(f, signal, timeout):
    def decorator(*args, **kwargs):
        signal.setitimer(signal.ITIMER_REAL, timeout)
        result = f(*args, **kwargs)
        signal.setitimer(signal.ITIMER_REAL, 0)
        return result
    return decorator
