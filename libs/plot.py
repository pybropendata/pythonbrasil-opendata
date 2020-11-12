import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


class CreatePlot:
    def __init__(self, sample_df):
        self.sample_df = sample_df

    def categorical_count_bar_plot(self, categorical_column):
        """
        Created using Plotly Bar Charts: https://plotly.com/python/bar-charts/.

        Creates a plot counting the values of a categorical column
        :param categorical_column: The column with categorical values
        :return: The figure of the plot, ready to be showed.
        """
        y_values = self.sample_df[categorical_column].value_counts().tolist()

        x_values = self.sample_df[categorical_column].unique().tolist()

        fig = px.bar(
            data_frame=self.sample_df,
            x=x_values,
            y=y_values,
            title=f"Categorical Count Bar chart using column {categorical_column}",
        )

        plt.figure(
            figsize=(8, 4),
            dpi=80,
        )

        return fig

    def histogram_plot(self, x_column, custom_n_bins=20, color=None, see_distribution=False):
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
                self.sample_df, x=x_column, color=color,
                marginal="box", nbins=custom_n_bins,
                title=f"Histogram chart using column {x_column}"
            )

        else:
            fig = px.histogram(
                self.sample_df, x=x_column, color=color,
                nbins=custom_n_bins,
                title=f"Histogram chart using column {x_column}",
            )

        plt.figure(
            figsize=(8, 4),
            dpi=80,
        )

        return fig