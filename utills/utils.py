# CONSTANTS
import inspect

URL = "https://opensource-demo.orangehrmlive.com/"
USERNAME = "Admin"
PASSWORD = "admin123"


def _get_function_name():
    return inspect.stack()[1][3]
