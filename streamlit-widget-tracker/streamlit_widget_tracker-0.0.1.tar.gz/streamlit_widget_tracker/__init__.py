import streamlit as st
from streamlit.report_thread import get_report_ctx
import streamlit_text_like as st_like

def start_tracking(exclude_key=None,passive_func=None):
    from streamlit_text_like import streamlit_text_like

    widget_values = {}

    def widget_wrapper(f, exclude_key):

        def wrapper(*args, **kwargs):
            """
            Helps keep track of widget interaction in streamlit.

            Args:
            exclude_key -> Pass key of widget to exclude it from being tracked

            Returns:
            Dictionary of widget state
            """
            if not 'key' in kwargs:
                raise AttributeError("Please pass a key to streamlit widget")

            widget_value = f(*args, **kwargs)
            key = kwargs['key']


            if (exclude_key is None) or (key not in exclude_key):
                """ key will be tracked """
                widget_values[key] = widget_value
            else:
                """ key will not be tracked """
                pass

            return widget_value

        return wrapper

    """ 
    Getting Session id - will be helpful if you want to manually track user device data
    """
    ctx = get_report_ctx()
    session_id = ctx.session_id
    widget_values = {'session_id': session_id}

    streamlit_text_like=widget_wrapper(streamlit_text_like,exclude_key)
    st_like.streamlit_text_like=widget_wrapper(st_like.streamlit_text_like,exclude_key)
    st.button = widget_wrapper(st.button, exclude_key)
    st.slider = widget_wrapper(st.slider, exclude_key)
    st.selectbox = widget_wrapper(st.selectbox, exclude_key)
    st.multiselect = widget_wrapper(st.multiselect, exclude_key)
    st.checkbox = widget_wrapper(st.checkbox, exclude_key)
    st.slider = widget_wrapper(st.slider, exclude_key)
    st.radio = widget_wrapper(st.radio, exclude_key)
    st.select_slider = widget_wrapper(st.select_slider, exclude_key)
    st.text_input = widget_wrapper(st.text_input, exclude_key)
    st.number_input = widget_wrapper(st.number_input, exclude_key)
    st.text_area = widget_wrapper(st.text_area, exclude_key)
    st.date_input = widget_wrapper(st.date_input, exclude_key)
    st.time_input = widget_wrapper(st.time_input, exclude_key)
    st.file_uploader = widget_wrapper(st.file_uploader, exclude_key)
    st.color_picker = widget_wrapper(st.color_picker, exclude_key)
    st.download_button = widget_wrapper(st.download_button, exclude_key)

    st.sidebar.button = widget_wrapper(st.sidebar.button, exclude_key)
    st.sidebar.slider = widget_wrapper(st.sidebar.slider, exclude_key)
    st.sidebar.selectbox = widget_wrapper(st.sidebar.selectbox, exclude_key)
    st.sidebar.multiselect = widget_wrapper(st.sidebar.multiselect, exclude_key)
    st.sidebar.checkbox = widget_wrapper(st.sidebar.checkbox, exclude_key)
    st.sidebar.slider = widget_wrapper(st.sidebar.slider, exclude_key)
    st.sidebar.radio = widget_wrapper(st.sidebar.radio, exclude_key)
    st.sidebar.select_slider = widget_wrapper(st.sidebar.select_slider, exclude_key)
    st.sidebar.text_input = widget_wrapper(st.sidebar.text_input, exclude_key)
    st.sidebar.number_input = widget_wrapper(st.sidebar.number_input, exclude_key)
    st.sidebar.text_area = widget_wrapper(st.sidebar.text_area, exclude_key)
    st.sidebar.date_input = widget_wrapper(st.sidebar.date_input, exclude_key)
    st.sidebar.time_input = widget_wrapper(st.sidebar.time_input, exclude_key)
    st.sidebar.file_uploader = widget_wrapper(st.sidebar.file_uploader, exclude_key)
    st.sidebar.color_picker = widget_wrapper(st.sidebar.color_picker, exclude_key)
    st.sidebar.download_button = widget_wrapper(st.sidebar.download_button, exclude_key)

    return widget_values
