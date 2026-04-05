from typing import Dict, Any
import numpy as np

class DecisionIntelligenceEnv:
    """
    Decision Intelligence Environment for Supply Chain Management
    An AI agent learns to make optimal decisions under uncertainty
    """
    
    def __init__(self, task_id: str = "easy"):
        """
        Initialize the environment
        task_id: "easy", "medium", or "hard"
        """
        self.task_id = task_id
        self.step_count = 0
        self.max_steps = 10
        self.state = {}
        self.done = False
        self.reward = 0.0
        self.info = {}
        
        # Initialize based on difficulty
        self._setup_task()
    
    def _setup_task(self):
        """Setup different difficulty levels"""
        if self.task_id == "easy":
            # Single product, single decision
            self.products = ["Product_A"]
            self.inventory = {"Product_A": 100}
            self.demand_forecast = {"Product_A": 30}
            self.supplier_reliability = {"Product_A": 0.9}
            
        elif self.task_id == "medium":
            # Multiple products with constraints
            self.products = ["Product_A", "Product_B", "Product_C"]
            self.inventory = {"Product_A": 100, "Product_B": 50, "Product_C": 75}
            self.demand_forecast = {"Product_A": 30, "Product_B": 20, "Product_C": 25}
            self.supplier_reliability = {"Product_A": 0.9, "Product_B": 0.7, "Product_C": 0.8}
            
        else:  # hard
            # Sequential decisions with uncertainty
            self.products = ["Product_A", "Product_B", "Product_C", "Product_D"]
            self.inventory = {"Product_A": 100, "Product_B": 50, "Product_C": 75, "Product_D": 60}
            self.demand_forecast = {"Product_A": 30, "Product_B": 20, "Product_C": 25, "Product_D": 15}
            self.supplier_reliability = {"Product_A": 0.9, "Product_B": 0.7, "Product_C": 0.8, "Product_D": 0.6}
    
    def reset(self) -> Dict[str, Any]:
        """Reset the environment to initial state"""
        self.step_count = 0
        self.done = False
        self.reward = 0.0
        
        # Reset inventory
        if self.task_id == "easy":
            self.inventory = {"Product_A": 100}
        elif self.task_id == "medium":
            self.inventory = {"Product_A": 100, "Product_B": 50, "Product_C": 75}
        else:
            self.inventory = {"Product_A": 100, "Product_B": 50, "Product_C": 75, "Product_D": 60}
        
        self.state = {
            "inventory": self.inventory.copy(),
            "demand_forecast": self.demand_forecast.copy(),
            "supplier_reliability": self.supplier_reliability.copy(),
            "step": self.step_count,
            "task_difficulty": self.task_id
        }
        
        return self.state
    
    def step(self, action: Dict[str, int]) -> tuple:
        """
        Take an action in the environment
        action: {"Product_A": order_quantity, ...}
        Returns: (state, reward, done, info)
        """
        self.step_count += 1
        
        # Process orders
        order_cost = 0
        stockout_cost = 0
        holding_cost = 0
        
        for product in self.products:
            order_qty = action.get(product, 0)
            
            # Calculate costs
            order_cost += order_qty * 10
            
            # Simulate demand
            demand = self.demand_forecast[product]
            supplier_reliability = self.supplier_reliability[product]
            
            # Random actual demand with uncertainty
            actual_demand = int(demand * np.random.uniform(0.8, 1.2))
            
            # Update inventory after demand
            available = self.inventory[product]
            sold = min(available, actual_demand)
            self.inventory[product] = available - sold + int(order_qty * supplier_reliability)
            
            # Calculate costs
            stockout = max(0, actual_demand - available)
            stockout_cost += stockout * 50
            holding = self.inventory[product] * 2
            holding_cost += holding
        
        # Calculate reward (0.0 to 1.0 scale)
        total_cost = order_cost + stockout_cost + holding_cost
        base_cost = 500
        raw_reward = max(0, 1.0 - (total_cost / base_cost))
        self.reward = min(1.0, raw_reward)
        
        # Update state
        self.state = {
            "inventory": self.inventory.copy(),
            "demand_forecast": self.demand_forecast.copy(),
            "cost_breakdown": {
                "order_cost": order_cost,
                "stockout_cost": stockout_cost,
                "holding_cost": holding_cost,
                "total_cost": total_cost
            },
            "step": self.step_count,
            "task_difficulty": self.task_id
        }
        
        # Check if episode is done
        if self.step_count >= self.max_steps:
            self.done = True
        
        self.info = {"total_cost": total_cost}
        
        return self.state, self.reward, self.done, self.info
    
    def get_state(self) -> Dict[str, Any]:
        """Return current state"""
        return self.state