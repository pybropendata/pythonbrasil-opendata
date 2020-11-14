import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


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
        values_perc = [round(value/ sum(values)*100,2) for value in values]
        categories = self.sample_df[categorical_column].unique().tolist()

        title = f"Valores em Percentual: {categorical_column}" if percent else f"Valores em Quantidade: {categorical_column}"
        fig = go.Figure()

        if percent:
            fig.add_trace(
                go.Bar( x=values_perc,y=categories,name=f"{categorical_column}", marker_color="black",orientation='h'),
            )
        else:
            fig.add_trace(
                go.Bar( x=values,y=categories,name=f"{categorical_column}", marker_color="black",orientation='h'),
            )
            
        fig.update_layout(title_text=f"{title}")

        return fig

    def histogram_plot(
        self, x_column, custom_n_bins=20, color=None, see_distribution=False
    ):
        """
        Created using Plotly Histogram: https://plotly.com/python/histograms/.

        Creates a histogram of the x_column. If another column goes in the color param,
        it separates the data according to that column.

        :param x_column: An df column to be used as x axis in the histogram.
        :param custom_n_bins: The number of divisions in the x axis of the histogram.
        :param color: An df column to be used to separate the data according to it.
        :param see_distribution: Bool that if true shows the distribution of the values.

        :return:  The figure of the plot, ready to be showed.
        """
        if see_distribution:
            fig = px.histogram(
                self.sample_df,
                x=x_column,
                color=color,
                marginal="box",
                nbins=custom_n_bins,
                title=f"Histogram chart using column {x_column}",
            )

        else:
            fig = px.histogram(
                self.sample_df,
                x=x_column,
                color=color,
                nbins=custom_n_bins,
                title=f"Histogram chart using column {x_column}",
            )

        plt.figure(
            figsize=(8, 4),
            dpi=80,
        )

        return fig
