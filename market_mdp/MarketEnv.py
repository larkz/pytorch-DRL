import numpy as np

class MarketEnv():

    def __init__(self):
        self.max_inventory = 100
        self.state_env_dim = 2
        self.action_env_dim = 1
        self.inventory = self.max_inventory

        random_price = np.random.uniform(0, 100)
        self.current_state = np.array([self.inventory, random_price])

    # .seed
    def seed(self, seed):
        return None
    
    # .action_space

    # .reset()
    def reset(self):
        random_ref_price = np.random.uniform(0, 100)
        self.inventory = self.max_inventory
        return np.array([self.inventory, random_ref_price])
    
    # .step(action)
    def step(self, action):
        previous_ref_price = self.current_state[1]
        demand_lambda = 50 - 0.5* previous_ref_price
        demand = np.floor(np.random.poisson(demand_lambda))
        reward = ((previous_ref_price + action)/2) * demand
        self.inventory -= 1
        next_state = np.array([self.inventory, action])
        
        return next_state, reward, self.inventory > 0, dict()


