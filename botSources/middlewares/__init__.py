from ..namespace import dp
from .CallbackAnswerMiddleware import CallbackAnswerMiddleware

if (__name__ == "middlewares"):
    # Register your middlewares here:
    dp.middleware.setup(CallbackAnswerMiddleware)