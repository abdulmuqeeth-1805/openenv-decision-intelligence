from openenv_env.environment import DecisionIntelligenceEnv

print("Testing Easy Task...")
env = DecisionIntelligenceEnv(task_id="easy")
state = env.reset()
print(f"Initial state: {state}")

action = {"Product_A": 20}
next_state, reward, done, info = env.step(action)
print(f"Reward: {reward}")
print("✅ Environment is working!")