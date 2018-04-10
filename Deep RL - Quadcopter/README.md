# Deep RL Quadcopter Controller

*Teach a Quadcopter How to Fly!*

This project is a reinforcement learning exercise that was the final part of the udacity deep learning course. In this project, the aim was to design an agent to fly a quadcopter, and then train it using a reinforcement learning algorithm. This algorithm was a Deep Deterministic Policy Gradient (DDPG) algorithm, most of which was given as a template. The exercise was to design a task and make the agent learn this task. The choice of the task was hovering. 

## Project Instructions

1. Clone the repository and navigate to the downloaded folder.

```
git clone "https://github.com/semiGr/dl-projects/Deep RL - Quadcopter.git"
cd "Deep RL - Quadcopter"
```

2. Create and activate a new environment.

```
conda create -n quadcop python=3.6 matplotlib numpy pandas
source activate quadcop
```
4. Once you activated the environment, install the required packages using requirements.txt file. For this step you will need tensorflow installed, which can be obtained using conda. 

```
pip install -r requirements.txt
```

3. Create an [IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html) for the `quadcop` environment. 
```
python -m ipykernel install --user --name quadcop --display-name "quadcop"
```

4. Open the notebook.
```
jupyter notebook Quadcopter_Project.ipynb
```

5. Before running code, change the kernel to match the `quadcop` environment by using the drop-down menu (**Kernel > Change kernel > quadcop**). Then, follow the instructions in the notebook.

6. You will likely need to install more pip packages to complete this project.  Please curate the list of packages needed to run your project in the `requirements.txt` file in the repository.
