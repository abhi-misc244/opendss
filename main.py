import altdss as dss
import os



# Define the path for the DSS file
dss_file = "./Project.dss"

# Create a blank file (you can start by writing initial configuration if needed)
with open(dss_file, 'w') as f:
    f.write("! This is a blank project file created using altdss\n")

# Now, let's create the components and add them to the DSS file




circuit = dss.altdss(f'''
    Clear
    Redirect "{dss_file}"
''')
 
print(circuit)
print(len(dss.altdss.Bus))
bus1 = dss.altdss.Bus
bus1.Name = 'Bus No 1'
bus1.Base = '22 kV'

dss.CircuitModel.

bus2 = dss.altdss.Bus
bus2.Name = 'Bus No 2'
bus2.Base = '0.415 kV'


bus3 = dss.altdss.Bus
bus3.Name = 'Bus No 3'
bus3.Base = '0.415 kV'

grid = dss.altdss.Vsource
grid.BasekV = 22 #kV
grid.BaseMVA = 100 #MVA
grid.Bus1 = bus1


print(bus3.Base)


bus4 = circuit.

gen = dss.altdss.Generator
gen.BaseFreq = 50
gen.Bus1 = bus1

# Add buses to the network (you might need to manually keep track of the buses, as no "project" is being used)
# There's no specific project container; instead, buses, transformers, etc., are treated as independent components

# Add grid on Bus 1
#grid = dss.altdss.Source(name="Grid", bus1="Bus1", base_voltage=120, voltage=120, angle=0)
#grid.add()

# Add transformer between Bus1 and Bus2
transformer = dss.Transformer(name="Transformer1", bus1="Bus1", bus2="Bus2", kVA=500, X=0.1, R=0.05)
transformer.add()

# Add a line between Bus2 and Bus3
line = dss.Line(name="Line1", bus1="Bus2", bus2="Bus3", length=1.0, r=0.05, x=0.1)
line.add()

# Add load on Bus 3
load = dss.Load(name="Load1", bus1="Bus3", p=100, q=50)
load.add()

# Now the components are added; you can now run a simulation if applicable
# For example, solve or analyze the system, depending on the features of the `altdss` package.
