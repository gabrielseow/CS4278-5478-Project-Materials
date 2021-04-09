# Shows domain and dimensions of observation space and action space
# Code taken from Duckietown Github
import gym, gym_duckietown # registers the envs!
DUCKIETOWN = ['Duckietown-straight_road-v0','Duckietown-4way-v0','Duckietown-udem1-v0','Duckietown-small_loop-v0','Duckietown-small_loop_cw-v0','Duckietown-zigzag_dists-v0','Duckietown-loop_obstacles-v0','Duckietown-loop_pedestrians-v0']
for town in DUCKIETOWN:
  env = gym.make(town)
  print(town, env.observation_space, env.action_space)