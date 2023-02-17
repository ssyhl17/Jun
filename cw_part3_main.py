from parametric_simulation2 import run_two_parameter_parametric
from energy_plus_two_parameters import EnergyPlus
import csv

eplus_run_path = './energyplus9.5/energyplus'
idf_path = './1ZoneUncontrolled_win_1.idf'

# Set parameter values and ranges
key_of_window_u = ['WindowMaterial:SimpleGlazingSystem',
                   'SimpleWindow:DOUBLE PANE WINDOW',
                   'solar_heat_gain_coefficient']

vals_of_window_u = []
for i in range(100, 250, 10):
    vals_of_window_u.append(i / 100)

key_of_window_s = ['WindowMaterial:SimpleGlazingSystem',
                   'SimpleWindow:DOUBLE PANE WINDOW',
                   'u_factor']

vals_of_window_s = []
for i in range(25, 75, 5):
    vals_of_window_s.append(i / 100)

# Create an EnergyPlusParameter object
energy_plus_parameter = EnergyPlus()

# Assign a value to window U
result_u = energy_plus_parameter.set_window_u(
    key_of_window_u, vals_of_window_u, val_range=(1.0, 2.5))

# Assign a value to window SHGC
parameter_result_s = energy_plus_parameter.set_window_s(
    key_of_window_s, vals_of_window_s, val_range=(0.25, 0.75))


def indoor_temp_mean(filename):
    # Reading a csv file
    with open(filename, 'r') as fp:
        reader = csv.reader(fp)
        # The list stores temp data
        indoor_temp = []
        # Iterate over the csv file, saving its temperature to the list
        for i, row in enumerate(reader):
            if i > 0:
                indoor_temp.append(float(row[8]))
    indoor_temp_sum = sum(indoor_temp)
    indoor_temp_length = len(indoor_temp)
    mean_temp = 0.0
    if len(indoor_temp) != 0:
        mean_temp = indoor_temp_sum / indoor_temp_length
    return mean_temp


if parameter_result_s and parameter_result_s:
    output_dir = 'param_window'
    u_key_vals = energy_plus_parameter.get_window_u()
    s_key_vals = energy_plus_parameter.get_window_s()

    output_paths, vals = run_two_parameter_parametric(eplus_run_path, idf_path, output_dir,
                                                      u_key_vals[0], u_key_vals[1],
                                                      s_key_vals[0], s_key_vals[1])

    print("output_paths:", output_paths)
    indoor_max_mean_temp = 0.0
    for key_value, val in zip(output_paths.keys(), vals):
        # Call the function to calculate the mean temperature
        this_mean = indoor_temp_mean('./' + output_paths[key_value])
        if this_mean > indoor_max_mean_temp:
            indoor_max_mean_temp = this_mean
            max_value = val

    print('The temp of window U:', max_value[0], ', window SHGC:', max_value[1])
