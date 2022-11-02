from parametric_simulation import run_one_parameter_parametric
from post_processor import plot_1D_results

eplus_run_path = './energyplus9.5/energyplus'
idf_path = './1ZoneUncontrolled_win_1.idf'
output_dir = './param_exp_1'
parameter_key = ['WindowMaterial:SimpleGlazingSystem',
                'SimpleWindow:DOUBLE PANE WINDOW',
                'solar_heat_gain_coefficient']
parameter_vals=list(range(25,75,2))
for i in range(25):
    parameter_vals[i]=parameter_vals[i]/100
plot_column_name = 'ZONE ONE:Zone Mean Air Temperature [C](TimeStep) '
y_axis_title = 'Indoor Air Temperature (C)'
plot_title = 'Simulation of Indoor Air Temperature vs. SHGC'
'''
output_paths = run_one_parameter_parametric(eplus_run_path, idf_path, output_dir,
                                parameter_key, parameter_vals)
'''
#print(output_paths)
output_paths={'0.25': './param_exp_1/run1/eplusout.csv', '0.27': './param_exp_1/run2/eplusout.csv', '0.29': './param_exp_1/run3/eplusout.csv', '0.31': './param_exp_1/run4/eplusout.csv', '0.33': './param_exp_1/run5/eplusout.csv', '0.35': './param_exp_1/run6/eplusout.csv', '0.37': './param_exp_1/run7/eplusout.csv', '0.39': './param_exp_1/run8/eplusout.csv', '0.41': './param_exp_1/run9/eplusout.csv', '0.43': './param_exp_1/run10/eplusout.csv', '0.45': './param_exp_1/run11/eplusout.csv', '0.47': './param_exp_1/run12/eplusout.csv', '0.49': './param_exp_1/run13/eplusout.csv', '0.51': './param_exp_1/run14/eplusout.csv', '0.53': './param_exp_1/run15/eplusout.csv', '0.55': './param_exp_1/run16/eplusout.csv', '0.57': './param_exp_1/run17/eplusout.csv', '0.59': './param_exp_1/run18/eplusout.csv', '0.61': './param_exp_1/run19/eplusout.csv', '0.63': './param_exp_1/run20/eplusout.csv', '0.65': './param_exp_1/run21/eplusout.csv', '0.67': './param_exp_1/run22/eplusout.csv', '0.69': './param_exp_1/run23/eplusout.csv', '0.71': './param_exp_1/run24/eplusout.csv', '0.73': './param_exp_1/run25/eplusout.csv'}

plot_1D_results(output_paths, plot_column_name,
                    y_axis_title, plot_title)