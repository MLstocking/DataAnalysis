import configparser

class read_args:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('./model_settings.txt')
    
    def set_args(self):
        self.stock_code = [self.config['model settings']['stock_code']]
        self.rl_method = self.config['model settings']['rl_method']
        self.net = self.config['model settings']['net']
        self.num_steps = int(self.config['model settings']['num_steps'])
        self.lr = 0.01
        self.discount_factor =float(self.config['model settings']['discount_factor'])
        self.start_epsilon = 0
        self.balance = int(self.config['model settings']['balance'])
        self.num_epoches = 1
        self.delayed_reward_threshold = float(self.config['model settings']['delayed_reward_threshold'])
        self.backend = 'tensorflow'
        self.output_name = self.config['model settings']['output_name']
        self.value_network_name = self.config['model settings']['value_network_name']
        self.policy_network_name = self.config['model settings']['policy_network_name']
        self.reuse_models = True
        self.learning = False
        self.start_date = self.config['model settings']['start_date']