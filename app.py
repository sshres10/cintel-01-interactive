import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Set the title for the page
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)
    ui.page_opts(title="PyShiny App with Plot", fillable=True) # Added title

# Define the histogram plotting function
@render.plot
def histogram():
    np.random.seed(72)
    x = 100 + 15 * np.random.randn(500)  
    plt.hist(x, bins=input.selected_number_of_bins(), density=True)
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.title('Dynamic Histogram')
    return plt.gcf()  
