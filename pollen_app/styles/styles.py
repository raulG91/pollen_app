
from enum import Enum
STYLESHEET = ["https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap"]

class Color(Enum):
     FOOTER = "#808080",
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
style = {
    "font_family": "Open Sans",
}

footer_style = {
    "width": "100%",
    "font_size": Size.DEFAULT,
    "height": "40px"

}
