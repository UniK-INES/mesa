"""Solara based visualization for Mesa models."""

from .components.altair import make_space_altair
from .components.matplotlib import make_plot_measure, make_space_matplotlib
from .output import OutputWidgetHandler, freeze_logs, show_logs
from .solara_viz import JupyterViz, SolaraViz
from .UserParam import Slider

__all__ = [
    "JupyterViz",
    "SolaraViz",
    "Slider",
    "make_space_altair",
    "make_space_matplotlib",
    "make_plot_measure",
    "OutputWidgetHandler",
    "show_logs",
    "freeze_logs",
]
