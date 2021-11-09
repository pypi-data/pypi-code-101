import ipywidgets as widgets
from IPython.display import clear_output, display
from ipywidgets import VBox, HBox, Layout
import time
from replifactory.GUI.device_control_widgets import StirrerWidgets
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


class CalibrationTab:
    def __init__(self, main_gui):
        self.title = "Calibration"
        self.main_gui = main_gui
        self.button = widgets.Button(description="Show device parameters")
        self.button.on_click(self.handle_button_click)
        self.output = widgets.Output()
        self.widget = VBox([self.button, self.output])
        self.update()

    def handle_button_click(self, button):
        self.update()

    def update(self):
        if self.main_gui.device is not None:
            with self.output:
                clear_output()
                time.sleep(0.1)
                display(StirrerWidgets(self.main_gui.device).widget)
                display(CalibratePump(self.main_gui.device).widget)
                for od_sensor in self.main_gui.device.od_sensors.values():
                    od_sensor.calibration_curve()
                    plt.show()
                # self.main_gui.device.show_parameters()
        else:
            with self.output:
                clear_output()
                time.sleep(0.1)
                print("No device available")


class InputWidget:
    def __init__(self, q):
        self.name = q
        self.input = widgets.FloatText(description=q, style={'description_width': 'initial'})
        self.submit = widgets.Button(description="submit")
        self.widget = HBox([self.input, self.submit])


class CalibratePump:
    def __init__(self, device):
        layout = Layout(display='flex', width='300px')
        style = {'description_width': '120px'}
        self.device = device
        self.pump_number = widgets.Dropdown(description="Pump",
                                            description_tooltip="Pump number\n1: Fresh medium\n\
                                            2: Drug1 medium\n3: Drug2 medium\n4: Waste vacuum",
                                            options=[1, 2, 3, 4], index=None, style=style, layout=layout,
                                            continuous_update=False)
        self.stock_volume = widgets.FloatText(description="stock volume",
                                              description_tooltip="Volume available for pumping\n\
                                              (free volume in waste bottle)",
                                              style=style, layout=layout)
        self.stock_concentration = widgets.FloatText(description="stock concentration",
                                                     description_tooltip="leave empty for fresh medium and waste",
                                                     style=style, layout=layout)
        self.calibration_label = widgets.HTML('<b>Pump calibration:</b>\n place a vial on scales and measure the \
        pumped volume to calibrate the pumps. Repeat the measurement between 1-100 rotations to build a multipoint \
        calibration curve that accounts for pressure buildup during longer, faster pump runs',
                                              style=style, layout=Layout(width="600px"))

        #         self.calibration_label = widgets.Label("""""")
        self.rotations = widgets.FloatText(description="rotations",
                                           description_tooltip="number of rotations of pump head",
                                           style=style, layout=layout)
        self.iterations = widgets.IntText(description="iterations",
                                          description_tooltip="number of repetitions for averaging \
                                          pumped volume measurement",
                                          style=style, layout=layout)
        self.vial = widgets.Dropdown(description="Vial", description_tooltip="Vial to pump into",
                                     options=[1, 2, 3, 4, 5, 6, 7], style=style, layout=layout)
        self.vial.observe(self.update_vial)
        self.output = widgets.Output()
        self.output2 = widgets.Output()
        self.run_button = widgets.Button(description="RUN", button_style="danger")
        self.plot_button = widgets.Button(description="plot")

        args = VBox([self.pump_number, self.stock_volume, self.stock_concentration, self.calibration_label,
                     self.vial, self.rotations, self.iterations, self.output, self.run_button])
        self.widget = VBox([args, self.output2], style=style, layout=Layout(display='flex',
                                                               flex_flow='column',
                                                               border='solid',
                                                               width='720px'))

        self.pump_number.observe(self.update_pump)
        self.rotations.observe(self.update)
        self.iterations.observe(self.update)
        self.stock_concentration.observe(self.update_stock_concentration)
        self.stock_volume.observe(self.update_stock_volume)
        self.run_button.on_click(self.run)
        self.update(0)

    @property
    def pump(self):
        return self.device.pumps[self.pump_number.value]

    def update_vial(self, change):
        vial = self.vial.value
        assert not self.device.is_pumping()
        for valve in range(1, 8):
            if self.device.valves.is_open[valve] or self.device.valves.is_open[valve] is None:
                if valve != self.vial.value:
                    self.device.valves.close(valve=valve)
        self.device.valves.open(valve=self.vial.value)

    def update_pump(self, change):
        self.update(0)
        if self.pump_number.value in [1, 2, 3, 4]:
            self.stock_concentration.value = self.pump.stock_concentration
            self.stock_volume.value = self.pump.stock_volume
            self.generate_plot()

    def update_stock_volume(self, change):
        self.pump.stock_volume = self.stock_volume.value

    def update_stock_concentration(self, change):
        self.pump.stock_concentration = self.stock_concentration.value

    def update(self, change):
        if self.pump_number.value in [1, 2, 3, 4]:
            with self.output:
                clear_output()
                pump_number = self.pump_number.value
                n_rotations = self.rotations.value
                n_iterations = self.iterations.value

                print("Pump %d will make %.1f rotations %d times" % (pump_number, n_rotations, n_iterations))
                pump = self.device.pumps[pump_number]
                total_volume = n_rotations * n_iterations * 0.1  # initial estimate
                pump.fit_calibration_function()
                if callable(pump.calibration_function):
                    def opt_function(volume):
                        return pump.calibration_function(volume) - n_rotations

                    predicted_mls = fsolve(opt_function, 1)[0]
                    predicted_total_mls = predicted_mls * n_iterations
                    total_volume = predicted_total_mls
                print("  (volume: ~%.2f mL)" % total_volume)

    def generate_plot(self):
        pump_number = self.pump_number.value
        pump = self.device.pumps[pump_number]
        with self.output2:
            clear_output()
            pump.calibration_curve()
            plt.show()

    def run(self, button):
        n_rotations = self.rotations.value
        n_iterations = self.iterations.value

        with self.output:
            print("Pumping...")
            for i in range(n_iterations):
                self.pump.move(n_rotations)
                print("%d/%d" % (i + 1, n_iterations), end="\t\r")
                while self.pump.is_pumping():
                    time.sleep(0.1)
                time.sleep(0.5)
            mlinput = InputWidget("How many ml?")
            display(mlinput.widget)

            def on_submit(button):
                ml = mlinput.input.value
                ml = ml / n_iterations
                self.device.calibration_pump_rotations_to_ml[self.pump_number.value][n_rotations] = round(ml, 3)
                self.device.save()
                self.generate_plot()

            mlinput.submit.on_click(on_submit)
