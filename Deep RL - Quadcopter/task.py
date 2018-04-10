import numpy as np
from physics_sim import PhysicsSim

class Task():
    """Task (environment) that defines the goal and provides feedback to the agent."""
    def __init__(self, init_pose=None, init_velocities=None, 
        init_angle_velocities=None, runtime=5., target_pos=None):
        """Initialize a Task object.
        Params
        ======
            init_pose: initial position of the quadcopter in (x,y,z) dimensions and the Euler angles
            init_velocities: initial velocity of the quadcopter in (x,y,z) dimensions
            init_angle_velocities: initial radians/second for each of the three Euler angles
            runtime: time limit for each episode
            target_pos: target/goal (x,y,z) position for the agent
        """
        # Simulation
        self.sim = PhysicsSim(init_pose, init_velocities, init_angle_velocities, runtime) 
        self.action_repeat = 3

        self.state_size = self.action_repeat * 6
        self.action_low = 0
        self.action_high = 700
        self.action_size = 4
        
        self.runtime = runtime
        # Goal
        self.target_pos = target_pos if target_pos is not None else np.array([0., 0., 10.]) 

    def get_reward(self):
        """Uses current pose of sim to return reward."""
        #reward = 1.-.3*(abs(self.sim.pose[:3] - self.target_pos)).sum()
        #reward = 1. - 0.3*min(np.linalg.norm(self.sim.pose[2] - self.target_pos[2])**2, 10)
        alpha_x, alpha_y, alpha_z = 0.001, 0.001, 0.001
        alpha_xhat, alpha_yhat, alpha_zhat = 0.001, 0.001, 0.001
        
        dist = np.linalg.norm(self.sim.pose[:2] - self.target_pos[:2])
        velo = np.linalg.norm(self.sim.v[:2])
        
        # this worked 
        if (dist < 0.2) and (velo < 0.5):
            reward = 5.
        else:
            reward = -0.005*(min(dist, 3)**2)-0.001*(min(velo,2)**2)
        
        #reward = 3-0.05*(min(dist, 3)**2)-0.01*(min(velo,2)**2)
        #if (dist > 2.) or (velo > 3.):
        #    reward = -5.
        
        #reward = 5.-0.3*(dist**2)-0.3*(velo**2)
        #if (dist > 3) or (velo > 3):
        #    reward = -5.
        
        
        
        #reward = 3.0 - (4.0 * ((self.target_pos[2] - self.sim.pose[2])**2))
        #if self.sim.pose[2] > self.target_pos[2] + 4 or self.sim.pose[2] < self.target_pos[2] - 4:
        #    reward -= 600
        #if timestamp > self.runtime:  # agent has run out of time
        #    reward += 300  # extra reward
        
        
        #reward = max((1.-0.05*min(dist**2,5)), 0)
        
        #if (dist < 0.1) and (velo < 1):
        #    reward = 1.
        #else:
        #    reward = 1.-(2./25)*(min(dist, 5)**2)
        
        #reward = -min(abs(self.target_pos[2] - self.sim.pose[2]), 20.0)  
        #if self.sim.pose[2] >= self.target_pos[2]:  # agent has crossed the target height
        #    reward += 10.0  # bonus reward
            
        
        #dist_ind_x = min(1./abs(self.sim.pose[0] - self.target_pos[0]) , 100)
        #dist_ind_y = min(1./abs(self.sim.pose[1] - self.target_pos[1]) , 100)
        #dist_ind_z = min(1./abs(self.sim.pose[2] - self.target_pos[2]) , 100)
            
        #reward = -0.05 + 0.3*(dist_ind_x + dist_ind_y + dist_ind_z)
        #reward = 10.-(alpha_x*((self.sim.pose[0] - self.target_pos[0])**2) + \
            #             alpha_y*((self.sim.pose[0] - self.target_pos[0])**2) + \
            #             alpha_z*((self.sim.pose[2] - self.target_pos[2])**2) + \
            #            (alpha_xhat*(self.sim.v[0]**2) + alpha_yhat*(self.sim.v[1]**2) + alpha_zhat*(self.sim.v[2]**2)) )
            
                
        #reward = -(alpha_z*((self.sim.pose[2] - self.target_pos[2])**2)) + (alpha_zhat*(self.sim.v[2]**2))
        #reward = .7 -(alpha_z * min( (self.sim.pose[2] - self.target_pos[2])**2, 10)  ) 
        #dist = np.linalg.norm(self.sim.pose[:2] - self.target_pos[:2])
        #velo = np.linalg.norm(self.sim.v[:2])
        #alpha_dist, alpha_velo = 0.001, 0.002
        #reward = np.exp(-(alpha_dist*(dist) + alpha_velo*(velo))) 
        #reward = -min(abs(self.sim.pose[2]-self.target_pos[2]), 10.)
        #if self.sim.pose[2]>=self.target_pos[2]:
        #    reward += 5.
        
        #reward = 1.-.2*(abs(self.sim.pose[:3] - self.target_pos)).sum()
        
        # original submission that worked 
        return np.clip(reward,-5.,5.)/5
         
        
    def step(self, rotor_speeds):
        """Uses action to obtain next state, reward, done."""
        reward = 0
        pose_all = []
        for _ in range(self.action_repeat):
            done = self.sim.next_timestep(rotor_speeds) # update the sim pose and velocities
            reward += self.get_reward() 
            pose_all.append(self.sim.pose)
        next_state = np.concatenate(pose_all)
        return next_state, reward, done

    def reset(self):
        """Reset the sim to start a new episode."""
        self.sim.reset()
        state = np.concatenate([self.sim.pose] * self.action_repeat) 
        return state