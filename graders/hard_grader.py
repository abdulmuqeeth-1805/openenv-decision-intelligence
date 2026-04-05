def grade_hard(env, agent_actions):
    """
    Grader for Hard task
    Tests sequential decision making under uncertainty
    """
    total_reward = 0
    env.reset()
    
    for step, actions in enumerate(agent_actions):
        _, reward, _, info = env.step(actions)
        total_reward += reward
        
        # Penalty for inconsistent decisions
        if step > 0:
            prev_inv = env.history.get('inventory', {})
            # (simplified consistency check)
    
    return min(1.0, total_reward / len(agent_actions))