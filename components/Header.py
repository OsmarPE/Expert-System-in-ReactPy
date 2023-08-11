from reactpy import component,html


@component
def Header(title = 'titulo'):
    return html.header({
        "class":" tracking-[0.2875rem] mb-8 uppercase font-medium flex items-center gap-2"
    },
        html.i({'class':'ri-book-line','style':{'fontSize':'20px'}}),
        html.h1(title),
    )