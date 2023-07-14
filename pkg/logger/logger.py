import loguru
from pkg.logger.iLogger import ILogger


class Logger(ILogger):
    def info(self, msg, *args, **kwargs):
        loguru.logger.info(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        loguru.logger.error(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        loguru.logger.warning(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        loguru.logger.debug(msg, *args, **kwargs)
