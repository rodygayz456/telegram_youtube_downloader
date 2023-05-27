import os


class ApiKeyUtils:
    TELEGRAM_BOT_ENVIRONMENT_NAME = "6127216105:AAF0Bk9BvcYsucb_XYqLd9M7X7RTpVTT9co"
    YOUTUBE_API_ENVIRONMENT_NAME = "AIzaSyD2eIQcS21Ex1o0GW8qup5jbk3AmuXXS4s"

    @staticmethod
    def get_telegram_bot_key():
        return os.environ.get(ApiKeyUtils.TELEGRAM_BOT_ENVIRONMENT_NAME, None)

    @staticmethod
    def get_youtube_api_key():
        return os.environ.get(ApiKeyUtils.YOUTUBE_API_ENVIRONMENT_NAME, None)
