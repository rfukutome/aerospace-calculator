import math
import engineering_constants as constants

def analyze_aircraft(coefficient_lift, coefficient_drag, wing_area, wing_span, weight):
    #TODO
    return

"""
@return : Returns the lift in SI units
@rtype : float
@param :
    air_density - Density of air (kg/m^3) can be taken from measurements or
                  based on the ISA table
    velocity - velocity of the aircraft (m/s)
    wing_area - wing area of an aircraft (m^2)
    coefficient_lift - coefficient of lift of aircraft.

Mathematical Function: L = 1/2 * rho * V^2 * A * Cl
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
    velocity - velocity of the aircraft (m/s)
    reference_area - reference area of an aircraft (m^2). This area can be total 
                     surface area, frontal area, or wing area. Drag will be the same, 
                     but the coefficient of drag will be related by the ratio of the areas
    coefficient_lift - coefficient of lift of aircraft.

Mathematical Function: D = 1/2 * rho * V^2 * A * Cd
"""
def calculate_drag(air_density, velocity, reference_area, coefficient_drag):
    drag = .5 * air_density * math.pow(velocity, 2) * reference_area * coefficient_drag
    return drag

"""
@return : Returns the induced drag of an aircraft which is the drag associated with the
          production of lift
@rtype : float
@param :
    induced_drag_correction_factor (k) - induced drag correction factor
    coefficient_lift - coefficient of lift of aircraft.

Mathematical Function: Cdi = kCl^2
"""
def calculate_induced_drag(induced_drag_correction_factor, coefficient_lift):
    Cdi = induced_drag_correction_factor * math.pow(coefficient_lift, 2)
    return Cdi

"""
@return : Returns the wing aspect ratio
@rtype : float
@param :
    wing_span - The distance from one tip of the wing to the other in meters
    wing_area - The wing area

Mathematical Function: AR = (b^2)/S
"""
def calculate_aspect_ratio(wing_span, wing_area):
    AR = math.pow(wing_span, 2)/wing_area
    return AR

"""
@return : Returns the oswald efficiency for a swept wing
@rtype : float
@param :
    aspect_ratio - Aspect ratio of the aircraft
    leading_edge_sweep_angle - The angle of the wing sweep measured in degrees 
                               from the aircrafts y axis.
@note : Valid for aspect ratios of 6 or more

Mathematical Function: e = 4.61(1-0.045 * AR^0.068)(cos(LE_angle))^0.15 - 3.1
"""
def calculate_oswald_efficiency_swept_wing(aspect_ratio, leading_edge_sweep_angle):
    e = 4.61 * (1 - 0.045 * math.pow(aspect_ratio, 0.68)) * math.pow(math.cos(leading_edge_sweep_angle), 0.15) - 3.1
    return e

"""
@return : Returns the oswald efficiency for a rectangular wing (no sweep)
@rtype : float
@param :
    aspect_ratio - Aspect ratio of the aircraft

@notes : Valid for aspect ratios of 6 or more

Mathematical Function: e = 1.78(1-0.045 * AR^0.068) - 0.64
"""
def calculate_oswald_efficiency_rectangular_wing(aspect_ratio):
    e = 1.78 * (1 - 0.045 * math.pow(aspect_ratio, 0.68)) - 0.64
    return e

"""
@return : Returns the reynolds number of a component (fuselage, wing, tail)
@rtype : float
@param :
    air_density - density of air
    true_airspeed - airspeed
    length - length of component in direction of flight
    air_viscosity - viscosity of air

Mathematical Function: Re = rho * V * L / mu
"""
def calculate_reynolds_number(air_density, true_airspeed, length, air_viscosity):
    Re = air_density * true_airspeed * length / air_viscosity
    return Re

def calculate_induced_drag_correction_factor(aspect_ratio):
    k = 1/(constants.PI * constants.e * aspect_ratio)
    return k

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
