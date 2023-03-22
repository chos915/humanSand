# -*- coding:utf-8 -*-
import streamlit as st
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import numpy as np


def main():
    
    st.title("HI")
    
      # color Picker
    color = st.color_picker('색상 선택')
    # st.write(color)

    # matplotlib
    data = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(data, bins=20, color = color)
    ax.set_title("dddd")

    st.pyplot(fig)
    

    # plotly chart
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    hist_data = [x1, x2, x3] 
    group_labels = ['Group 1', 'Group 2', 'Group 3']

    fig = ff.create_distplot(
        hist_data, group_labels, bin_size = [.1, .25, .5]
    )

    st.plotly_chart(fig, use_container_width=True)

    
if __name__ == "__main__":
    main()