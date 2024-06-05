INTERFACE_DARK = u"""@font-face {
    font-family: NovaFlat;
    src:  format(\truetype\);
}
*{
color: #fff;
font-family: url(:/fonts/Nova_Flat/NovaFlat-Regular.ttf);
font-size: 12px;
border: nine;
background: none;"}
#centralwidget{
background-color: rgb(33, 43, 51);
}
#left_menu_widget, #percentage_bar_chart, #nested_donuts,
#line_charts, #bar_charts{ 
background-color: rgba(61, 80, 95, 100)
}
#header_frame, #frame_3, #frame_5{
background-color: rgb(61, 80, 95);
}
#frame_4 QPushButton{
padding: 10px;
border-radius: 5px;
background-color: rgba(33, 43, 51, 100);
}
#header_nav QPushButton{
	background-color: rgb(61, 80, 95);
	border-radius: 15px;
	border: 3px solid rgb(120, 157, 186);
}
#header_nav QPushButton:hover{
	background-color: rgb(120, 157, 186);
}
"""

INTERFACE_LIGHT = u"""
@font-face {
    font-family: NovaFlat;
    src:  format(\truetype\);
}

* {
    color: #000;
    font-family: url(./Nova_Flat/NovaFlat-Regular.ttf);
    font-size: 12px;
    border: none;
    background: none;
}

#centralwidget {
    background-color: #f5f5f5;
}

#left_menu_widget,
#percentage_bar_chart,
#nested_donuts,
#line_charts,
#bar_charts {
    background-color: rgba(240, 240, 240, 1);
}

#header_frame,
#frame_3,
#frame_5 {
    background-color: #f0f0f0;
}

#frame_4 QPushButton {
    padding: 10px;
    border-radius: 5px;
    background-color: rgba(255, 255, 255, 1);
}

#header_nav QPushButton {
    background-color: #f0f0f0;
    border-radius: 15px;
    border: 3px solid #789dbe;
}

#header_nav QPushButton:hover {
    background-color: #789dbe;
}

"""


MAIN_MENU_DARK = u"""
* {
    color: #fff;
    font-family: url(./Nova_Flat/NovaFlat-Regular.ttf);
    font-size: 12px;
    border: none;
    background: none;
}

#centralwidget {
    background-color: rgb(33, 43, 51);
}

#left_menu_widget, #percentage_bar_chart, #nested_donuts,
#line_charts, #bar_charts, #temperature_bar_chart {
    background-color: rgba(61, 80, 95, 100);
}

#header_nav, #frame_3, #frame_5 {
    background-color: rgb(61, 80, 95);
}

#frame_4 QPushButton {
    padding: 10px;
    border-radius: 5px;
    background-color: rgba(33, 43, 51, 100);
}

#header_nav QPushButton{
    background-color: rgb(61, 80, 120);
    border-radius: 15px;
    border: 3px solid rgb(120, 157, 186);
}

#header_nav QPushButton:hover{
    background-color: rgb(120, 157, 186);
}
"""

MAIN_MENU_LIGHT = u"""
* {
    color: #000;
    font-family: url(:/fonts/Nova_Flat/NovaFlat-Regular.ttf);
    font-size: 12px;
    border: none;
    background: rgb(102, 153, 204);
}

#header_nav, #frame_3, #frame_5, QLabel, #frame_6,
#frame_2, #controlButtons{
    background-color: rgb(255, 255, 240);
    
}

#frame_4 QPushButton {
    padding: 10px;
    border-radius: 5px;
    background-color: rgba(220, 220, 220, 100);
}

#header_nav QPushButton {
    background-color: rgb(140, 146, 172);
    border-radius: 15px;
}

#header_nav QPushButton:hover {
    background-color: rgb(180, 180, 180);
}
"""

MAIN_ICON_PATH = './icons/noun-prediction.png'
CHARTS_ICON_PATH = './icons/noun-chart.png'