#!/usr/bin/env python3
import sys
from PIL import ImageDraw, ImageFont, Image

class TitleCard:
    def __init__(
            self,
            font_path='/usr/share/fonts/truetype/source-code-pro-ttf/SourceCodePro-Bold.ttf',
            font_size=172,
            border=50,
            width=1920,
            height=1080,
            title_color='#EBC805FF',
            name_color='#FFFFFFFF'
    ):
        self.font = ImageFont.truetype(
            font=font_path,
            size=font_size
        )

        self.border = border
        self.width = width
        self.height = height
        self.title_color = title_color
        self.name_color = name_color

    def _get_width(self, draw, text):
        width, _  = draw.textsize(text, font=self.font)
        return width

    def _line_break(self, draw, text):
        # We need to know how long a space is
        space_width = self._get_width(draw, ' ')

        new_line = True
        space_left = self.width - (self.border*2)
        output = ''

        for word in text.split(' '):
            curr = self._get_width(draw, word)
            if (curr + space_width) > space_left:
                if new_line == True:
                    # can't place without splitting the word.
                    raise
                else:
                    # add a new break and reset
                    new_line = True
                    space_left = self.width - (self.border*2)
                    output += ('\n' + word)
            else:
                # we have space left.
                space_left -= (curr + space_width)
                output += (word + ' ')
                new_line = False

        return output

    def generate(self, title, name):
        im = Image.new('RGBA', (self.width, self.height))
        draw = ImageDraw.Draw(im)
        # First step involves figuring out whenever we need 

        _, title_y = draw.multiline_textsize(title, font=self.font)
        _, name_y = draw.multiline_textsize(name, font=self.font)

        # check we don't overflow the bounds
        if (title_y + self.border) > (self.height - name_y - self.border):
            raise 

        draw.multiline_text(
            (self.border, self.border),
            self._line_break(draw, title),
            fill=self.title_color,
            font=self.font
        )

        draw.multiline_text(
            (self.border, (self.height - name_y - self.border)),
            self._line_break(draw, name),
            fill=self.name_color,
            font=self.font
        )

        return im



if __name__ == '__main__':
    tc = TitleCard()
    title = sys.argv[1]
    name = sys.argv[2]
    filename = sys.argv[3]
    tc.generate(title, name).save(filename)
