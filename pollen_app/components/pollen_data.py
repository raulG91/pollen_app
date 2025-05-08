import reflex as rx
from pollen_app.styles.styles import Size
from  pollen_app.state import FormState

color_map = {
        0: "grey",
        1: "green",
        2: "green",
        3: "yellow",
        4: "orange",
        5: "red"
    }  

def data_table() ->rx.Component:
    return rx.vstack()

def form_data(layout)-> rx.Component:

    return layout(  
                rx.hstack(
                    rx.text("Provincia"),
                    rx.select(
                        FormState.provinces,
                        value= FormState.selected_province,
                        on_change=FormState.on_change_province,
                        label="Provincia",
                        name="province"
                    ),
                    
                ),
                rx.hstack(
                    rx.text("Municipio"),
                    rx.select(
                        FormState.towns_list,
                        value = FormState.selected_town,
                        on_change=FormState.on_change_town,
                        label= "Municipio",
                        name="town"
                    )
                ),
                rx.hstack(
                    rx.button("Buscar", type="submit"),
                    
                ),                    
                width="100%",
                align_items="center",
                justify_content="center"

            )
def display_value(value:int)->rx.Component:

   
    return rx.cond(
        value == 0,
        rx.table.cell(rx.icon("circle", color=color_map[0],stroke_width=0,fill=color_map[0]),align="center"),
        rx.cond(
            (value == 1) | (value == 2),
            rx.table.cell(rx.icon("circle", color=color_map[1],fill=color_map[1],stroke_width=0),align="center"),
            rx.cond(
                value == 3,
                rx.table.cell(rx.icon("circle", color=color_map[3],fill=color_map[3],stroke_width=0),align="center"),
                rx.cond(
                    value == 4,
                    rx.table.cell(rx.icon("circle", color=color_map[4],fill=color_map[4],stroke_width=0),align="center"),
                    rx.table.cell(rx.icon("circle", color=color_map[5],fill= color_map[5],stroke_width=0),align="center"),

                )
            )

        )
        )


def display_row(data_row:dict)->rx.Component:
    return rx.table.row(
                rx.table.row_header_cell(data_row[0],font_size=["0.8em", "0.9em", "1em"]),
                display_value(data_row[1][0]),
                display_value(data_row[1][1]),
                display_value(data_row[1][2]),
                display_value(data_row[1][3]),
                display_value(data_row[1][4])
                

                
  
    )
def pollen_data() -> rx.Component:
    return rx.box(
        rx.form(
            rx.mobile_and_tablet(
                form_data(rx.vstack)
                          
            ),
            rx.desktop_only(
                form_data(rx.hstack)
            ),
            on_submit = FormState.submit_form,
            reset_on_submit=True
        ),
        rx.cond(
            FormState.pollen_data,
            data_table(),
            empty()
        )
    )
def empty() -> rx.Component:
    return rx.vstack()

def data_table() -> rx.Component:
    #Display table information
    return rx.box(
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Fecha",font_size=["0.8em", "0.9em", "1em"]),
                        rx.table.column_header_cell(FormState.dates[0],font_size=["0.8em", "0.9em", "1em"]),
                        rx.table.column_header_cell(FormState.dates[1],font_size=["0.8em", "0.9em", "1em"]),
                        rx.table.column_header_cell(FormState.dates[2],font_size=["0.8em", "0.9em", "1em"]),
                        rx.table.column_header_cell(FormState.dates[3],font_size=["0.8em", "0.9em", "1em"]),
                        rx.table.column_header_cell(FormState.dates[4],font_size=["0.8em", "0.9em", "1em"])
                    ),
                ),
                rx.table.body(
                    rx.foreach(
                        FormState.pollen_data,
                        display_row #Display value for current plant
                    ),
                ),  
            margin_top = "20px"),   
            leyend()
    )

def leyend() ->rx.Component:

#Define legend for table
    return  rx.vstack(
                rx.hstack(
                    rx.hstack(
                        rx.icon("circle", color=color_map[0],stroke_width=0,fill=color_map[0]),
                        rx.text("Nulo",font_size=["0.8em", "0.9em", "1em"])
                    ),
                    rx.hstack(
                        rx.icon("circle", color=color_map[1],stroke_width=0,fill=color_map[1]),
                        rx.text("Bajo",font_size=["0.8em", "0.9em", "1em"])
                    ),
                    rx.hstack(
                        rx.icon("circle", color=color_map[3],stroke_width=0,fill=color_map[3]),
                        rx.text("Moderado",font_size=["0.8em", "0.9em", "1em"])
                    ),
                    rx.hstack(
                        rx.icon("circle", color=color_map[4],stroke_width=0,fill=color_map[4]),
                        rx.text("Alto",font_size=["0.8em", "0.9em", "1em"])
                    ),
                    rx.hstack(
                        rx.icon("circle", color=color_map[5],stroke_width=0,fill=color_map[5]),
                        rx.text("Muy alto",font_size=["0.8em", "0.9em", "1em"])
                    ),
                ),
                width="100%",
                align="center",
                margin_top = "15px"
            ) 

        




