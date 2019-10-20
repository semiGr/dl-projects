# dl-projects
deep learning repo

# updates - 27 Jan 2019 
- added a "deep-optimal-stopping" folder, where two main notebooks are found;
- "AmericanOption" - presents an implementation for a deep learning solver for optimal stopping 
  problems; in this case it is presented in a toy example;
- "American-option-tf-estimator" presents the same problem, but in a tensorflow estimator implementation.
  This part is still work in progress...
  
# updates - 6 May 2019
- added the python notebook of the dog classifier project as part of the Udacity projects. Note that
  it is only part of the project, as the data files required for the actual are too big to upload.

# updates - 7 Oct 2019
- added an updated version of the optimal stopping solver. the new code presents the same "dice" problem, but for general time steps. Further extension that allows for general "payoffs" will follow. (currently this payoff is the identity.)
- as a next step, the solver will be compared to more standard MC methods in terms of efficieny. this is currently work in progress.

# updates - 21 Oct 2019
- added an upgraded version of the deep optimal stopping solver. the new notebook contains two improvments: 1) implementation of generic payoff function; 2) improved learning rate settings that allows for more consistent training results.
- the file also contains conculding remarks and potential directions for future work.
