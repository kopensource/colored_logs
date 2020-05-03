class IconSet:
    def __init__(
        self,
        info: str = 'ℹ',
        success: str = '✔',
        fail: str = '✘',
        warning: str = '!',
        error: str = '☠',
        critical: str = '☠',
        process: str = '⧗',
        time: str = '◴'
    ):
        self.info = info
        self.success = success
        self.fail = fail
        self.warning = warning
        self.error = error
        self.critical = critical
        self.process = process
        self.time = time