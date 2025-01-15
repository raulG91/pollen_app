import reflex as rx
from pollen_app.styles.styles import footer_style,Size

def footer() -> rx.Component:
    return rx.el.footer(
        rx.flex(
            rx.vstack(
                rx.text("Autor Raúl García",size="3",weight="bold",),
            ),
            rx.hstack(
                rx.link(rx.icon(tag="github"),
                    href="https://github.com/raulG91/pollen_app",
                    underline="always",
                    is_external= True),
                ),
            rx.hstack(
                rx.link(rx.icon(tag="linkedin"),
                href="https://www.linkedin.com/in/raul-garcia-pedrosa-35a014118",
            underline="always",
            is_external=True
        )
        ),

        style=footer_style,
        direction="row",
        align="center",
        justify="center",
        spacing= "3",
        bg=rx.color("accent", 3),

    )

    ) 
        