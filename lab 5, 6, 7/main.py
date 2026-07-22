from simulation import Simulation

sim = Simulation(persons=10, media = 3, edges = 10)

sim.setup()

sim.print()
sim.run(10)
sim.print()