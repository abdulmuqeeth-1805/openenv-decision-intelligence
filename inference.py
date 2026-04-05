import sys
import json
from openenv_env.environment import DecisionIntelligenceEnv

def main():
    task_id = sys.argv[1] if len(sys.argv) > 1 else "easy"
    
    print("[START]")
    
    env = DecisionIntelligenceEnv(task_id=task_id)
    state = env.reset()
    
    print(f'[STEP] observation: {json.dumps(state)}')
    
    # Simple baseline agent: order 20% of forecast
    action = {}
    for product in env.products:
        action[product] = int(env.demand_forecast[product] * 0.2)
    
    print(f'[STEP] action: {json.dumps(action)}')
    
    next_state, reward, done, info = env.step(action)
    
    print(f'[STEP] reward: {reward}')
    print(f'[STEP] done: {done}')
    print("[END]")
    
    print(f"Score: {reward}")

if __name__ == "__main__":
    main()