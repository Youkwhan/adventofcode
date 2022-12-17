# 30 mins count down

#valves, flow rate (pressure per min), one minute to open/ one minute to follow a tunnel
# start at valve AA

#when we open a valve pressure = flow rate * minute remainding

# class Valve:
#    current_pressure = 0
#    total_pressure = 0
#    time = 0

#    def __init__(self, valve, flow_rate, tunnels) -> None:
#       self.valve = valve
#       self.flow_rate = flow_rate
#       self.neighboring_tunnels = tunnels # problem we only know the names..
from collections import defaultdict, deque

def get_non_zero_valves(valves: dict)-> set:
   non_zero_valves = {key for key, value in valves.items() if value[0] > 0}
   non_zero_valves.add("AA") #starting position
   return non_zero_valves

def get_shortest_paths(potential_valves: set, graph: dict)->dict:
   # The shortest path to walk(+1) to each tunnel
   shortest_path = defaultdict(dict)
   
   # need to find the shortest path from AA to any of the potential_valves
   # which also means the shortest path between potential_valves
   
   potential_valves_list = list(potential_valves)
   for i, start in enumerate(potential_valves_list):
      for end in potential_valves_list[i+1:]:
         # get the shortest path between two nodes
         path_cost = get_shortest_path(start, end, graph)

         # update distance to each path; key: "AA", value: {"BB":0, "CC":0}
         shortest_path[start][end] = path_cost
         shortest_path[end][start] = path_cost

   return shortest_path
      

def get_shortest_path(start, end, graph)->int:
   # BFS for the shortest path since, all paths costs the same 1 minute
   q = deque([(start, 0)])
   cost = defaultdict(lambda:float("inf"))

   while q:
      # pop the current node
      cur_tunnel, steps = q.popleft()

      # check whether we are at the target
      if cur_tunnel == end:
         break

      # check whether we have a higher cost of coming here
      if steps > cost[cur_tunnel]:
         continue # skip

      # go through all neighbors and append the target
      for neighbor in graph[cur_tunnel][1]:

         # compute the new cost (time)
         nsteps = steps + 1
         if nsteps < cost[neighbor]:
            #update the cost
            cost[neighbor] = nsteps
            
            # append to the queue
            q.append((neighbor, nsteps))
   #return the cost of traveling
   return cost[end]

def traverse_all_paths(shortest_path, valves, time_limit):
   paths = defaultdict(lambda:-1)

   #traverse our valves in bfs fashion
   # because we need to start from "AA" then walk outwards
   q = deque([("AA", 0, time_limit, set())])

   while q:
      # pop next closest tunnel
      cur_tunnel, accumulated_flow, time_limit, visited = q.popleft()

      # get our neighbours that we can reach in time
      neighbors = (neighbor for neighbor in shortest_path[cur_tunnel] if neighbor not in visited and shortest_path[cur_tunnel][neighbor] < time_limit )

      # update the maximum
      if paths[frozenset(visited)] < accumulated_flow:
         paths[frozenset(visited)] = accumulated_flow
      
      # append the neighbours
      for neighbor in neighbors:
         #get the flow
         new_flow = (time_limit-shortest_path[cur_tunnel][neighbor]-1) * valves[neighbor][0]

         #make a new set
         new_set = visited | {neighbor}
         q.append((neighbor, accumulated_flow + new_flow, time_limit - shortest_path[cur_tunnel][neighbor] -1, new_set))
      
      return paths

def part1(valves: dict):
   # potential valves we should visit
   non_zero_valves = get_non_zero_valves(valves) 
   # print(non_zero_valves)

   # get the shortest "tunnel" path between potential valves (we should go to)
   shortest_path = get_shortest_paths(non_zero_valves, valves)
   # print(shortest_path)

   # go through every possile tunnel path and find the their releasing pressure
   pressures = traverse_all_paths(shortest_path, valves, 30)
   # print(pressures)

   print(f"part1 maximum pressure we can release is {max(pressures.values())}")

def parse_data(data:str)->dict:
   valves = {}
   for line in data:
      line = line.strip().split()
      valve = line[1]
      flow_rate = line[4].split("=")[1][:-1]
      tunnels = "".join(line[9:]).split(",")
      
      valves[valve] = [int(flow_rate), tunnels]
   return valves

if __name__ == "__main__":
   with open("test.txt", "r") as data:
      data = data.read().split("\n")
      valves = parse_data(data)
      part1(valves)
