from typing import Any

from selenium.webdriver.common import service as service

class Service(service.Service):
    service_args: Any
    def __init__(
        self, executable_path, port: int = ..., service_args: Any | None = ..., log_path: Any | None = ..., env: Any | None = ...
    ) -> None: ...
    def command_line_args(self): ...
