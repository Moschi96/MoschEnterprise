# -*- coding: utf-8 -*-
"""
Created on 01.08.2020

@author: Tim Bill

Description:
------------
Module contains functions to plot Ts, Th, logph diagrams for specific fluid

Last Update:
------------
24.08.2020 Christoph Hoeges
    Tidy up implementation, check of functionality

TODO:
- in GUI:
    - option to save or not + drop-down menu with all possible endings (instead of twice a tick-option)


- state_input: Values should be one list but:
    [(), (), ...] where each tuple is in shape of (x,y)
- saving options should not be 2 inputs but only one (dictionary would be better probably)
    - Two options within: Boolean (if saving should happen) + type (pdf, png, svg...)
"""


# ======================================================================================================================
#                                                     Imports
# ======================================================================================================================
from . import RefProp
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from labellines import labelLines  # labelLine,
import datetime


# ======================================================================================================================
#                                                   Information
# ======================================================================================================================
__version__ = "1.0"
__author__ = "Tim Bill"


# ======================================================================================================================
#                                                 Default values
# ======================================================================================================================
T_s_diag_default = {"scale_checkbox": True, "title_checkbox": True, "grid_checkbox": True, "resolution": 100,
                    "p_min": 0.5, "left_x_limit": 1, "right_x_limit": 2, "upper_y_limit": 265, "lower_y_limit": 350}
T_h_diag_default = {"scale_checkbox": True, "title_checkbox": True, "grid_checkbox": True, "resolution": 100,
                    "p_min": 0.5, "left_x_limit": 140, "right_x_limit": 450, "upper_y_limit": 230,
                    "lower_y_limit": 390}
logp_h_diag_default = {"scale_checkbox": True, "title_checkbox": True, "grid_checkbox": True, "resolution": 100,
                       "p_min": 0.5, "left_x_limit": 200, "right_x_limit": 500, "upper_y_limit": 100000,
                       "lower_y_limit": 5000000}
gen_settings_default = {"selected_lan": "eng", "font_size": 12, "line_width": 2, "fig_height": 16, "fig_width": 20,
                        "marker_size": 5}


# ======================================================================================================================
#                                              Language dictionary
# ======================================================================================================================
lan_dict = {"title_diag": {"eng": " diagram of ", "ger": "-Diagramm des Stoffes "},
            "x_T_s": {"eng": "Specific entropy in kJ/kgK", "ger": "Spezifische Entropie in kJ/kgK"},
            "y_T_s": {"eng": "Temperature in K", "ger": "Temperatur in K"},
            "x_T_h": {"eng": "Specific enthalpy in kJ/kg", "ger": "Spezifische Enthalpie in kJ/kg"},
            "y_T_h": {"eng": "Temperature in K", "ger": "Temperatur in K"},
            "x_log(p)_h": {"eng": "Specific enthalpy in kJ/kg", "ger": "Spezifische Enthalpie in kJ/kg"},
            "y_log(p)_h": {"eng": "Logarithmic pressure in bar", "ger": "Logarithmischer Druck in Bar"}}


# ======================================================================================================================
#                                                 Diagram creation
# ======================================================================================================================
def create_diagram(fluid_name="R134a", selected_diag_type="T-s", state_input=None, iso_input=None, iso_offset=300,
                   diag_settings=None, gen_settings=None, saving_format=None):
    """ creates diagram for chosen fluid and selected options/settings

    Parameters:
    :param string fluid_name:
        name of fluid
    :param string selected_diag_type:
        selected diagram type; can be "T-s", "h-s" or "log(p)-h"
    :param list state_input:
        list including all dots entered by the user
    :param list iso_input:
        list including all pressures/temperatures for isobars/isotherms entered by the user
    :param int iso_offset:
        describes range of iso lines
    :param dictionary diag_settings:
        dictionary including all diagram options/settings entered/selected by the user
            type:       key:
            float       left_x_limit
            float       right_x_limit
            float       upper_y_limit
            float       lower_y_limit
            boolean     scale_checkbox
            boolean     title_checkbox
            boolean     grid_checkbox
            int         resolution
            float       p_min
    :param dictionary gen_settings:
        dictionary including all general options/settings entered/selected by the user
            type:       key:
            string      selected_lan
            int         font_size
            int         line_width
            int         fig_height
            int         fig_width
            int         marker_size
    :param String saving_format:
        can be pdf, png or svg
    Return:
    :return matplotlib.figure.Figure figure:
        instance of class FigureClass (pyplot package)


    Example of calling function create_diagram:
    create_diagram("R134a",
                   "T-s",
                   [(290, 1.050), (300, 1.128), (300, 1.714)],
                   [10, 15],
                   200,
                   {"left_x_limit": 0.8, "right_x_limit": 2, "lower_y_limit": 240, "upper_y_limit": 380,
                    "scale_checkbox": True, "title_checkbox": True, "grid_checkbox": True, "resolution": 100,
                    "p_min": 0.5},
                   {"selected_lan": "eng", "font_size": 12, "line_width": 2, "fig_height": 16, "fig_width": 20,
                    "marker_size": 5},
                   True,
                   False)
    """

    # default settings
    diag_settings_default = T_s_diag_default
    if selected_diag_type == "T-h":
        diag_settings_default = T_h_diag_default
    elif selected_diag_type == "log(p)-h":
        diag_settings_default = logp_h_diag_default
    if not diag_settings:
        diag_settings = diag_settings_default
    else:
        for key in diag_settings_default:
            if key not in diag_settings:
                diag_settings[key] = diag_settings_default[key]

    if not gen_settings:
        gen_settings = gen_settings_default
    else:
        for key in gen_settings_default:
            if key not in gen_settings:
                gen_settings[key] = gen_settings_default[key]

    # REFPROP instance
    rp = RefProp(fluid_name, use_warnings=False, use_error_check=False)
    Tc, pc, dc = rp.get_crit_point()

    # vapor dome
    # dew: Taulinie (rechts)
    # boil: Siedelinie (links)
    # points to approximate vapor dome
    p_array = np.linspace(diag_settings["p_min"]*1e5, pc, diag_settings["resolution"])
    two_phase = {"dew": [], "boil": []}
    two_phase_T = {"dew": [], "boil": []}
    two_phase_s = {"dew": [], "boil": []}
    two_phase_h = {"dew": [], "boil": []}

    for p in p_array:
        two_phase["dew"].append(rp.calc_state("PQ", p, 1.0))
        two_phase["boil"].append(rp.calc_state("PQ", p, 0.0))
        two_phase_T["dew"].append(two_phase["dew"][-1].T)
        two_phase_T["boil"].append(two_phase["boil"][-1].T)
        two_phase_s["dew"].append(two_phase["dew"][-1].s/1000)
        two_phase_s["boil"].append(two_phase["boil"][-1].s/1000)
        two_phase_h["dew"].append(two_phase["dew"][-1].h/1000)
        two_phase_h["boil"].append(two_phase["boil"][-1].h/1000)

    figure = plt.figure(" ", figsize=(gen_settings["fig_width"]/2.54, gen_settings["fig_height"]/2.54),
                        linewidth=gen_settings["line_width"], facecolor=None)

    mpl.rcParams.update({"font.size": gen_settings["font_size"],
                         "lines.linewidth": gen_settings["line_width"],
                         "axes.linewidth": gen_settings["line_width"],
                         "lines.markersize": gen_settings["marker_size"]})

    # draw diagram
    if selected_diag_type == "T-s":
        # calculate states
        states = []
        for i in range(0, len(state_input)):
            states.append(rp.calc_state("TS", state_input[i][0], state_input[i][1] * 1000))
        if not state_input == []:
            if state_input[0]:
                states.append(rp.calc_state("TS", state_input[0][0], state_input[0][1] * 1000))

        states_data = [[], []]
        for state in states:
            states_data[0].append(state.s / 1000)
            states_data[1].append(state.T)
        # connect points to vapor dome
        plt.plot(two_phase_s["dew"], two_phase_T["dew"], "k")
        plt.plot(two_phase_s["boil"], two_phase_T["boil"], "k")
        # plot dots
        for i in range(0, len(states)):
            plt.plot(states_data[0][i], states_data[1][i], "ro")
        # connect dots
        plt.plot(states_data[0], states_data[1], "r")

        plt.xlabel(lan_dict["x_T_s"][gen_settings["selected_lan"]])
        plt.ylabel(lan_dict["y_T_s"][gen_settings["selected_lan"]])

        if diag_settings["title_checkbox"]:
            plt.title(selected_diag_type + lan_dict["title_diag"][gen_settings["selected_lan"]] + fluid_name)

    elif selected_diag_type == "T-h":
        # calculate states
        states = []
        for i in range(0, len(state_input)):
            states.append(rp.calc_state("TH", state_input[i][0], state_input[i][1] * 1000))
        if state_input[0]:
            states.append(rp.calc_state("TH", state_input[0][0], state_input[0][1] * 1000))

        states_data = [[], []]
        for state in states:
            states_data[0].append(state.h / 1000)
            states_data[1].append(state.T)
        # connect points to vapor dome
        plt.plot(two_phase_h["dew"], two_phase_T["dew"], "k")
        plt.plot(two_phase_h["boil"], two_phase_T["boil"], "k")
        # plot dots
        for i in range(0, len(states)):
            plt.plot(states_data[0][i], states_data[1][i], "ro")
        # connect dots
        plt.plot(states_data[0], states_data[1], "r")

        plt.xlabel(lan_dict["x_T_h"][gen_settings["selected_lan"]])
        plt.ylabel(lan_dict["y_T_h"][gen_settings["selected_lan"]])

        if diag_settings["title_checkbox"]:
            plt.title(selected_diag_type + lan_dict["title_diag"][gen_settings["selected_lan"]] + fluid_name)

    elif selected_diag_type == "log(p)-h":
        # calculate states
        states = []
        for i in range(0, len(state_input)):
            states.append(rp.calc_state("PH", state_input[i][0] * 1e5, state_input[i][1] * 1000))
        if state_input[0]:
            states.append(rp.calc_state("PH", state_input[0][0] * 1e5, state_input[0][1] * 1000))

        states_data = [[], []]
        for state in states:
            states_data[0].append(state.h / 1000)
            states_data[1].append(state.p / 1e5)
        # connect points to vapor dome
        plt.semilogy(two_phase_h["dew"], p_array / 1e5, "k")
        plt.semilogy(two_phase_h["boil"], p_array / 1e5, "k")
        # plot dots
        for i in range(0, len(states)):
            plt.semilogy(states_data[0][i], states_data[1][i], "ro")
        # connect dots
        plt.semilogy(states_data[0], states_data[1], "r")

        plt.xlabel(lan_dict["x_log(p)_h"][gen_settings["selected_lan"]])
        plt.ylabel(lan_dict["y_log(p)_h"][gen_settings["selected_lan"]])

        if diag_settings["title_checkbox"]:
            plt.title(selected_diag_type + lan_dict["title_diag"][gen_settings["selected_lan"]] + fluid_name)

    # draw isobars/isotherms
    xvals = []

    if selected_diag_type == "T-s":
        for p in iso_input:
            p = p * 1e5
            isobar_states = [[], []]

            state_q0 = rp.calc_state("PQ", p, 0.0)
            subcooled_s = int(state_q0.s)
            state_q1 = rp.calc_state("PQ", p, 1.0)
            overheated_s = int(state_q1.s)

            # subcooled region
            """ isobars in subcooled region nearly equivalent to vapor dome
            for s in range(subcooled_s - iso_offset, subcooled_s, 5):
                state_subcooled = rp.calc_state("PS", p, s)
                isobar_states[0].append(state_subcooled.s/1000)
                isobar_states[1].append(state_subcooled.T)
            """

            # vapor dome
            isobar_states[0].append(state_q0.s / 1000)
            isobar_states[1].append(state_q0.T)
            isobar_states[0].append(state_q1.s / 1000)
            isobar_states[1].append(state_q1.T)

            # overheated region
            for s in range(overheated_s, overheated_s + iso_offset, 5):
                state_subcooled = rp.calc_state("PS", p, s)
                isobar_states[0].append(state_subcooled.s / 1000)
                isobar_states[1].append(state_subcooled.T)

            # connect points to isobars
            plt.plot(isobar_states[0], isobar_states[1], "k", linewidth=gen_settings["line_width"],
                     label="" + str(p / 1e5) + " bar")

            xvals.append((subcooled_s / 1000 + overheated_s / 1000) / 2)

        labelLines(plt.gca().get_lines(), xvals=xvals, fontsize=int(gen_settings["font_size"] / 1.5))

    elif selected_diag_type == "T-h":
        for p in iso_input:
            p = p * 1e5
            isobar_states = [[], []]

            state_q0 = rp.calc_state("PQ", p, 0.0)
            subcooled_h = int(state_q0.h)
            state_q1 = rp.calc_state("PQ", p, 1.0)
            overheated_h = int(state_q1.h)

            # subcooled region
            """ isobars in subcooled region nearly equivalent to vapor dome
            for h in range(subcooled_h - iso_offset*300, subcooled_h, 500):
                state_subcooled = rp.calc_state("PH", p, h)
                isobar_states[0].append(state_subcooled.h/1000)
                isobar_states[1].append(state_subcooled.T)
            """

            # vapor dome
            isobar_states[0].append(state_q0.h / 1000)
            isobar_states[1].append(state_q0.T)
            isobar_states[0].append(state_q1.h / 1000)
            isobar_states[1].append(state_q1.T)

            # overheated region
            for h in range(overheated_h, overheated_h + iso_offset * 300, 500):
                state_subcooled = rp.calc_state("PH", p, h)
                isobar_states[0].append(state_subcooled.h / 1000)
                isobar_states[1].append(state_subcooled.T)

            # connect points to isobars
            plt.plot(isobar_states[0], isobar_states[1], "k", linewidth=gen_settings["line_width"],
                     label="" + str(p / 1e5) + " bar")

            xvals.append((subcooled_h / 1000 + overheated_h / 1000) / 2)

        labelLines(plt.gca().get_lines(), xvals=xvals, fontsize=int(gen_settings["font_size"] / 1.5))

    elif selected_diag_type == "log(p)-h":
        for T in iso_input:
            isotherm_states = [[], []]

            state_q0 = rp.calc_state("TQ", T, 0.0)
            subcooled_p = int(state_q0.p)
            state_q1 = rp.calc_state("TQ", T, 1.0)
            overheated_p = int(state_q1.p)

            # subcooled region
            for p in range(int((100000 * 300) * (1 / iso_offset)), subcooled_p, 1000):
                state_subcooled = rp.calc_state("PT", p, T)
                isotherm_states[0].append(state_subcooled.h / 1000)
                isotherm_states[1].append(state_subcooled.p / 1e5)

            # vapor dome
            isotherm_states[0].append(state_q0.h / 1000)
            isotherm_states[1].append(state_q0.p / 1e5)
            isotherm_states[0].append(state_q1.h / 1000)
            isotherm_states[1].append(state_q1.p / 1e5)

            # overheated region
            for p in range(overheated_p, overheated_p + iso_offset * 50000, 1000):
                state_subcooled = rp.calc_state("PT", p, T)
                isotherm_states[0].append(state_subcooled.h / 1000)
                isotherm_states[1].append(state_subcooled.p / 1e5)

            # connect points to isobars
            plt.semilogy(isotherm_states[0], isotherm_states[1], "k", linewidth=gen_settings["line_width"],
                         label="" + str(T) + " K")

            xvals.append((state_q0.h / 1000 + state_q1.h / 1000) / 2)

        labelLines(plt.gca().get_lines(), xvals=xvals, fontsize=int(gen_settings["font_size"] / 1.5))

    plt.grid(diag_settings["grid_checkbox"])
    if not diag_settings["scale_checkbox"]:
        plt.xlim([diag_settings["left_x_limit"], diag_settings["right_x_limit"]])
        plt.ylim([diag_settings["lower_y_limit"], diag_settings["upper_y_limit"]])
    plt.tight_layout()

    # save diagram
    current_time = datetime.datetime.now().strftime("%d_%m_%Y-%H_%M_%S")
    if saving_format:
        plt.savefig(selected_diag_type + "-diagram_" + fluid_name + "_" + current_time + "." + saving_format)

    plt.show()

    return figure
