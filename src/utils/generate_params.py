class GenerateParams:
    def __init__(self, quote_list, range, interval, fundamental, dividends, modules, token):
        self.quote_list = quote_list
        self.range = range
        self.interval = interval
        self.fundamental = fundamental
        self.dividends = dividends
        self.modules = modules
        self.token = token

    def get_params(self):
        if self.fundamental or self.dividends:
            raise NotImplementedError
        elif self.modules != 'summaryProfile':
            raise NotImplementedError
        else:
            params = {
                'range': self.range,
                'interval': self.interval,
                'fundamental': self.fundamental,
                'dividends': self.dividends,
                'modules': self.modules,
                'token': self.token,
            }
            return params,
