from gym.envs.registration import register

register(
    id='abEnv-v0',
    entry_point='custom_gym.envs:Acrobot2Env',
)

register(
    id='mcEnv-v0',
    entry_point='custom_gym.envs:MountainCar2Env',
)