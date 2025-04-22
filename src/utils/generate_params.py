class GenerateParams:
    def __init__(self, days_range, interval, fundamental, dividends, modules, token):
        self.days_range = days_range
        self.interval = interval
        self.fundamental = fundamental
        self.dividends = dividends
        self.modules = modules
        self.token = token

    def get_params(self):
        if self.fundamental == 'true' or self.dividends == 'true':
            raise NotImplementedError
        elif self.modules != 'summaryProfile' or self.modules != 'list':
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

class ValidateParams:
    def __init__(self, params):
       self.params = params

    def validate(self):
        if self.params.get('fundamental') == 'true' or self.params.get('dividends') == 'true':
            raise NotImplementedError
        else:
            return self.params
