import reflex as rx

def nav_bar()->rx.Component:
    return rx.box(
            rx.desktop_only(
                rx.hstack(
                    rx.hstack(
                        rx.image(
                            src="/Pollen_App.png",
                            width="2.75em",
                            height="auto",
                            border_radius="25%",
                        ),
                        rx.heading(
                            "Polen App", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Pollen App", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        width="100%",
    )