from gym.envs.registration import register

register(
    id='xmz_env-v0',
    entry_point='xmz_env.envs:CdmEnv',
)