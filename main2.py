from opendssdirect import dss
import os



print('OpenDSSDirect.py and engine versions:', dss.Version())
print("\n")

# Define the path for the DSS file
dss_file = "./Project.dss"

# Create a blank file (you can start by writing initial configuration if needed)
with open(dss_file, 'w') as f:
    f.write("! This is a blank project file created using altdss\n")



dss.Command('Clear Redirect "{dss_file}" Set DefaultBaseFrequency=50')
print("Base Frequency changed to", "------TBC", "\n")

dss.Command(
    "New Circuit.{circuit_name} BasekV={base_kV}, pu={puV_source} Bus1={source_bus} mvasc3={mvasc3} mvasc1={mvasc1}".format(
        circuit_name='ActiveCircuit',
        base_kV=22,
        source_bus = "Bus1",
        puV_source = 1.01,
        mvasc3 = 500,
        mvasc1 = 500

    ))

dss.Command(
    "New Load.{test_load} phases=3 bus1={load_bus} kv={kV} kw={kW} pf={pf} model=5".format(
            test_load="Load1",
            load_bus="Bus1",
            kV=22,
            kW=120,
            pf=.8
        )
    )


dss.Solution.Solve()
print("List of buses here  -----\n",dss.Circuit.AllBusNames())
print("List of bus voltages here  -----\n",dss.Circuit.AllBusMagPu())



dss.Solution.Mode(12)
dss.Solution.Solve()
print("List of bus voltages here  -----\n",dss.Circuit.AllBusMagPu())
print(dss.Circuit.YCurrents())

#dss.Solution.Solve()
print(dss.Solution.CheckFaultStatus())
dss.Circuit.SetActiveBus('Bus1')
print("List of bus Short Circuit Currents here  -----\n",dss.Bus.Isc())
