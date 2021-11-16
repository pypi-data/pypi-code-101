import numpy as np

from gym import error, spaces, utils
from gym.utils import seeding
import gym

import os
import pybullet as p
import pybullet_data
import math
import random

class GwenEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    def __init__(self):
       
         # graphical user interface (GUI) client mode 
        # if connect_mode == "GUI":
        self.step_counter = 0
        self.client = p.connect(p.GUI)

        # # direct link to physics engine
        # elif connect_mode  == "DIRECT":

        #     self.client = p.connect(p.DIRECT)
        
        # adjust physics engine parameters if necessary (refer to documentation) --> not done for ME5406 Project
        # p.setPhysicsEngineParameter()
        
        # set gravity as -9.81 ms^-2
        p.setGravity(0, 0, -9.81)

        # add additional data path to access urdf files from pybullet
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
 

        # add plane to world
        self.plane_id = p.loadURDF("plane.urdf", basePosition = [0, 0, 0])
            
        self.spiderbot_id = p.loadURDF("Spiderbot_URDFs/SpiderBot_4Legs/urdf/SpiderBot_4Legs.urdf", basePosition = [0, 0, 0.25])
        
        self.action_space = spaces.Box(np.array([-10]*8), np.array([10]*8))
        
        self.observation_space = spaces.Box(np.array([-10]*8), np.array([10]*8))
    

    def step(self, action):
        rev_joint_indices=[1,2,4,5,7,8,10,11]
        xposbefore = p.getBasePositionAndOrientation(self.spiderbot_id)
        dv=0.005
        dtheta = [ dv*a for a in action]
        currentPoses = [p.getLinkState(self.spiderbot_id, int(indice)) for indice in rev_joint_indices]
        newPose = [  currentPoses[i]+dtheta[i] for i in range(len(dtheta))]
        
        for index in range(len(rev_joint_indices)):
            p.setJointMotorControl2(self.spiderbot_id, rev_joint_indices[index], p.POSITION_CONTROL, targetPosition = newPose[index] )
        
        p.stepSimulation()
        xposafter = p.getBasePositionAndOrientation(self.spiderbot_id)
        forward_reward = (xposafter[0][0] - xposbefore[0][0]) / 0.2
        ctrl_cost = 0.5 * np.square(action).sum()
        survive_reward = 1.0
        reward = forward_reward - ctrl_cost  + survive_reward
        state_object, _ = p.getBasePositionAndOrientation(self.objectUid)
        



        if state_object[0]>1:
            reward = 1
            done = True
        else:
            reward = 0
            done = False

        self.step_counter += 1
        MAX_EPISODE_LEN =100
        if self.step_counter > MAX_EPISODE_LEN: ##
            reward = 0
            done = True

        info = {'object_position': state_object}
        self.observation = state_object
        return np.array(self.observation).astype(np.float32), reward, done, info

    def _get_obs(self):
        return np.concatenate(
            [
                self.sim.data.qpos.flat[2:],
                self.sim.data.qvel.flat,
                np.clip(self.sim.data.cfrc_ext, -1, 1).flat,
            ]
        )

    def reset(self):
        p.resetSimulation()
        p.configureDebugVisualizer(p.COV_ENABLE_RENDERING,0) # we will enable rendering after we loaded everything
        p.setGravity(0,0,-10)
        # urdfRootPath=pybullet_data.getDataPath()
        

        self.plane_id = p.loadURDF("plane.urdf", basePosition = [0, 0, 0])

   
        self.spiderbot_id = p.loadURDF("Spiderbot_URDFs/SpiderBot_4Legs/urdf/SpiderBot_4Legs.urdf", basePosition = [0, 0, 0.25])
       

        state_robot = p.getBasePositionAndOrientation(self.spiderbot_id)
        observation = state_robot[0] 
        p.configureDebugVisualizer(p.COV_ENABLE_RENDERING,1) # rendering's back on again
        return observation

    def render(self, mode='human'):
        view_matrix = p.computeViewMatrixFromYawPitchRoll(cameraTargetPosition=[0.7,0,0.05],
                                                            distance=.7,
                                                            yaw=90,
                                                            pitch=-70,
                                                            roll=0,
                                                            upAxisIndex=2)
        proj_matrix = p.computeProjectionMatrixFOV(fov=60,
                                                     aspect=float(960) /720,
                                                     nearVal=0.1,
                                                     farVal=100.0)
        (_, _, px, _, _) = p.getCameraImage(width=960,
                                              height=720,
                                              viewMatrix=view_matrix,
                                              projectionMatrix=proj_matrix,
                                              renderer=p.ER_BULLET_HARDWARE_OPENGL)

        rgb_array = np.array(px, dtype=np.uint8)
        rgb_array = np.reshape(rgb_array, (720,960, 4))

        rgb_array = rgb_array[:, :, :3]
        return rgb_array

    def _get_state(self):
        return self.observation

    def close(self):
        p.disconnect()
