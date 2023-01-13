# ======================================================================================================================
#                                                    Imports
# ======================================================================================================================
import PySimpleGUI as sg
from .diagram_creator import create_diagram


# ======================================================================================================================
#                                                   Information
# ======================================================================================================================
__version__ = "1.0"
__author__ = "Tim Bill"


# ======================================================================================================================
#                                              Language dictionary
# ======================================================================================================================
lan_dict = {"diag_tab": {"eng": "Diagram type", "ger": "Diagrammtyp"},
            "state_tab": {"eng": "State input", "ger": "Eingabe Zustände"},
            "diag_settings_tab": {"eng": "Diagram settings", "ger": "Diagramm-Einstellungen"},
            "gen_settings_tab": {"eng": "General settings", "ger": "Allgemeine Einstellungen"},

            "fluid_name_text1": {"eng": "Fluid selection:", "ger": "Fluidauswahl:"},
            "fluid_name_text2": {"eng": "Manual input:", "ger": "Manuelle Eingabe:"},
            "T_s_radio_text": {"eng": "T-s diagram", "ger": "T-s-Diagramm"},
            "T_h_radio_text": {"eng": "T-h diagram", "ger": "T-h-Diagramm"},
            "log(p)_h_radio_text": {"eng": "log(p)-h diagram", "ger": "log(p)-h-Diagramm"},
            "saving_format_text": {"eng": "Saving format:", "ger": "Speicherformat:"},
            "create_diag_button": {"eng": "Create diagram", "ger": "Diagramm erstellen"},

            "state_text": {"T-s": {"eng": "Selected diagram type: T-s diagram"
                                          "\n\nPlease input states like this: (T1, s1), (T2, s2), ..."
                                          "\nTemperature T in K, Specific entropy s in kJ/kgK",
                                   "ger": "Ausgewählter Diagrammtyp: T-s-Diagramm"
                                          "\n\nBitte Zustände wie folgt eingeben: (T1, s1), (T2, s2), ..."
                                          "\nTemperatur T in K, Spezifische Entropie s in kJ/kgK"},
                           "T-h": {"eng": "Selected diagram type: T-h diagram"
                                          "\n\nPlease input states like this: (T1, h1), (T2, h2), ..."
                                          "\nTemperature T in K, Specific enthalpy h in kJ/kg",
                                   "ger": "Ausgewählter Diagrammtyp: T-h-Diagramm"
                                          "\n\nBitte Zustände wie folgt eingeben: (T1, h1), (T2, h2), ..."
                                          "\nTemperatur T in K, Spezifische Enthalpie h in kJ/kg"},
                           "log(p)-h": {"eng": "Selected diagram type: log(p)-h diagram"
                                               "\n\nPlease input states like this: (p1, h1), (p2, h2), ..."
                                               "\nPressure p in bar, Specific enthalpy h in kJ/kg",
                                        "ger": "Ausgewählter Diagrammtyp: log(p)-h diagram"
                                               "\n\nBitte Zustände wie folgt eingeben: (p1, h1), (p2, h2), ..."
                                               "\nDruck p in bar, Spezifische Enthalpie h in kJ/kg"}
                           },
            "iso_text": {"T-s": {"eng": "Please input isobars like this: p1, p2, ..."
                                        "\nPressure p in bar",
                                 "ger": "Bitte Isobaren wie folgt eingeben: p1, p2, ..."
                                        "\nDruck p in bar"},
                         "T-h": {"eng": "Please input isobars like this: p1, p2, ..."
                                        "\nPressure p in bar",
                                 "ger": "Bitte Isobaren wie folgt eingeben: p1, p2, ..."
                                        "\nDruck p in bar"},
                         "log(p)-h": {"eng": "Please input isotherms like this: T1, T2, ..."
                                             "\nTemperature T in K",
                                      "ger": "Bitte Isothermen wie folgt eingeben: T1, T2, ..."
                                             "\nTemperatur T in K"}
                         },
            "offset_text": {"eng": "\n\nIsoline offset:", "ger": "\n\nIsolinien-Versatz:"},

            "diag_text": {"eng": "Diagram                (limits only effective if automatic scale not active)",
                          "ger": "Diagramm             (Limits nur wirksam, wenn automatische Skalierung nicht aktiv)"},
            "left_x_limit_text": {"eng": "Left x limit:", "ger": "Linkes x-Limit:"},
            "right_x_limit_text": {"eng": "Right x limit:", "ger": "Rechtes x-Limit:"},
            "lower_y_limit_text": {"eng": "Lower y limit:", "ger": "Unteres y-Limit:"},
            "upper_y_limit_text": {"eng": "Upper y limit:", "ger": "Oberes y-Limit:"},
            "scale_checkbox_text": {"eng": "Scale diagram automatically",
                                    "ger": "Diagramm automatisch skalieren"},
            "title_checkbox_text": {"eng": "Show title", "ger": "Titel anzeigen"},
            "grid_checkbox_text": {"eng": "Activate grid", "ger": "Gitternetz aktivieren"},
            "vapor_dome_text": {"eng": "Vapor dome", "ger": "Dampfglocke"},
            "resolution_text": {"eng": "Resolution:", "ger": "Auflösung:"},
            "p_min_text": {"eng": "p_min:", "ger": "p_min:"},

            "lan_text": {"eng": "Language", "ger": "Sprache"},
            "eng_radio_text": {"eng": "English", "ger": "Englisch"},
            "ger_radio_text": {"eng": "German", "ger": "Deutsch"},
            "font_size_settings_text": {"eng": "Font and size settings",
                                        "ger": "Schriftgröße-/art,""Linien-/Markereinstellungen"},
            "font_size_text": {"eng": "Font size:", "ger": "Schriftgröße:"},
            "line_width_text": {"eng": "Line width:", "ger": "Linienstärke:"},
            "fig_width_text": {"eng": "Figure width:", "ger": "Fensterbreite:"},
            "fig_height_text": {"eng": "Figure height:", "ger": "Fensterhöhe:"},
            "marker_size_text": {"eng": "Marker size:", "ger": "Markergröße:"}}


# ======================================================================================================================
#                                                   GUI  settings
# ======================================================================================================================
sg.change_look_and_feel("Dark")

tab_diag_type_layout = [[sg.Text(lan_dict["fluid_name_text1"]["eng"], key="fluid_name_text1", pad=((10, 0), (10, 0)),
                                 size=(15, 1)),
                         sg.Combo(["R1234YF", "R1234ZEE", "R1234ZF", "R134a", "R161", "R32", "R404A.MIX", "R410A.MIX",
                                   "R454C", "R457A", "PROPANE"],
                                  key="fluid_combo", default_value="R134a", pad=((0, 0), (10, 0)), size=(20, 1))],
                        [sg.Text(lan_dict["fluid_name_text2"]["eng"], key="fluid_name_text2", pad=((10, 0), (5, 0)),
                                 size=(14, 1)),
                         sg.Input(key="fluid_input", size=(22, 1), pad=((7, 10), (5, 0)), default_text="")],
                        [sg.Radio("", "radio_diag", key="T_s_radio", pad=((10, 0), (10, 0)),
                                  enable_events=True, default=True),
                         sg.Text(lan_dict["T_s_radio_text"]["eng"], key="T_s_radio_text", pad=((2, 0), (10, 0)),
                                 size=(20, 1))],
                        [sg.Radio("", "radio_diag", key="T_h_radio", pad=((10, 0), (0, 0)), enable_events=True),
                         sg.Text(lan_dict["T_h_radio_text"]["eng"], key="T_h_radio_text", pad=((2, 0), (0, 0)),
                                 size=(20, 1))],
                        [sg.Radio("", "radio_diag", key="log(p)_h_radio", pad=((10, 0), (0, 0)), enable_events=True),
                         sg.Text(lan_dict["log(p)_h_radio_text"]["eng"], key="log(p)_h_radio_text",
                                 pad=((2, 0), (0, 0)), size=(20, 1))],
                        [sg.Text(lan_dict["saving_format_text"]["eng"], key="saving_format_text",
                                 pad=((10, 0), (5, 5)), size=(15, 1)),
                         sg.Combo(["pdf", "png", "svg"], key="saving_combo", pad=((0, 0), (5, 5)), size=(20, 1))],
                        [sg.Button(lan_dict["create_diag_button"]["eng"], key="create_diag_button", size=(25, 1),
                                   pad=((10, 0), (5, 10)), button_color=("black", "green"), bind_return_key=True)]]

tab_state_layout = [[sg.Text(lan_dict["state_text"]["T-s"]["eng"], key="state_text", pad=((10, 0), (10, 0)),
                             size=(60, 4))],
                    [sg.Input(key="state_input", size=(72, 1), pad=((10, 10), (4, 0)), default_text="")],
                    [sg.Text(lan_dict["iso_text"]["T-s"]["eng"], key="iso_text", pad=((10, 0), (25, 0)), size=(47, 2)),
                     sg.Text(lan_dict["offset_text"]["eng"], key="offset_text", pad=((5, 0), (10, 0)), size=(17, 3))],
                    [sg.Input(key="iso_input", size=(52, 1), pad=((10, 10), (1, 0)), default_text=""),
                     sg.Input(key="offset_input", size=(17, 1), pad=((5, 10), (1, 0)), default_text="300")]]

tab_diag_settings_layout = [[sg.Text(lan_dict["diag_text"]["eng"], key="diag_text", pad=((10, 0), (10, 0)),
                                     size=(60, 1))],
                            [sg.Text(lan_dict["left_x_limit_text"]["eng"], key="left_x_limit_text",
                                     pad=((15, 0), (0, 0)), size=(12, 1)),
                             sg.Input(key="left_x_limit_input", size=(12, 1), disabled=True, default_text="1"),
                             sg.Text(lan_dict["right_x_limit_text"]["eng"], key="right_x_limit_text",
                                     pad=((60, 0), (0, 0)), size=(12, 1)),
                             sg.Input(key="right_x_limit_input", size=(12, 1), disabled=True, default_text="2")],
                            [sg.Text(lan_dict["lower_y_limit_text"]["eng"], key="lower_y_limit_text",
                                     pad=((15, 0), (0, 0)), size=(12, 1)),
                             sg.Input(key="lower_y_limit_input", size=(12, 1), disabled=True, default_text="265"),
                             sg.Text(lan_dict["upper_y_limit_text"]["eng"], key="upper_y_limit_text",
                                     pad=((60, 0), (0, 0)), size=(12, 1)),
                             sg.Input(key="upper_y_limit_input", size=(12, 1), disabled=True, default_text="350")],
                            [sg.Checkbox("", key="scale_checkbox", pad=((15, 0), (5, 0)), enable_events=True,
                                         default=True),
                             sg.Text(lan_dict["scale_checkbox_text"]["eng"], key="scale_checkbox_text",
                                     pad=((2, 0), (5, 0)), size=(28, 1)),
                             sg.Checkbox("", key="title_checkbox", pad=((0, 0), (5, 0)), default=True),
                             sg.Text(lan_dict["title_checkbox_text"]["eng"], key="title_checkbox_text",
                                     pad=((2, 0), (5, 0)), size=(30, 1))],
                            [sg.Checkbox("", key="grid_checkbox", pad=((15, 0), (0, 0)), default=True),
                             sg.Text(lan_dict["grid_checkbox_text"]["eng"], key="grid_checkbox_text",
                                     pad=((2, 0), (0, 0)), size=(29, 1))],
                            [sg.Text(lan_dict["vapor_dome_text"]["eng"], key="vapor_dome_text", pad=((10, 0), (10, 0)),
                                     size=(40, 1))],
                            [sg.Text(lan_dict["resolution_text"]["eng"], key="resolution_text", pad=((15, 0), (0, 0)),
                                     size=(12, 1)),
                             sg.Input(key="resolution_input", size=(12, 1), default_text="100"),
                             sg.Text(lan_dict["p_min_text"]["eng"], key="p_min_text", pad=((60, 0), (0, 0)),
                                     size=(12, 1)),
                             sg.Input(key="p_min_input", size=(12, 1), default_text="0.5")],
                            [sg.Text("", pad=((0, 0), (0, 0)), size=(1, 1))]]


tab_gen_settings_layout = [[sg.Text(lan_dict["lan_text"]["eng"], key="lan_text", pad=((10, 0), (10, 0)), size=(40, 1))],
                           [sg.Radio("", "radio_lan", key="eng_radio", pad=((15, 0), (0, 0)), enable_events=True,
                                     default=True),
                            sg.Text(lan_dict["eng_radio_text"]["eng"], key="eng_radio_text", pad=((2, 0), (0, 0)),
                                    size=(20, 1))],
                           [sg.Radio("", "radio_lan", key="ger_radio", pad=((15, 0), (0, 0)), enable_events=True),
                            sg.Text(lan_dict["ger_radio_text"]["eng"], key="ger_radio_text", pad=((2, 0), (0, 0)),
                                    size=(20, 1))],
                           [sg.Text(lan_dict["font_size_settings_text"]["eng"], key="font_size_settings_text",
                                    pad=((10, 0), (10, 0)), size=(40, 1))],
                           [sg.Text(lan_dict["font_size_text"]["eng"], key="font_size_text", pad=((15, 0), (0, 0)),
                                    size=(12, 1)),
                            sg.Input(key="font_size_input", size=(12, 1), default_text="12"),
                            sg.Text(lan_dict["line_width_text"]["eng"], key="line_width_text", pad=((60, 0), (0, 0)),
                                    size=(12, 1)),
                            sg.Input(key="line_width_input", size=(12, 1), default_text="2")],
                           [sg.Text(lan_dict["fig_height_text"]["eng"], key="fig_height_text", pad=((15, 0), (0, 0)),
                                    size=(12, 1)),
                            sg.Input(key="fig_height_input", size=(12, 1), default_text="16"),
                            sg.Text(lan_dict["fig_width_text"]["eng"], key="fig_width_text", pad=((60, 0), (0, 0)),
                                    size=(12, 1)),
                            sg.Input(key="fig_width_input", size=(12, 1), default_text="20")],
                           [sg.Text(lan_dict["marker_size_text"]["eng"], key="marker_size_text", pad=((15, 0), (0, 0)),
                                    size=(12, 1)),
                            sg.Input(key="marker_size_input", size=(12, 1), default_text="5")]]


layout = [[sg.TabGroup([[sg.Tab(lan_dict["diag_tab"]["eng"], tab_diag_type_layout, key="diag_tab"),
                         sg.Tab(lan_dict["state_tab"]["eng"], tab_state_layout, key="state_tab"),
                         sg.Tab(lan_dict["diag_settings_tab"]["eng"], tab_diag_settings_layout,
                                key="diag_settings_tab"),
                         sg.Tab(lan_dict["gen_settings_tab"]["eng"], tab_gen_settings_layout,
                                key="gen_settings_tab")]])]]


# ======================================================================================================================
#                                                 GUI - functions
# ======================================================================================================================
def open_diag_configurator_window():
    """ opens diagram configurator window
    """

    window = sg.Window("Diagram configurator", layout, size=(550, 240))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == "T_s_radio":
            selected_diag_type = "T-s"
            selected_lan = get_selected_lan(values)
            window["state_text"].update(lan_dict["state_text"][selected_diag_type][selected_lan])
            window["left_x_limit_input"].update("1")
            window["right_x_limit_input"].update("2")
            window["lower_y_limit_input"].update("265")
            window["upper_y_limit_input"].update("350")
        elif event == "T_h_radio":
            selected_diag_type = "T-h"
            selected_lan = get_selected_lan(values)
            window["state_text"].update(lan_dict["state_text"][selected_diag_type][selected_lan])
            window["left_x_limit_input"].update("140")
            window["right_x_limit_input"].update("450")
            window["lower_y_limit_input"].update("230")
            window["upper_y_limit_input"].update("390")
        elif event == "log(p)_h_radio":
            selected_diag_type = "log(p)-h"
            selected_lan = get_selected_lan(values)
            window["state_text"].update(lan_dict["state_text"][selected_diag_type][selected_lan])
            window["left_x_limit_input"].update("200")
            window["right_x_limit_input"].update("500")
            window["lower_y_limit_input"].update("100000")
            window["upper_y_limit_input"].update("5000000")

        if event == "scale_checkbox":
            if values["scale_checkbox"]:
                window["left_x_limit_input"].update(disabled=True)
                window["right_x_limit_input"].update(disabled=True)
                window["lower_y_limit_input"].update(disabled=True)
                window["upper_y_limit_input"].update(disabled=True)
            else:
                window["left_x_limit_input"].update(disabled=False)
                window["right_x_limit_input"].update(disabled=False)
                window["lower_y_limit_input"].update(disabled=False)
                window["upper_y_limit_input"].update(disabled=False)

        if values["eng_radio"]:
            window.set_title("Diagram configurator")
            for gui_element in lan_dict:
                if gui_element == "state_text" or gui_element == "iso_text":
                    selected_diag_type = get_selected_diag_type(values)
                    window[gui_element].update(lan_dict[gui_element][selected_diag_type]["eng"])
                else:
                    window[gui_element].update(lan_dict[gui_element]["eng"])
        elif values["ger_radio"]:
            window.set_title("Diagrammkonfigurator")
            for gui_element in lan_dict:
                if gui_element == "state_text" or gui_element == "iso_text":
                    selected_diag_type = get_selected_diag_type(values)
                    window[gui_element].update(lan_dict[gui_element][selected_diag_type]["ger"])
                else:
                    window[gui_element].update(lan_dict[gui_element]["ger"])

        if event == "create_diag_button":
            window.close()

            selected_fluid = values["fluid_combo"]
            if not values["fluid_input"] == "":
                selected_fluid = values["fluid_input"]

            selected_diag_type = get_selected_diag_type(values)
            selected_lan = get_selected_lan(values)

            state_input = values["state_input"].replace("(", "")
            state_input = state_input.replace(")", "")
            state_input = state_input.split(",")
            state_input_list = []
            if not state_input[0] == "":
                for i in range(0, len(state_input), 2):
                    state_input_list.append((float(state_input[i]), float(state_input[i + 1])))

            iso_input_list = values["iso_input"].split(",")
            if not iso_input_list[0] == "":
                for i in range(0, len(iso_input_list)):
                    iso_input_list[i] = float(iso_input_list[i])
            else:
                iso_input_list = []

            diag_settings = {"left_x_limit": float(values["left_x_limit_input"]),
                             "right_x_limit": float(values["right_x_limit_input"]),
                             "upper_y_limit": float(values["upper_y_limit_input"]),
                             "lower_y_limit": float(values["lower_y_limit_input"]),
                             "scale_checkbox": values["scale_checkbox"],
                             "title_checkbox": values["title_checkbox"],
                             "grid_checkbox": values["grid_checkbox"],
                             "resolution": int(values["resolution_input"]),
                             "p_min": float(values["p_min_input"])}

            gen_settings = {"selected_lan": selected_lan,
                            "font_size": int(values["font_size_input"]),
                            "line_width": int(values["line_width_input"]),
                            "fig_height": int(values["fig_height_input"]),
                            "fig_width": int(values["fig_width_input"]),
                            "marker_size": int(values["marker_size_input"])}

            create_diagram(selected_fluid, selected_diag_type, state_input_list, iso_input_list,
                           int(values["offset_input"]), diag_settings, gen_settings, values["saving_combo"])

    window.close()


def get_selected_lan(values):
    """ returns selected language

    Parameters:
    :param List values:
        values of the window
    Return:
    :return string selected_lan:
        Selected language
    """

    selected_lan = "eng"
    if values["ger_radio"]:
        selected_lan = "ger"
    return selected_lan


def get_selected_diag_type(values):
    """ returns selected diagram type

    Parameters:
    :param List values:
        values of the window
    Return:
    :return string selected_diag_type:
        Selected diagram type
    """

    selected_diag_type = "T-s"
    if values["T_h_radio"]:
        selected_diag_type = "T-h"
    elif values["log(p)_h_radio"]:
        selected_diag_type = "log(p)-h"
    return selected_diag_type
