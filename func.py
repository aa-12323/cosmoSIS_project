import matplotlib as plt
import numpy as np

output = ""

def plot_distance(d="None"):
    
    z = self.load_file("distances", "z")
    d = self.load_file("distances", self.distance)
    pylab.plot(z, d*self.scaling)
    pylab.grid()
    pylab.xlabel("Redshift z")
    pylab.ylabel(self.name)