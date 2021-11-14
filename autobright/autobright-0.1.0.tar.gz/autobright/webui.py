import sys

import altair as alt
import streamlit as st
import streamlit.cli as st_cli

from autobright.colorhugals import ColorHug
from autobright.ddccontrol import DDCControl
from autobright.measurements import Measurements
from autobright.models import ProportionalBrightnessModel


def ui():
    sensor = ColorHug()
    display = DDCControl(7)
    model = ProportionalBrightnessModel()
    measurements = Measurements()

    st.markdown("# Display")

    manual_brightness = st.slider("Brightness", 0, 100)
    if st.button("Set"):
        display.set_brightness(manual_brightness)

    st.markdown("# Measurements")

    if st.button("Save"):
        reading = sensor.get_reading()
        st.markdown(f"Reading: {reading}")
        measurements.add_measurement(reading, manual_brightness)

    chart = (
        alt.Chart(measurements.get_measurements())
        .mark_point()
        .encode(alt.X("reading"), alt.Y("brightness"), alt.Tooltip("datetime"))
        .interactive()
    )
    st.altair_chart(chart)


def main():
    sys.argv = ["streamlit", "run", __file__]
    sys.exit(st_cli.main())


if __name__ == "__main__" and st._is_running_with_streamlit:
    ui()
