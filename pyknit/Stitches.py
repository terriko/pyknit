from PIL import Image, ImageDraw, ImageFont


def box(fname, cell_width, cell_height, stitch_width):
    chart_image = Image.new(
        "RGB", (cell_width*stitch_width, cell_height), "#ffffff"
    )

    # draw some gridlines
    draw = ImageDraw.Draw(chart_image)
    chart_image.save(fname+".png")

def cable(fname, cell_width, cell_height, front_sts, back_sts, direction="F", purl=False, ):
    stitch_width = front_sts + back_sts
    chart_image = Image.new(
        "RGB", (cell_width*stitch_width, cell_height), "#ffffff"
    )

    # draw some gridlines
    draw = ImageDraw.Draw(chart_image)
    # Border
    draw.rectangle(
                ((0,0), (stitch_width*cell_width, cell_height)),
                fill="white",
                outline="black"
            )
    # Back stitches
    back_fill = "black" if purl else "white"
    draw.polygon(((0,0), (back_sts*cell_width,0),
        (stitch_width*cell_width, cell_height), (front_sts*cell_width, cell_height)), fill=back_fill, outline="black")
    draw.polygon(( (back_sts*cell_width,0), (stitch_width*cell_width, 0),
        (front_sts*cell_width, cell_height), (0, cell_height)), fill="white", outline="black")

    chart_image.save(fname+"R.png")
    flipped = chart_image.transpose(Image.FLIP_LEFT_RIGHT)
    flipped.save(fname+"L.png")


def main():
    cable("symbols/cable", 50, 50, 2, 2)


if __name__=='__main__':
    main()