"""
@return : Returns the lift in SI units
@rtype : float
@param : 
	air_density - Density of air (kg/m^3) can be taken from measurements or 
	              based on the ISA table
	velocity - velocity of the aircraft (ft/s)
	wing_area - wing area of an aircraft (ft^2)
	coefficient_lift - coefficient of lift of aircraft.
"""
def calculate_lift(air_density, velocity, wing_area, coefficient_lift):
    lift = .5 * air_density * math.pow(velocity, 2) * wing_area * coefficient_lift
    return lift

"""
@return : Returns the drag in SI units
@rtype : float
@param : 
	air_density - Density of air (kg/m^3) can be taken from measurements or 
	              based on the ISA table
	velocity - velocity of the aircraft (ft/s)
	reference_area - reference area of an aircraft (ft^2). This area can be total 
	                 surface area, frontal area, or wing area. Drag will be the same, 
	                 but the coefficient of drag will be related by the ratio of the areas
	coefficient_lift - coefficient of lift of aircraft.
"""
def calculate_drag(air_density, velocity, reference_area, coefficient_drag):
	drag = .5 * air_density * math.pow(velocity, 2) * reference_area * coefficient_drag
	return drag

def get_isa_air_pressure():
	# TODO
	return

def mach_to_cas():
	# TODO
	return

def cas_to_mach():
	# TODO
	return

def calculate_crossover_altitude():
	# TODO
	return

