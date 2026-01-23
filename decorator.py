import time


def debugFuncTime(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print(f"function execution time{start_time - end_time}")
        return result

    return wrapper


@debugFuncTime
def sleep_time(n):
    print("calculation pending")
    time.sleep(n)


# sleep_time(10)


# another example of decorator


validate_api_key = ["124", "013", "310"]


def require_pin(func):
    def wrapper(apiKey, *args):
        if apiKey in validate_api_key:
            print("authorize")
            return func(apiKey, *args)
        else:
            print("401 UnAuthorized")

    return wrapper


@require_pin
def enterPin(key):
    print(key)


# enterPin("00")


# -----------------


def cache(func):
    previous_cache = {}
    # print(previous_cache, "cache")

    def wrapper(*args):
        if args in previous_cache:
            print("cache se utha ke diya")
            return previous_cache[args]
        result = func(*args)
        previous_cache[args] = result
        return result

    return wrapper


@cache
def calculation(a, b):
    return a + b


print(calculation(1, 1))
print(calculation(1, 2))
print(calculation(1, 1))


def test(**kwargs):
    print(kwargs)

test(name="saad", age=12)
