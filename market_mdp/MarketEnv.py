import numpy as np

class MarketEnv():

    def __init__(self):
        self.max_inventory = 2500
        self.state_env_dim = 2
        
        self.inventory = self.max_inventory
        self.action_space = np.arange(0, 101)
        self.action_env_dim = len(self.action_space)

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
    
    def get_random_price():
        return np.random.uniform(0, 100)
        
    # .step(action)
    def step(self, action_index):
        previous_ref_price = self.current_state[1]
        demand_lambda = 50 - 0.5* previous_ref_price
        demand = np.floor(np.random.poisson(demand_lambda))
        set_price = self.action_space[action_index]

        reward = ((previous_ref_price + set_price)/2) * demand
        self.current_state[0] = self.current_state[0] - demand

        inventory = self.current_state[0] 
        next_state = np.array([inventory , set_price])
        
        return next_state, reward, inventory  > 0, dict()


