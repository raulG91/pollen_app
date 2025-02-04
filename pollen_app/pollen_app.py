"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from pollen_app.state import FormState

from rxconfig import config
from  .components.footer import footer
import pollen_app.styles.styles as Styles
from .components.pollen_data import pollen_data
from .components.navbar import nav_bar


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.flex(
            nav_bar(),
            rx.color_mode.button(position="top-right"),
            rx.vstack(
                
                rx.box(
                    pollen_data(),  # Wrap pollen_data in a box for isolation
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    width="100%",
                    margin_top ="10px"
                ),
                spacing="5",
                justify="center",
            ),
            direction="column",
            #justify="between",
            
            min_height="95vh",  # Ensure the full height is distributed
        ),
        footer(),
    )
meta=[
    {"author": "Raul Garcia"},
    {"char_set":"UTF-8"},
    {"description":"Polen App"},
    {"keywords": "Polen, Pollen, España, Andalucia"},
    {"og:title": "Polen APP"},
    {"og:description": "Polen App"}
]


app = rx.App(stylesheets = Styles.STYLESHEET,
            style=Styles.style)

app.add_page(index,title="Polen app",description="Polen app",meta=meta,on_load=FormState.on_load)
