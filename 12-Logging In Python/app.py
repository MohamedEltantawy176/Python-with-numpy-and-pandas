import logging

## logging settings
logging.basicConfig(
        level = logging.DEBUG,
        format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler("app1.log"),
            logging.StreamHandler()
        ]
)

logger= logging.getLogger("ArtimetjicApp")

def add(a,b):
    logger.debug("Adding result: %s", a + b)
    return a + b

def subtract(a,b):
    logger.debug("Subtracting result: %s", a - b)
    return a - b

def multiply(a,b):
    logger.debug("Multiplying result: %s", a * b)
    return a * b

def divide(a,b):
    try:
        result = a / b
        logger.debug("Dividing result: %s", a / b)
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    



add(10,15)
subtract(15,10)
multiply(15,10)
divide(15,5)