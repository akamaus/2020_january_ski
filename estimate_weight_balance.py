#!/usr/bin/env python3

import planner.food as F
import planner.equipment as E
import planner.utils as U

from members import *

import products as P
food_table = F.food_planning(P.Food,
                             NBreakfast=P.NBreakfast,
                             NDinner=P.NDinner,
                             NLunch=P.NLunch,
                             NSnack=P.NSnack)

import stuff as S
stuff_table = E.equipment_planning(S.SharedEquipment); stuff_table

import numpy as np
avg_men_weight = np.mean([m.food_weight() + m.equipment_weight() for m in Members.values() if m.male])

U.print_overweight(Members, lambda m: m.food_weight() + m.equipment_weight(),
                   avg_men_weight,
                   WomanFoodWeightNorm + WomanSharedEquipWeightNorm );
