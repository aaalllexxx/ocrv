from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from settings import env


class Log(ABC):
    format = "{prefix} {info} | {date} | user_id: {user_id}"


class LogType(Enum):
    file = 0
    console = 1


@dataclass
class LogInfo:
    info: str
    user_id: str


class FileLog(Log):
    def log(self, data: LogInfo, path, prefix="[#]"):
        with open(path, "a") as file:
            file.write(
                self.format.format(prefix=prefix,
                                   info=data.info,
                                   date=datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                                   user_id=data.user_id))
            file.write("\n")


class ConsoleLog(Log):
    @staticmethod
    def log(data: LogInfo, **kwargs):
        if env.debug:
            print(f"[{data.user_id}] | {data.info} | {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}", **kwargs)


class Debug:
    __log_functions = {
        "file": FileLog().log,
        "console": ConsoleLog().log
    }

    @classmethod
    def log(cls, info: LogInfo, log_type: LogType, *args):
        cls.__log_functions[log_type.name](info, *args)
