from reactpy import component,html, use_state
import reactpy


@component
def Form(setTypeBook,setModalShow ,modalShow):
    
    year, setYear = use_state('')
    reason, setReason = use_state('')
    time, setTime = use_state('')
    count, setCount = use_state('')

    @reactpy.event(prevent_default=True)
    def handleSubmit(event):
        setTypeBook({
            'edad':f'{year}',
            'motivo':f'{reason}',
            'tiempo':f'{time}',
            'cantidad':f'{count}',
        })
    
    
    attrItem = {
        "class":"mb-3"
    }
    attrLabel = {
        "class":"block mb-2 text-sm font-medium ",
        "style":{
            "fontFamily":"Montserrat"
        }
    }

    attrSubmit = {
        "class":"block h-[2.68rem] cursor-pointer transition-all duration-300 hover:bg-black hover:text-white px-4 w-[max-content] rounded-full border-2 border-black  mt-6  ",
        
        'type':'submit',
        'value':'Consultar'
    }
    attrSelect = {"on_change": lambda e : setYear(e['target']['value'])}
    
    attrForm = {
    "on_submit": handleSubmit,
    "style":{
        
    }
}
    return html.form(
        attrForm,
        html.div(
            attrItem,
            html.label(attrLabel,'Edad:'),
            html.select(
                {"on_change": lambda e : setYear(e['target']['value'])},
                html.option({'value':''},'Selecciona la edad'),
                html.option({'value':'Niño menor de 11 años'},'Niño menor de 11 años'),
                html.option({'value':'Adolescente'},'Adolescente'),
                html.option({'value':'Joven de 19 a 25 años'},'Joven de 19 a 25 años'),
                html.option({'value':'Joven de 19 a 25 años'},'Adulto'),
            )
        ),
        html.div(
            attrItem,
            html.label(attrLabel,'Tiempo para acabar su libro'),
            html.select(
                {"on_change": lambda e : setTime(e['target']['value'])},
                html.option({'value':''},'Selecciona el tiempo'),
                html.option({'value':'1 semana'},'1 semana'),
                html.option({'value':'2 semanas'},'2 semanas'),
                html.option({'value':'1 mes'},'1 mes'),
                html.option({'value':'Más de 2 meses'},'Más de 2 meses'),
            )
        ),
        html.div(
            attrItem,
            html.label(attrLabel,'Motivo de Lectura'),
            html.select(
                {"on_change": lambda e : setReason(e['target']['value'])},
                html.option({'value':''},'Selecciona tu motivo de lectura'),
                html.option({'value':'Distracción'},'Distracción'),
                html.option({'value':'Aprender'},'Aprender'),
                html.option({'value':'Interés'},'Interés'),
                html.option({'value':'Curiosidad'},'Curiosidad'),
            )
        ),
        html.div(
            attrItem,
            html.label(attrLabel,'Cantidad a Pagar'),
            html.select(
                {"on_change": lambda e : setCount(e['target']['value'])},
                html.option({'value':''},'Selecciona la cantidad a pagar'),
                html.option({'value':'Menos de $250'},'Menos de $250'),
                html.option({'value':'Entre $300 y $400'},'Entre $300 y $400'),
                html.option({'value':'$500 o más'},'$500 o mas'),
            )
        ),
        html.input(attrSubmit)
    )


