def grade_easy(env, agent_actions):
    """
    Grader for Easy task
    Returns score between 0.0 and 1.0
    """
    total_reward = 0
    env.reset()
    
    for action in agent_actions:
        _, reward, _, _ = env.step(action)
        total_reward += reward
    
    avg_reward = total_reward / len(agent_actions)
    return min(1.0, avg_reward)