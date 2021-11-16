from gym.envs.registration import register

register(
    id='gwen-v0',
    entry_point='gym_gwen.envs:GwenEnv',
)