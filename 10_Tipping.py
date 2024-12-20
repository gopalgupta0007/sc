#make sure before running these code install these pages
# pip install scipy
# pip install packaging
# pip install networkx
# pip install matplotlib

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

quality=ctrl.Antecedent(np.arange(0,11,1),'quality') # create input variable neurons => antecedent
service=ctrl.Antecedent(np.arange(0,11,1),'service')
 
# quality = [0,1,2,3,4,5,6,7,8,9,10]   user can give qality in 0-10
# service = [0,1,2,3,4,5,6,7,8,9,10]   user can give service in 0-10
# depend on service and quality user can happy with our service so they give good tip

tip=ctrl.Consequent(np.arange(0,26,1),'tip')  # create output variable neurons => Consequent
# tip = [0,1,2,3,4,5,6,7,8,9,10]   user can give tip in 0-25


quality.automf(3)
quality.view()


service.automf(3) # automf => auto membership functions
service.view()

tip['low']=fuzz.trimf(tip.universe,[0,0,13])
tip['medium']=fuzz.trimf(tip.universe,[0,13,25])
tip['high']=fuzz.trimf(tip.universe,[13,25,25])
tip.view()

rule1=ctrl.Rule(quality['poor']|service['poor'], tip['low'])
rule2=ctrl.Rule(quality['average']|service['average'], tip['medium'])
rule3=ctrl.Rule(quality['good']|service['good'], tip['high'])

tipping_ctrl=ctrl.ControlSystem([rule1, rule2, rule3])
tipping_simulator=ctrl.ControlSystemSimulation(tipping_ctrl)

# i will give own value the qulity = 9.8 and service = 9.5 and system calculate the tip according to given my tip(output variable)
tipping_simulator.input['quality']=9.8
tipping_simulator.input['service']=9.5
tipping_simulator.compute()


tipping_simulator.output['tip']
print(tipping_simulator.output['tip'])
