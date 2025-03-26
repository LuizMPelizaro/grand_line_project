class GenerateParams:
    def __init__(self, quote_list, days_range, interval, fundamental, dividends, modules, token):
        self.quote_list = quote_list
        self.days_range = days_range
        self.interval = interval
        self.fundamental = fundamental
        self.dividends = dividends
        self.modules = modules
        self.token = token

    def get_params(self):
        if self.fundamental == 'true' or self.dividends == 'true':
            raise NotImplementedError
        elif self.modules != 'summaryProfile':
            raise NotImplementedError
        else:
            params = {
                'range': self.days_range,
                'interval': self.interval,
                'fundamental': self.fundamental,
                'dividends': self.dividends,
                'modules': self.modules,
                'token': self.token,
            }
            return params
