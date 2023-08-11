from reactpy import component,html

@component
def Book(motivo,edad,img):
    return html.div(
        html.p(motivo),
        html.p(edad),
        html.img({
            'src':f'{img}'
        })
    )