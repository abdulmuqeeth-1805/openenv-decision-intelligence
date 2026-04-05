def grade_medium(env, agent_actions):
    """
    Grader for Medium task
    Checks multi-product decision quality
    """
    total_reward = 0
    env.reset()
    
    for actions in agent_actions:
        _, reward, _, info = env.step(actions)
        total_reward += reward
        
        # Bonus for balanced inventory
        inventory = env.state.get('inventory', {})
        if len(set(inventory.values())) < 3:  # Balanced
            total_reward += 0.05
    
    score = min(1.0, total_reward / len(agent_actions))
    return score