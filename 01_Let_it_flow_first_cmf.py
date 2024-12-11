import cmf

"""The project represents the study area and holds the cells (horizontal discretization of the soil), 
   the reaches (discretized river sections), "free" water storages (like lakes, dams etc.) 
   and the boundary conditions. While models for channeled flow may only contain reaches, 
   but no cells, every model spatial explicit description of subsurface flux needs to have cells."""
p = cmf.project()

# Create Water_storage 1 in project p
W1 = p.NewStorage(name='W1')      # (std::string       name,double x = 0,double y = 0,double z = 0 )
# Create Water_storage 2 in project p, without any volume as an initial state
W2 = p.NewStorage(name='W2')

# Create a linear storage equation from W1 to W2 with a residence time tr of one day
q = cmf.LinearStorageConnection(source=W1,target=W2,residencetime=1.0)
# Set the initial state of w1 to 1m³ of water.
W1.volume = 1.0

# Create an integrator (solver) for the ODE represented by project p,
# with an error tolerance of 1e-9
solver = cmf.RKFIntegrator(p, 1e-9)
# Import Python's datetime module
import datetime
# Set the intitial time of the solver
#solver.t = datetime.datetime(2012,1,1)
""" The code above is the setup part. Every cmf model consists of a setup part, 
    where the hydrological system is defined. For larger models, 
    Python's looping and conditional syntax and the possibility to read nearly any 
    data format can help to define the system from data."""

# Create a csv file on disk for output, and write column headers
# fout = open('firstmodel.csv','w')
# fout.write('time,w1.volume m3,w2.volume m3\n')
# # Run the model for 7 days, using a while loop
# while solver.t < datetime.datetime(2012,1,7):
#     # integrate the system for 1 h
#     solver.integrate_until(solver.t + datetime.timedelta(hours=1))
#     # write output (using the format operator %)
#     fout.write('{t},{w1:0.4f},{w2:0.4f}\n'.format(t=solver.t,w1=W1.volume,w2=W2.volume))
# fout.close()

""" Alternative run time loop for plotting !
    An alternative way to the run time code above is using list comprehension. 
    The result is then not written into a file, 
    but stored in memory using a list. This list can be plotted using the pylab-API of matplotlib. 
    The setup code is as before. """

# Iterate the solver hourly through the time range and return for each time step the volume in W1 and W2
result = [[W1.volume,W2.volume] for t in solver.run(datetime.datetime(2012,1,1),datetime.datetime(2012,1,7),datetime.timedelta(hours=1))]
import pylab as plt
plt.plot(result)
plt.xlabel('hours')
plt.ylabel('Volume in $m^3$')
plt.legend(('W1','W2'))
plt.show() # This line was missing in the Code






