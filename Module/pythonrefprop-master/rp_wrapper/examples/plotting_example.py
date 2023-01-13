# -*- coding: utf-8 -*-
"""
Created on 01.08.2020

@author: Tim Bill

Description:
------------
Example script for plotting functions


Last Update:
------------
24.08.2020 Christoph Hoeges
    Tidy up implementation, check of functionality
"""
# ======================================================================================================================
#                                                    Imports
# ======================================================================================================================
from rp_wrapper import RefProp
from rp_wrapper.diagram_creator import create_diagram
from rp_wrapper.diagram_configurator import open_diag_configurator_window


# ======================================================================================================================
#                                                General function
# ======================================================================================================================
def example_call_diagram_creator():
    """ Example function to call plot creation with different settings.
    For further information see doc-string of package-function!

    Return:
    :return matplotlib.figure.Figure figure:
        instance of class FigureClass (pyplot package)
    """
    # Fluid name
    fluid_name = "Propane"
    # Diagram type
    selected_diag_type = "T-h"
    # Iso-lines in case some are wanted (in case of pressure: unit is bar)
    iso_input = []
    iso_offset = 200

    diag_settings = {"left_x_limit": 150, "right_x_limit": 800, "lower_y_limit": 240, "upper_y_limit": 400,
                     "scale_checkbox": False, "title_checkbox": False, "grid_checkbox": True, "resolution": 100,
                     "p_min": 0.5}

    gen_settings = {"selected_lan": "eng", "font_size": 12, "line_width": 2, "fig_height": 9, "fig_width": 12,
                    "marker_size": 5}

    # Get values for state point
    T_air_in = 2 + 273.15  # Evaporator secondary fluid temperature at inlet in K
    T_water_in = 60 + 273.15  # Condenser secondary fluid temperature at inlet in K
    dT_pinch = 2
    dT_sh = 5
    dT_sc = 5
    eta_is = 0.7
    rp = RefProp(fluid_name=fluid_name)
    state1_q1 = rp.calc_state("TQ", T_air_in - dT_pinch - dT_sh, 1.0)
    state1 = rp.calc_state("PT", state1_q1.p, state1_q1.T + dT_sh)
    state3_q0 = rp.calc_state("TQ", T_water_in + dT_pinch + dT_sc, 0.0)
    state2_q1 = rp.calc_state("PQ", state3_q0.p, 1.0)
    state3 = rp.calc_state("PT", state3_q0.p, state3_q0.T - dT_sc)
    state4 = rp.calc_state("PH", state1.p, state3.h)
    state2_s = rp.calc_state("PS", state3.p, state1.s)
    h2 = state1.h + (state2_s.h - state1.h)/eta_is
    state2 = rp.calc_state("PH", state3.p, h2)

    state_input = [(state1.T, state1.h/1000),
                   (state2.T, state2.h/1000),
                   (state2_q1.T, state2_q1.h / 1000),
                   (state3_q0.T, state3_q0.h / 1000),
                   (state3.T, state3.h/1000),
                   (state4.T, state4.h/1000),
                   (state1_q1.T, state1_q1.h/1000)]
    # frist state: T = 290K, s = 1.050 kJ/kgK
    # second state: T = 300, s = 1.128 kJ/kgK
    # third state: T = 300, s = 1.714 kJ/kgK

    fig = create_diagram(fluid_name,
                         selected_diag_type=selected_diag_type,
                         state_input=state_input,
                         iso_input=iso_input,
                         iso_offset=iso_offset,
                         diag_settings=diag_settings,
                         gen_settings=gen_settings,
                         saving_format="pdf")
    return fig


# ======================================================================================================================
#                                                      Main
# ======================================================================================================================
if __name__ == "__main__":
    # Choose mode
    # Here:
    #   - "gui": To use graphical user interface
    #   - "manual": To use code / functions (calls example function)
    mode = "manual"
    # Call functions
    if mode == "manual":
        figure = example_call_diagram_creator()
    elif mode == "gui":
        open_diag_configurator_window()
    else:
        print("Only two modes are possible - choose either 'manual' or 'gui'!")
