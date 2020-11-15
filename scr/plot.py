import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


class CreatePlot:
    def __init__(self, sample_df):
        self.sample_df = sample_df

    def categorical_count_bar_plot(self, categorical_column, percent=False):
        """
        Created using Plotly Bar Charts: https://plotly.com/python/bar-charts/.

        Creates a plot counting the values of a categorical column
        :param categorical_column: The column with categorical values
        :return: The figure of the plot, ready to be showed.
        """

        values = self.sample_df[categorical_column].value_counts().tolist()
        values_perc = [round(value / sum(values) * 100, 2) for value in values]
        categories = self.sample_df[categorical_column].unique().tolist()

        title = (
            f"Valores em Percentual: {categorical_column}"
            if percent
            else f"Valores em Quantidade: {categorical_column}"
        )
        fig = go.Figure()

        if percent:
            fig.add_trace(
                go.Bar(
                    x=values_perc,
                    y=categories,
                    name=f"{categorical_column}",
                    marker_color="black",
                    orientation="h",
                ),
            )
        else:
            fig.add_trace(
                go.Bar(
                    x=values,
                    y=categories,
                    name=f"{categorical_column}",
                    marker_color="black",
                    orientation="h",
                ),
            )

        fig.update_layout(title_text=f"{title}")

        return fig

    def value_count_bar_plot(self, categorical_column, total_column, percent=False):
        """
        Created using Plotly Bar Charts: https://plotly.com/python/bar-charts/.

        Creates a plot counting the values of a categorical column
        :param categorical_column: The column with categorical values
        :return: The figure of the plot, ready to be showed.
        """
        self.sample_df = self.sample_df.sort_values(by=total_column)
        values = self.sample_df[total_column]
        values_perc = [round(value / sum(values) * 100, 2) for value in values]
        categories = self.sample_df[categorical_column]

        title = (
            f"Valores em Percentual: {total_column}"
            if percent
            else f"Valores em Quantidade: {total_column}"
        )
        fig = go.Figure()

        if percent:
            fig.add_trace(
                go.Bar(
                    x=categories,
                    y=values_perc,
                    name=f"{categorical_column}",
                    orientation="v",
                    marker={"color": list(range(-10, 20))},
                ),
            )
        else:
            fig.add_trace(
                go.Bar(
                    x=categories,
                    y=values,
                    name=f"{categorical_column}",
                    orientation="v",
                    marker={"color": list(range(-10, 20))},
                ),
            )

        fig.update_layout(title_text=f"{title}")

        return fig
