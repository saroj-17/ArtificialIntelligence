
'''
Lab 1 (Python): Reflex-based Intelligent Agent
Objective:
To design and implement reflex-based intelligent agents that make real-time decisions based on percepts from dynamic environments, such as traffic flow and presence detection.
To simulate environment-agent interaction using Python, demonstrating how agents can control systems like traffic signals and smart home lighting based on simple condition action rules.

'''
import random
import time
## === Agent 1: Traffic Light Controller ===

class TrifficEnvironment:
    #constructor
    def __init__(self):
        self.traffic_density = "High"
        self.light = "Red"
        self.timer = 0

    def get_percept(self):
        return self.traffic_density, self.timer, self.light


    def update_environment(self):
        self.traffic_density = random.choice(["High", "Low"])
        self.timer += 1
   
    def execute_action(self, action):
        if action == "SwitchToGreen":
            self.light = "Green"
            self.timer = 0
            print("Action Performed: Switched to Green -> GO ")
        elif action == "SwitchToRed":
            self.light = "Red"
            self.timer = 0
            print("Action Performed: Switched to Red ->  STOP ")
        else:
            self.light = "Yellow",
            print("Action performed: Switched to Yellow ->  Get Ready")

class TrafficLightAgent:
    def decide(self, trafficDensity, timer, currentLight):
        if currentLight == "Red" and trafficDensity == "High":
            return "SwitchToGreen"
        elif currentLight == "Green" and timer >=4:
            return "SwitchToRed"
        else:
            return "Yellow"
        
#smart light system 
class RoomEnvironment: 
    def __init__(self): 
        self.presence = "True"
        self.light = "ON"
        self.time = "Day"

    def get_percept(self): 
        return self.presence, self.light, self.time

    def update_environment(self): 
        self.presence = random.choice(["True", "false"])
        self.time = random.choice(["Day", "Night"])

    def execute_action(self, action): 
        if action == "TurnOn": 
            self.light ="ON"
            print("Action Performed: Light turned on ")
        elif action == "TurnOff": 
            self.light = "OFF"
            print("Action performedL:Light turned off")
        else: 
            print("NoAction")

class SmartLightAgent: 
    def decide(self, presence, timeOfDay, light):
        if presence == "True" and timeOfDay =="Night": 
            return "TurnOn"
        elif presence == "False" and timeOfDay == "Day": 
            return  "TurnOff"
        else: 
            print("NoOperation")

#simulation 

def simulate_traffic_agent(steps): 
    print("\n -- Traffic Light Simulation ---")
    env = TrifficEnvironment()
    agent = TrafficLightAgent()

    for step in range(steps): 
        print(f"Step {step+1}")
        env.update_environment()
        percepts = env.get_percept()
        print(f"Percepts:\n Traffic Density:{percepts[0]},Timer:{percepts[1]}, Light:{percepts[2]}")
        action = agent.decide(*percepts)
        env.execute_action(action)
        time.sleep(1)

def simulate_smart_light_agent(steps): 
    print("\n -- Smart Light Simulation ---")
    env = RoomEnvironment()
    agent = SmartLightAgent()

    for step in range(steps): 
        print(f"Step {step+1}")
        env.update_environment()
        percepts = env.get_percept()
        print(f"Percepts:\n Presence :{percepts[0]},Light:{percepts[1]}, Timer:{percepts[2]}")
        action = agent.decide(*percepts)
        env.execute_action(action)
        time.sleep(1)

#main 

if __name__ == "__main__":
    simulate_traffic_agent(steps=5)
    simulate_smart_light_agent(steps=5)




