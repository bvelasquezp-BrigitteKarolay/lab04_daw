from interpreter import draw
from chessPictures import *

draw(
    square.negative().join(square).horizontalRepeat(4)
    .under(
        square.join(square.negative()).horizontalRepeat(4)
    ).verticalRepeat(2)
)