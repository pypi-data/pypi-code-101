from datetime import timedelta, datetime
from inspect import stack
from logging import Logger, getLogger

from dash import Dash
from dash.html import Div, H3, Table, Tr, Td
from dash.dcc import Dropdown, Graph
from dash.dependencies import Input, Output
from pandas import DataFrame
from plotly.graph_objs import Figure, Scatter
from plotly.subplots import make_subplots

from com.enovation.toolbox.predictability.bean import PredictabilityBean
from com.enovation.toolbox.predictability.dp_date_predictability.dp_computer import DatePredictabilityComputer


class DatePredictabilityGrapher:
    _logger: Logger = getLogger(__name__)

    def graph_predictability(
            self,
            obj_predictability: PredictabilityBean
    ):
        self._logger.debug(f"Function '{stack()[0].filename} - {stack()[0].function}' is called.")

        obj_the_dash_instance: Dash = Dash(
            __name__,
            external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
        )

        obj_the_dash_instance.layout = Div([

            # A title
            H3("Zoom on a given key"),

            # The filter to select a key (aka. a project, an opportunity, etc) to graph and zoom in
            Dropdown(
                id="key_drop_down",
                placeholder="Select a key to graph and zoom in...",
                options=[
                    {'label': x, 'value': x}
                    for x in obj_predictability.df_by_key[DatePredictabilityComputer.str__input__column_label__key]
                ],
            ),

            Div([
                # The graph
                Graph(id='predictability_graph'),

                # The table
                Table([
                    Tr([Td(x), Td("--", id=x)])
                    for x in obj_predictability.df_by_key.columns
                ]),
            ]),
        ])

        @obj_the_dash_instance.callback(
            [Output(x, 'children') for x in obj_predictability.df_by_key.columns],
            Input('key_drop_down', 'value'))
        def callback_update_table(str_key):

            # If we have a key selected in the drop down
            if str_key:

                # We return the statistics for this key, as a list
                return obj_predictability.df_by_key[
                           obj_predictability.df_by_key[
                               DatePredictabilityComputer.str__input__column_label__key
                           ] == str_key
                           ].iloc[0, :].tolist()

            # Else, we have no key selected in the drop down
            else:

                # We return "--" for each field
                return ["--"] * len(obj_predictability.df_by_key.columns)

        @obj_the_dash_instance.callback(
            Output('predictability_graph', 'figure'),
            Input('key_drop_down', 'value')
        )
        def callback_update_graph(str_key):

            # We instantiate the Figure object that will be rendered
            # fig_the_figure: Figure = Figure()
            fig_the_figure: Figure = make_subplots(specs=[[{"secondary_y": True}]])

            # Add figure title
            fig_the_figure.update_layout(
                title_text=f"Date Predictability for <b>{str_key}</b>"
            )

            # Set x-axis title
            fig_the_figure.update_xaxes(title_text=DatePredictabilityComputer.str__input__column_label__date)

            # Set y-axes titles
            fig_the_figure.update_yaxes(
                title_text=DatePredictabilityComputer.str__input__column_label__measure,
                secondary_y=False)
            fig_the_figure.update_yaxes(
                title_text=DatePredictabilityComputer.str__output__column_label__predictability,
                range=[0, 1],
                tickformat=',.0%',
                secondary_y=True)

            # If we have a key selected in the drop down
            if str_key:

                # We select the data for that selected key
                df_the_historical_data: DataFrame = obj_predictability.df_historical[
                    obj_predictability.df_historical[
                        DatePredictabilityComputer.str__input__column_label__key
                    ] == str_key
                    ]
                d_the_stats_data: dict = obj_predictability.df_by_key[
                                             obj_predictability.df_by_key[
                                                 DatePredictabilityComputer.str__input__column_label__key
                                             ] == str_key
                                             ].iloc[0, :].to_dict()

                # We trace the projected measures
                fig_the_figure.add_trace(
                    Scatter(
                        x=df_the_historical_data[DatePredictabilityComputer.str__input__column_label__date],
                        y=df_the_historical_data[DatePredictabilityComputer.str__input__column_label__measure],
                        name=DatePredictabilityComputer.str__input__column_label__measure,
                    )
                )

                # We trace the reference system: the cone converging towards the last measure
                dt_the_bottom_left_corner: datetime = min(
                    d_the_stats_data[DatePredictabilityComputer.str__statistics__column_label__measure_last],
                    d_the_stats_data[DatePredictabilityComputer.str__statistics__column_label__date_first]
                )
                dt_the_top_right_corner: datetime = max(
                    d_the_stats_data[DatePredictabilityComputer.str__statistics__column_label__measure_last],
                    d_the_stats_data[DatePredictabilityComputer.str__statistics__column_label__date_last]
                )
                dt_the_top_left_corner: datetime = max(
                    d_the_stats_data[DatePredictabilityComputer.str__statistics__column_label__measure_last],
                    d_the_stats_data[DatePredictabilityComputer.str__statistics__column_label__measure_last]
                    + timedelta(
                        days=(
                                d_the_stats_data[DatePredictabilityComputer.str__statistics__column_label__measure_last]
                                - d_the_stats_data[DatePredictabilityComputer.str__statistics__column_label__date_first]
                        ).days
                    )
                )
                dt_the_bottom_right_corner: datetime = min(
                    d_the_stats_data[DatePredictabilityComputer.str__statistics__column_label__measure_last],
                    d_the_stats_data[DatePredictabilityComputer.str__statistics__column_label__measure_last]
                    - timedelta(
                        days=(
                                d_the_stats_data[DatePredictabilityComputer.str__statistics__column_label__date_last]
                                - d_the_stats_data[
                                    DatePredictabilityComputer.str__statistics__column_label__measure_last]
                        ).days
                    )
                )

                # 1. The last measure, as an horizontal line
                fig_the_figure.add_trace(
                    Scatter(
                        x=[
                            dt_the_bottom_left_corner,
                            dt_the_top_right_corner
                            # d_the_stats_data[DatePredictabilityComputer.str__statistics__column_label__date_first],
                            # d_the_stats_data[DatePredictabilityComputer.str__statistics__column_label__date_last],
                        ],
                        y=[
                            d_the_stats_data[DatePredictabilityComputer.str__statistics__column_label__measure_last],
                            d_the_stats_data[DatePredictabilityComputer.str__statistics__column_label__measure_last],
                        ],
                        name=DatePredictabilityComputer.str__statistics__column_label__measure_last,
                    )
                )

                # 2. The increasing cone
                fig_the_figure.add_trace(
                    Scatter(
                        x=[dt_the_bottom_left_corner, dt_the_top_right_corner],
                        y=[dt_the_bottom_left_corner, dt_the_top_right_corner],
                        name="Increasing cone",
                    )
                )

                # 3. The decreasing cone
                fig_the_figure.add_trace(
                    Scatter(
                        x=[dt_the_bottom_left_corner, dt_the_top_right_corner],
                        y=[dt_the_top_left_corner, dt_the_bottom_right_corner],
                        name="Decreasing cone",
                    )
                )

                # We trace the predictability
                fig_the_figure.add_trace(
                    Scatter(
                        x=df_the_historical_data[DatePredictabilityComputer.str__input__column_label__date],
                        y=df_the_historical_data[DatePredictabilityComputer.str__output__column_label__predictability],
                        name=DatePredictabilityComputer.str__output__column_label__predictability,
                    ),
                    secondary_y=True
                )

                fig_the_figure.update_traces(mode='markers+lines', hovertemplate=None)
                fig_the_figure.update_layout(legend=dict(y=0.5, traceorder='reversed', font_size=16))

                return fig_the_figure

            else:
                # Todo: return here a figure which is a rectangle with a message to select a key
                return Figure()

        obj_the_dash_instance.run_server(debug=True, use_reloader=False)

        self._logger.debug(f"Function '{stack()[0].filename} - {stack()[0].function}' is returning.")
